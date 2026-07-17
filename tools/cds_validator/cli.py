"""Command-line interface of the CDS offline token validator (DEC-S-094).

Entry point: ``python -m tools.cds_validator``. Commands: ``version``,
``validate-file``, ``validate-cases``, ``digest``. Exit codes:

validate-file: 0 Pass / Pass with limitations · 1 Fail · 2 Blocked ·
3 configuration/contract/internal error.
validate-cases: 0 all actual results match the committed expected results ·
1 at least one expected/actual mismatch · 2 execution blocked by a contract,
input, or dependency problem · 3 internal validator error.

A negative fixture whose expected Fail/Blocked state is recognized correctly
is a successful harness observation, not a harness failure (DEC-S-102).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.cds_validator import json_loader, reporting
from tools.cds_validator.canonicalization import (
    CANONICALIZATION_METHOD,
    DIGEST_ALGORITHM,
    DigestError,
    content_digest,
)
from tools.cds_validator.models import ResultState
from tools.cds_validator.schema_registry import SchemaRegistry, UnknownSchemaError
from tools.cds_validator.validation import ValidationEngine
from tools.cds_validator.version import (
    DTCG_REPORT_VERSION,
    PROFILE_VERSION,
    SCHEMA_IDS,
    VALIDATOR_VERSION,
    dependency_versions,
    runtime_identity,
)

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_BLOCKED = 2
EXIT_INTERNAL = 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.cds_validator",
        description="CDS offline token profile validator (Experimental; "
                    "executor-produced evidence, no Candidate status).")
    parser.add_argument(
        "--repository-root", default=".",
        help="Repository root containing the schemas/ directory (default: cwd).")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("version", help="Print validator/runtime/schema identities.")

    validate_file = commands.add_parser(
        "validate-file", help="Run the applicable V1–V4 layers on one document.")
    validate_file.add_argument("input", help="Document path (.tokens.json / "
                               ".source-set.json / .resolver.json).")
    validate_file.add_argument("--manifest", help="Optional Source-Set Manifest path.")
    validate_file.add_argument("--resolver", help="Optional Resolver document path.")
    validate_file.add_argument("--report", help="Optional JSON report output path.")

    validate_cases = commands.add_parser(
        "validate-cases", help="Run all validation cases and compare "
                               "actual against committed expected results.")
    validate_cases.add_argument("cases", help="Validation-case matrix path.")
    validate_cases.add_argument("--report", help="Optional JSON report output path.")
    validate_cases.add_argument("--digests", help="Optional digest report output path.")

    digest = commands.add_parser(
        "digest", help="RFC 8785 + SHA-256 content digest of a strict-JSON document.")
    digest.add_argument("input", help="Strict-JSON document path.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.repository_root).resolve()
    try:
        if args.command == "version":
            return _cmd_version(root)
        if args.command == "digest":
            return _cmd_digest(Path(args.input))
        registry = SchemaRegistry(root)
        engine = ValidationEngine(root, registry)
        if args.command == "validate-file":
            return _cmd_validate_file(engine, args)
        if args.command == "validate-cases":
            return _cmd_validate_cases(engine, registry, root, args)
        return EXIT_INTERNAL
    except (UnknownSchemaError, json_loader.LoaderError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return EXIT_BLOCKED
    except Exception as exc:  # noqa: BLE001 — CLI boundary, stable exit code 3
        print(f"INTERNAL ERROR (CDS-INTERNAL): {exc!r}", file=sys.stderr)
        return EXIT_INTERNAL


def _cmd_version(root: Path) -> int:
    payload = {
        "validatorVersion": VALIDATOR_VERSION,
        "pythonVersion": runtime_identity()["pythonVersion"],
        "cdsProfileVersion": PROFILE_VERSION,
        "dtcgReportVersion": DTCG_REPORT_VERSION,
        "schemaIds": SCHEMA_IDS,
        "dependencyVersions": dependency_versions(),
        "canonicalizationMethod": CANONICALIZATION_METHOD,
        "digestAlgorithm": DIGEST_ALGORITHM,
    }
    print(json.dumps(payload, indent=2))
    return EXIT_OK


def _cmd_digest(path: Path) -> int:
    try:
        print(content_digest(json_loader.load_path(path)))
        return EXIT_OK
    except json_loader.DuplicateKeyError as exc:
        print(f"FAIL (V1, no digest): {exc}", file=sys.stderr)
        return EXIT_FAIL
    except json_loader.LoaderError as exc:
        print(f"FAIL (V1, no digest): {exc}", file=sys.stderr)
        return EXIT_FAIL
    except DigestError as exc:
        print(f"BLOCKED (no digest): {exc}", file=sys.stderr)
        return EXIT_BLOCKED


def _cmd_validate_file(engine: ValidationEngine, args) -> int:
    paths = [Path(args.input)]
    if args.manifest:
        paths.append(Path(args.manifest))
    if args.resolver:
        paths.append(Path(args.resolver))
    result = engine.validate_scope(paths)
    outcome = result.outcome
    payload = {
        "input": str(args.input),
        "results": outcome.as_dict(),
        "rationales": outcome.rationales,
        "blockingLayer": outcome.blocking_layer(),
        "diagnostics": [d.to_json() for d in outcome.diagnostics],
    }
    print(json.dumps(payload, indent=2))
    if args.report:
        reporting.write_json(Path(args.report), payload)
    states = set(outcome.as_dict().values())
    if ResultState.FAIL.value in states:
        return EXIT_FAIL
    if ResultState.BLOCKED.value in states:
        return EXIT_BLOCKED
    return EXIT_OK


def _cmd_validate_cases(engine: ValidationEngine, registry: SchemaRegistry,
                        root: Path, args) -> int:
    started_at = reporting.utc_now()
    case_document = json_loader.load_path(Path(args.cases))
    schema_errors = registry.iter_errors("validation-case", case_document)
    if schema_errors:
        for error in schema_errors[:5]:
            print(f"BLOCKED: case matrix schema violation: {error.message}",
                  file=sys.stderr)
        return EXIT_BLOCKED

    case_results = []
    digest_entries: dict[str, str] = {}
    undigestible: dict[str, str] = {}
    for case in case_document["cases"]:
        case_results.append(
            _run_case(engine, root, case, digest_entries, undigestible))

    limitations = [
        "V2 covers only the bounded DTCG 2025.10 subset required by the CDS "
        "profile and the committed fixtures (DEC-S-098); unsupported DTCG "
        "areas (full color-module value validation, resolver modifier "
        "semantics, composite-type internals) are not validated and are not "
        "represented as passed.",
        "V4 assesses only objectively machine-checkable aspects; status "
        "truth, semantics, accessibility relevance, and compatibility "
        "remain human/governance review (Not assessed).",
        "This report is executor-produced, pre-commit evidence and is not "
        "independently reviewed (DEC-S-103); it confers no Candidate, "
        "Stable, conformance, or release status (DEC-S-104).",
    ]
    report = reporting.build_report(root, case_results, started_at, limitations)
    result_schema_errors = registry.iter_errors("validation-result", report)
    if result_schema_errors:
        for error in result_schema_errors[:5]:
            print(f"INTERNAL: result schema violation: {error.message}",
                  file=sys.stderr)
        return EXIT_INTERNAL

    if args.report:
        reporting.write_json(Path(args.report), report)
    if args.digests:
        reporting.write_json(Path(args.digests), {
            "reportVersion": reporting.REPORT_VERSION,
            "canonicalizationMethod": CANONICALIZATION_METHOD,
            "digestAlgorithm": DIGEST_ALGORITHM,
            "digestNote": "Content digests are integrity aids over parsed "
                          "content; they are not signatures and prove no "
                          "authorship, approval, or release (DEC-S-100).",
            "digests": digest_entries,
            "undigestible": undigestible,
        })

    summary = report["summary"]
    print(json.dumps(summary, indent=2))
    if summary["executionErrors"]:
        return EXIT_INTERNAL
    if summary["expectedMatches"] != summary["totalCases"]:
        return EXIT_FAIL
    return EXIT_OK


def _run_case(engine: ValidationEngine, root: Path, case: dict,
              digest_entries: dict[str, str],
              undigestible: dict[str, str]) -> dict:
    fixture_paths = case["fixturePaths"]
    expected = {
        "V1": case["expectedV1"], "V2": case["expectedV2"],
        "V3": case["expectedV3"], "V4": case["expectedV4"],
    }
    entry = {
        "caseId": case["caseId"],
        "fixturePaths": fixture_paths,
        "classification": case["classification"],
        "expected": expected,
        "actual": {},
        "expectedMatch": False,
        "blockingLayer": "none",
        "diagnostics": [],
        "contentDigests": {},
        "sourceRevisions": {},
        "executionStatus": "executed",
    }
    try:
        result = engine.validate_scope([root / p for p in fixture_paths])
    except Exception as exc:  # noqa: BLE001 — recorded, surfaces as exit 3
        entry["executionStatus"] = f"internal-error: {exc!r}"
        return entry

    outcome = result.outcome
    entry["actual"] = outcome.as_dict()
    entry["blockingLayer"] = outcome.blocking_layer()
    entry["diagnostics"] = [d.to_json() for d in outcome.diagnostics]

    layers_match = entry["actual"] == expected
    category_match = True
    expected_category = case.get("expectedDiagnosticCategory", "none")
    if case["classification"] == "negative" and expected_category != "none":
        categories = {d.category for d in outcome.diagnostics}
        category_match = expected_category in categories
    entry["expectedMatch"] = layers_match and category_match

    for doc in result.documents:
        rel = str(doc.path.relative_to(root)).replace("\\", "/")
        if doc.content is not None:
            try:
                digest = content_digest(doc.content)
                entry["contentDigests"][rel] = digest
                digest_entries[rel] = digest
            except DigestError as exc:
                undigestible[rel] = str(exc)
        else:
            undigestible[rel] = ("no digest: V1 parse failed "
                                 "(duplicate-key or invalid JSON, DEC-S-100)")
        payload = doc.payload or (
            doc.content if isinstance(doc.content, dict) else {}) or {}
        revision = payload.get("sourceRevision")
        if revision:
            entry["sourceRevisions"][rel] = revision
    return entry
