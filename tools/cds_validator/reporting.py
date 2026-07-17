"""Machine-readable validation reports (DEC-S-101).

Reports bind runtime, dependency, schema, profile, DTCG, case, source,
expected-result, actual-result, diagnostic, digest, and review-state
identities. ``independentReviewState`` is always ``pending`` here: the
producer of a report can never be its independent reviewer (DEC-S-103).
A worktree execution is never presented as a committed revision.
"""

from __future__ import annotations

import datetime
import json
import subprocess
from pathlib import Path
from typing import Any

from tools.cds_validator.canonicalization import (
    CANONICALIZATION_METHOD,
    DIGEST_ALGORITHM,
)
from tools.cds_validator.version import (
    DTCG_REPORT_VERSION,
    PROFILE_VERSION,
    SCHEMA_IDS,
    VALIDATOR_VERSION,
    dependency_versions,
    runtime_identity,
)

REPORT_VERSION = "1"
INDEPENDENT_REVIEW_STATE = "pending"


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def repository_identity(repository_root: Path) -> dict[str, str]:
    """Local, offline Git identity (read-only). Never claims a clean commit."""
    revision = "unknown"
    worktree_state = "unknown"
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=repository_root,
            capture_output=True, text=True, timeout=30, check=False)
        if head.returncode == 0:
            revision = head.stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain"], cwd=repository_root,
            capture_output=True, text=True, timeout=30, check=False)
        if status.returncode == 0:
            worktree_state = "clean" if not status.stdout.strip() else "modified worktree"
    except (OSError, subprocess.SubprocessError):
        pass
    return {"repositoryRevision": revision, "worktreeState": worktree_state}


def build_report(repository_root: Path, cases: list[dict[str, Any]],
                 started_at: str, limitations: list[str]) -> dict[str, Any]:
    matched = sum(1 for case in cases if case["expectedMatch"] is True)
    execution_errors = sum(
        1 for case in cases if case["executionStatus"] != "executed")
    identity = repository_identity(repository_root)
    return {
        "reportVersion": REPORT_VERSION,
        "validatorVersion": VALIDATOR_VERSION,
        "profileVersion": PROFILE_VERSION,
        "dtcgReportVersion": DTCG_REPORT_VERSION,
        "runtimeIdentity": runtime_identity(),
        "dependencyVersions": dependency_versions(),
        "executionIdentity": {
            "executedBy": "Claude (scoped executor)",
            "executionContext": "CDS-WP-013 offline fixture harness",
            "evidenceClass": "executor-produced, pre-commit, not independently reviewed",
        },
        "repositoryRevision": identity["repositoryRevision"],
        "worktreeState": identity["worktreeState"],
        "offlineMode": True,
        "schemaIds": dict(SCHEMA_IDS),
        "startedAtUtc": started_at,
        "completedAtUtc": utc_now(),
        "cases": cases,
        "summary": {
            "totalCases": len(cases),
            "expectedMatches": matched,
            "expectedMismatches": len(cases) - matched - execution_errors,
            "executionErrors": execution_errors,
            "canonicalizationMethod": CANONICALIZATION_METHOD,
            "digestAlgorithm": DIGEST_ALGORITHM,
        },
        "limitations": limitations,
        "independentReviewState": INDEPENDENT_REVIEW_STATE,
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
