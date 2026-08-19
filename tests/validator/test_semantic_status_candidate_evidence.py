"""CDS-WP-016 Candidate Accessibility Gate — evidence-suite unit tests.

These tests bind the test-only statement fixture, the evidence runner, the real
Semantic Status source, and the DE/EN terminology mapping together. They prove
structural and rule-level properties only. They prove no accessibility, no WCAG
conformance, no assistive-technology behaviour, no comprehension, no Candidate
status, and no admitted AE-1.

Since the result-format v2 rework (DEC-S-126) they additionally prove that the
runner holds **no governance state**: it reports what the evidenced bytes declare,
records a caller-declared authority context, and grants nothing. The synthetic
Proposed Candidate source used below is written to a temporary directory
**outside the repository**; the real Semantic Status source is never mutated, and
no `semantic-status-rev-0002-candidate` artifact is created in the repository.
"""

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tests.validator import semantic_status_candidate_evidence_runner as runner
from tools.cds_validator import json_loader
from tools.cds_validator.models import CDS_EXTENSION_ROOT
from tools.cds_validator.semantic_status import AUTHORIZED_AXES, EXPECTED_TOKEN_COUNT

REPO_ROOT = Path(__file__).resolve().parents[2]
CASES = (REPO_ROOT / "tests" / "fixtures" / "semantic-status-statements"
         / "CANDIDATE_EVIDENCE_CASES.json")
TOKEN_SOURCE = (REPO_ROOT / "tokens" / "semantic" / "status"
                / "semantic-status.tokens.json")
TERMINOLOGY = (REPO_ROOT / "docs" / "foundations"
               / "SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md")
MATRIX = (REPO_ROOT / "docs" / "operations"
          / "SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md")
RUNNER_SOURCE = (REPO_ROOT / "tests" / "validator"
                 / "semantic_status_candidate_evidence_runner.py")

#: Phrases that have no truthful use in an evidence fixture or an evidence
#: result at the current project state. `CDS certified` is prohibited outright;
#: the others would be conformance or accessibility claims, and none is valid.
FORBIDDEN_CLAIM_PHRASES = (
    "cds certified", "cds-certified",
    "wcag conformant", "wcag-conformant", "wcag compliant",
    "cds is accessible", "cds-conformant", "is candidate",
)

ALLOWED_COVERAGE_STATES = frozenset({
    "COVERED", "COVERED_WITH_LIMITATION", "REPRESENTATION_TRIGGERED_WITH_PLAN",
})

#: The committed, authoritative source revision. Unchanged by this rework.
CURRENT_SOURCE_REVISION = "semantic-status-rev-0001"

#: The revision identity DEC-S-126 **reserves** for a future Proposed Candidate
#: Revision. It is deliberately not created in the repository; it exists here
#: only inside a temporary synthetic fixture written outside the repository.
RESERVED_CANDIDATE_REVISION = "semantic-status-rev-0002-candidate"

#: Field names retired with result format v1. Their reappearance would mean the
#: runner had resumed asserting global governance state it has no authority over.
RETIRED_V1_BOUNDARY_FIELDS = (
    "maturityState", "approvalState", "candidateStatus",
    "admittedAccessibilityEvidenceLevel", "evidenceLevelProduced",
)

#: The v1 evidence artifacts. Immutable history: the schema bump must not have
#: rewritten them.
V1_EVIDENCE_RESULTS = (
    (REPO_ROOT / "artifacts" / "validation"
     / "wp016-candidate-accessibility-remediation-results.json"),
    (REPO_ROOT / "artifacts" / "validation"
     / "wp016-candidate-accessibility-clean-reexecution-results.json"),
)


def load_manifest():
    return json_loader.load_path(CASES)


def execute(source_revision=CURRENT_SOURCE_REVISION,
            source_authority_context="authoritative-current",
            token_source=TOKEN_SOURCE, worktree_state="unknown"):
    return runner.run(CASES, token_source, TERMINOLOGY,
                      "test-revision", source_revision,
                      source_authority_context, worktree_state)


def write_proposed_candidate_source(directory: Path) -> Path:
    """Write a synthetic Proposed Candidate copy of the real token source.

    Test-only data, written **outside the repository** and deleted afterwards.
    Only the governance metadata differs: `sourceRevision`, `maturityState`, and
    `approvalState` carry the *target* values a future Candidate revision would
    declare. The real source is never touched, and this creates no Candidate
    revision in CDS.
    """
    content = json_loader.load_path(TOKEN_SOURCE)
    payload = content["$extensions"][CDS_EXTENSION_ROOT]
    payload["sourceRevision"] = RESERVED_CANDIDATE_REVISION
    payload["maturityState"] = "Candidate"
    payload["approvalState"] = "Approved"
    target = directory / "proposed-candidate.tokens.json"
    target.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
    return target


class FixtureBoundaryTests(unittest.TestCase):
    """The fixture layer must declare itself test-only and non-normative."""

    @classmethod
    def setUpClass(cls):
        cls.manifest = load_manifest()

    def test_manifest_is_test_only_and_non_normative(self):
        self.assertIs(self.manifest["testOnly"], True)
        self.assertIs(self.manifest["nonNormative"], True)
        self.assertEqual(self.manifest["authority"], "evidence fixture only")

    def test_manifest_denies_every_contract_role(self):
        boundary = self.manifest["boundary"]
        for key in ("isCdsApi", "isSourceSet", "isSchema", "isConsumerContract",
                    "isProductProfile", "isChannelFormat", "approvedForRuntimeUse"):
            self.assertIs(boundary[key], False, key)
        self.assertTrue(boundary["statement"].strip())

    def test_case_ids_are_unique(self):
        ids = [case["caseId"] for case in self.manifest["cases"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_case_carries_subject_identity_and_declared_scope(self):
        # Composition Rules fields 1 and 2; reported separately from the eight
        # enumerated fail-closed conditions and never folded into them.
        for case in self.manifest["cases"]:
            statement = case["statement"]
            self.assertTrue(str(statement.get("subjectIdentity") or "").strip(),
                            case["caseId"])
            self.assertTrue(str(statement.get("declaredScope") or "").strip(),
                            case["caseId"])

    def test_no_unregistered_axis_or_value_outside_the_fail_closed_case(self):
        for case in self.manifest["cases"]:
            axes = case["statement"]["axes"]
            unregistered = [
                f"{axis}.{value}" for axis, value in axes.items()
                if axis not in AUTHORIZED_AXES or value not in AUTHORIZED_AXES[axis]
            ]
            if unregistered:
                # Only a case that deliberately provokes FC-2 may carry one.
                self.assertIn("FC-2", case["expectedFailClosed"],
                              f"{case['caseId']} {unregistered}")
            else:
                self.assertEqual(unregistered, [], case["caseId"])

    def test_expected_ids_are_registered(self):
        registered_rr = {row["id"] for row in self.manifest["reviewRequiredCombinations"]}
        registered_fc = {row["id"] for row in self.manifest["failClosedConditions"]}
        self.assertEqual(registered_rr, set(runner.REVIEW_REQUIRED_IDS))
        self.assertEqual(registered_fc, set(runner.FAIL_CLOSED_IDS))
        for case in self.manifest["cases"]:
            self.assertLessEqual(set(case["expectedReviewRequired"]), registered_rr)
            self.assertLessEqual(set(case["expectedFailClosed"]), registered_fc)


class ValueRequirementCoverageTests(unittest.TestCase):
    """All 25 Vocabulary Candidate evidence requirements must be mapped."""

    @classmethod
    def setUpClass(cls):
        cls.manifest = load_manifest()
        cls.result = execute()

    def test_authorized_identifiers_are_exactly_twenty_five(self):
        self.assertEqual(len(runner.authorized_value_ids()), EXPECTED_TOKEN_COUNT)

    def test_each_requirement_appears_exactly_once(self):
        ids = [row["id"] for row in self.manifest["valueRequirements"]]
        self.assertEqual(len(ids), EXPECTED_TOKEN_COUNT)
        self.assertEqual(len(set(ids)), EXPECTED_TOKEN_COUNT)
        self.assertEqual(set(ids), set(runner.authorized_value_ids()))

    def test_no_requirement_row_is_unmapped(self):
        coverage = self.result["valueRequirementCoverage"]
        self.assertEqual(coverage["unmapped"], [])
        self.assertEqual(coverage["covered"], EXPECTED_TOKEN_COUNT)
        self.assertEqual(coverage["expected"], EXPECTED_TOKEN_COUNT)
        self.assertTrue(coverage["satisfied"])
        self.assertEqual(coverage["duplicateRequirementIds"], [])
        self.assertEqual(coverage["unauthorizedRequirementIds"], [])

    def test_every_requirement_has_an_allowed_coverage_state(self):
        for row in self.manifest["valueRequirements"]:
            self.assertIn(row["coverageState"], ALLOWED_COVERAGE_STATES, row["id"])
            self.assertIn(row["evidenceType"],
                          ("MACHINE", "HUMAN_REVIEW", "MIXED",
                           "REPRESENTATION_TRIGGERED"), row["id"])
            self.assertTrue(row["requirement"].strip(), row["id"])

    def test_limited_coverage_states_carry_a_stated_limitation(self):
        for row in self.manifest["valueRequirements"]:
            if row["coverageState"] == "COVERED":
                continue
            self.assertTrue((row["limitation"] or "").strip(), row["id"])

    def test_each_requirement_has_at_least_one_asserting_case(self):
        for row in self.result["valueRequirementCoverage"]["rows"]:
            self.assertTrue(row["caseIds"], row["id"])
            self.assertEqual(row["missingCaseIds"], [], row["id"])
            self.assertTrue(row["assertingCaseIds"], row["id"])

    def test_requirements_matrix_document_lists_all_twenty_five(self):
        text = MATRIX.read_text(encoding="utf-8")
        for identifier in runner.authorized_value_ids():
            self.assertIn(identifier, text, identifier)


class RuleCoverageTests(unittest.TestCase):
    """Review-required and fail-closed coverage must be exactly 6/6 and 8/8."""

    @classmethod
    def setUpClass(cls):
        cls.result = execute()

    def test_review_required_coverage_is_six_of_six(self):
        coverage = self.result["reviewRequiredCoverage"]
        self.assertEqual(coverage["covered"], list(runner.REVIEW_REQUIRED_IDS))
        self.assertEqual(len(coverage["covered"]), 6)
        self.assertTrue(coverage["satisfied"])

    def test_fail_closed_coverage_is_eight_of_eight(self):
        coverage = self.result["failClosedCoverage"]
        self.assertEqual(coverage["covered"], list(runner.FAIL_CLOSED_IDS))
        self.assertEqual(len(coverage["covered"]), 8)
        self.assertTrue(coverage["satisfied"])

    def test_no_seventh_review_required_or_ninth_fail_closed_exists(self):
        self.assertEqual(len(runner.REVIEW_REQUIRED_IDS), 6)
        self.assertEqual(len(runner.FAIL_CLOSED_IDS), 8)

    def test_expected_and_actual_classifications_agree(self):
        self.assertEqual(self.result["failures"], [])
        self.assertEqual(self.result["blocked"], [])
        self.assertEqual(self.result["executionErrors"], [])
        for case in self.result["caseResults"]:
            self.assertTrue(case["expectedMatch"], case["caseId"])
            self.assertEqual(case["expectedReviewRequired"],
                             case["actualReviewRequired"], case["caseId"])
            self.assertEqual(case["expectedFailClosed"],
                             case["actualFailClosed"], case["caseId"])

    def test_not_applicable_without_rationale_is_both_rr4_and_fc6(self):
        # The Composition Rules list this state in both tables; neither is
        # silently reinterpreted as the other.
        rows = [c for c in self.result["caseResults"]
                if "FC-6" in c["actualFailClosed"]]
        self.assertTrue(rows)
        for row in rows:
            self.assertIn("RR-4", row["actualReviewRequired"], row["caseId"])
            self.assertEqual(row["actualClassification"], "fail-closed")

    def test_fail_closed_dominates_classification(self):
        for case in self.result["caseResults"]:
            if case["actualFailClosed"]:
                self.assertEqual(case["actualClassification"], "fail-closed",
                                 case["caseId"])
            elif case["actualReviewRequired"]:
                self.assertEqual(case["actualClassification"], "review-required",
                                 case["caseId"])
            else:
                self.assertEqual(case["actualClassification"], "representable",
                                 case["caseId"])


class SourceAndLocalizationStructureTests(unittest.TestCase):
    """Real-source description coverage and DE/EN structural coverage."""

    @classmethod
    def setUpClass(cls):
        cls.result = execute()

    def test_every_real_status_token_has_a_non_empty_description(self):
        coverage = self.result["sourceDescriptionCoverage"]
        self.assertEqual(coverage["described"], EXPECTED_TOKEN_COUNT)
        self.assertEqual(coverage["expected"], EXPECTED_TOKEN_COUNT)
        self.assertEqual(coverage["missing"], [])
        self.assertTrue(coverage["satisfied"])

    def test_de_en_structural_coverage_is_twenty_five_of_twenty_five(self):
        coverage = self.result["deEnStructuralCoverage"]
        self.assertEqual(coverage["rows"], EXPECTED_TOKEN_COUNT)
        self.assertEqual(coverage["expected"], EXPECTED_TOKEN_COUNT)
        self.assertEqual(coverage["englishLabels"], EXPECTED_TOKEN_COUNT)
        self.assertEqual(coverage["germanLabels"], EXPECTED_TOKEN_COUNT)
        self.assertTrue(coverage["satisfied"])

    def test_no_duplicate_missing_or_unauthorized_terminology_identifier(self):
        coverage = self.result["deEnStructuralCoverage"]
        self.assertEqual(coverage["duplicateIdentifiers"], [])
        self.assertEqual(coverage["missingIdentifiers"], [])
        self.assertEqual(coverage["unauthorizedIdentifiers"], [])
        self.assertEqual(coverage["rowsWithoutEnglishLabel"], [])
        self.assertEqual(coverage["rowsWithoutGermanLabel"], [])

    def test_structural_coverage_does_not_claim_semantic_equivalence(self):
        # Machine-checkable structure is not machine-checkable meaning.
        self.assertIn("not machine-checked",
                      self.result["deEnStructuralCoverage"]["boundary"])
        self.assertIn("no comprehension",
                      self.result["sourceDescriptionCoverage"]["boundary"])


class ResultBoundaryTests(unittest.TestCase):
    """The fixture and the result must claim nothing."""

    @classmethod
    def setUpClass(cls):
        cls.result = execute()
        cls.manifest = load_manifest()

    def test_result_declares_itself_test_only_and_non_normative(self):
        self.assertIs(self.result["testOnly"], True)
        self.assertIs(self.result["nonNormative"], True)
        self.assertEqual(self.result["schemaVersion"], runner.RESULT_SCHEMA_VERSION)

    def test_result_asserts_no_claim_conformance_or_human_approval(self):
        boundaries = self.result["boundaries"]
        self.assertEqual(boundaries["claims"], "none")
        self.assertEqual(boundaries["conformanceStatement"], "none")
        self.assertEqual(boundaries["humanApproval"], "none")
        # v1 asserted the project-wide maturity/approval/Candidate/AE state here.
        # The runner is not that authority, so those fields are gone for good.
        for retired in RETIRED_V1_BOUNDARY_FIELDS:
            self.assertNotIn(retired, boundaries, retired)

    def test_no_numeric_accessibility_score_is_produced(self):
        self.assertIs(self.result["scoreProduced"], False)
        serialized = json.dumps(self.result, ensure_ascii=False).lower()
        self.assertNotIn("percentage accessible", serialized)

    def test_neither_fixture_nor_result_carries_a_prohibited_claim_phrase(self):
        for name, blob in (("fixture", json.dumps(self.manifest, ensure_ascii=False)),
                           ("result", json.dumps(self.result, ensure_ascii=False))):
            lowered = blob.lower()
            for phrase in FORBIDDEN_CLAIM_PHRASES:
                self.assertNotIn(phrase, lowered, f"{name}: {phrase}")

    def test_result_status_is_an_allowed_value(self):
        self.assertIn(self.result["resultStatus"],
                      ("Pass", "Pass with limitations", "Fail", "Blocked"))

    def test_current_run_passes_with_declared_limitations(self):
        self.assertEqual(self.result["resultStatus"], "Pass with limitations")
        self.assertEqual(self.result["coverageStatesWithLimitation"],
                         ["COVERED_WITH_LIMITATION"])


class ResultFormatV2Tests(unittest.TestCase):
    """v2 separates what the source declares from what the run establishes."""

    @classmethod
    def setUpClass(cls):
        cls.result = execute()

    def test_schema_version_is_result_format_two(self):
        self.assertEqual(runner.RESULT_SCHEMA_VERSION,
                         "cds-wp016-candidate-accessibility-evidence-result/2")
        self.assertEqual(self.result["schemaVersion"],
                         runner.RESULT_SCHEMA_VERSION)
        self.assertTrue(self.result["schemaVersion"].endswith("/2"))

    def test_source_declared_metadata_is_read_from_the_evidenced_bytes(self):
        # The values are whatever the source says — not literals in the runner.
        declared = self.result["sourceDeclaredMetadata"]
        payload = (json_loader.load_path(TOKEN_SOURCE)["$extensions"]
                   [CDS_EXTENSION_ROOT])
        self.assertEqual(declared["sourceRevision"], payload["sourceRevision"])
        self.assertEqual(declared["maturityState"], payload["maturityState"])
        self.assertEqual(declared["approvalState"], payload["approvalState"])
        # And for the current committed source those values are:
        self.assertEqual(declared["sourceRevision"], CURRENT_SOURCE_REVISION)
        self.assertEqual(declared["maturityState"], "Experimental")
        self.assertEqual(declared["approvalState"], "Unapproved")
        self.assertIs(declared["declaresCandidateTargetMetadata"], False)

    def test_result_claims_no_global_admitted_evidence_level(self):
        # The runner is not the authority on the project's evidence state and
        # must not restate one — least of all a stale one.
        serialized = json.dumps(self.result, ensure_ascii=False)
        self.assertNotIn("admittedAccessibilityEvidenceLevel", serialized)
        self.assertNotIn("Provisional AE-1 candidate", serialized)
        self.assertNotIn("AE-0", serialized)

    def test_run_grants_no_maturity_approval_or_candidate(self):
        effects = self.result["authorityEffects"]
        self.assertIs(effects["maturityGrantedByRun"], False)
        self.assertIs(effects["approvalGrantedByRun"], False)
        self.assertIs(effects["candidateGrantedByRun"], False)

    def test_run_grants_no_admission_claim_conformance_or_human_approval(self):
        effects = self.result["authorityEffects"]
        self.assertIs(effects["evidenceAdmissionGrantedByRun"], False)
        self.assertIs(effects["claimGrantedByRun"], False)
        self.assertIs(effects["conformanceGrantedByRun"], False)
        self.assertIs(effects["humanApprovalGrantedByRun"], False)

    def test_no_authority_effect_is_ever_true(self):
        # Structural: every declared effect is false, in every context.
        for context in runner.SOURCE_AUTHORITY_CONTEXTS:
            effects = execute(
                source_authority_context=context)["authorityEffects"]
            self.assertEqual(len(effects), 7, context)
            for key, value in effects.items():
                self.assertIs(value, False, f"{context}:{key}")

    def test_evidence_produced_is_an_unreviewed_unadmitted_ae1_candidate(self):
        produced = self.result["evidenceProduced"]
        self.assertEqual(produced["evidenceType"],
                         "Structural and Automated Evidence")
        self.assertEqual(produced["evidenceLevelRepresented"], "AE-1")
        self.assertEqual(produced["evidenceClass"], "AE-1 Evidence Candidate")
        self.assertIn("not independently reviewed",
                      produced["independentReviewState"])
        self.assertIn("not admitted", produced["admissionState"])

    def test_execution_context_is_caller_declared_and_bounded(self):
        context = self.result["executionContext"]
        self.assertEqual(context["sourceAuthorityContext"],
                         "authoritative-current")
        self.assertEqual(context["allowedSourceAuthorityContexts"],
                         list(runner.SOURCE_AUTHORITY_CONTEXTS))
        self.assertEqual(runner.SOURCE_AUTHORITY_CONTEXTS,
                         ("authoritative-current", "proposed-candidate"))
        self.assertEqual(context["cdsRevision"], self.result["cdsRevision"])
        self.assertEqual(context["sourceRevision"], self.result["sourceRevision"])
        self.assertTrue(context["statement"].strip())

    def test_an_unbounded_authority_context_is_rejected(self):
        for bad in ("", "current", "candidate", "Proposed Candidate", None):
            with self.assertRaises(ValueError):
                execute(source_authority_context=bad)

    def test_source_revision_mismatch_fails_closed(self):
        payload = execute(source_revision="semantic-status-rev-9999")
        cross_check = payload["sourceRevisionCrossCheck"]
        self.assertIs(cross_check["match"], False)
        self.assertEqual(cross_check["declaredBySource"], CURRENT_SOURCE_REVISION)
        self.assertEqual(cross_check["declaredByArgument"],
                         "semantic-status-rev-9999")
        self.assertEqual(payload["resultStatus"], "Blocked")
        self.assertTrue(payload["executionErrors"])

    def test_the_source_wins_over_the_cli_argument(self):
        # The mismatch is never repaired by trusting the argument.
        payload = execute(source_revision="semantic-status-rev-9999")
        self.assertEqual(payload["sourceDeclaredMetadata"]["sourceRevision"],
                         CURRENT_SOURCE_REVISION)
        boundary = payload["sourceRevisionCrossCheck"]["boundary"].lower()
        self.assertIn("source is authoritative over the argument", boundary)
        self.assertIn("fails closed", boundary)
        # The CLI argument never becomes source authority; the runner says so in
        # the controlled failure itself.
        errors = " ".join(payload["executionErrors"]).lower()
        self.assertIn("never overrides the source", errors)


class ProposedCandidateContextTests(unittest.TestCase):
    """A synthetic Proposed Candidate Revision grants nothing.

    The fixture lives in a temporary directory outside the repository. The real
    Semantic Status source is never mutated and no Candidate revision is created
    in CDS: `semantic-status-rev-0002-candidate` stays a reserved identity.
    """

    @classmethod
    def setUpClass(cls):
        cls.directory = Path(tempfile.mkdtemp(prefix="cds-proposed-candidate-"))
        cls.source = write_proposed_candidate_source(cls.directory)
        cls.result = execute(source_revision=RESERVED_CANDIDATE_REVISION,
                             source_authority_context="proposed-candidate",
                             token_source=cls.source)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.directory, ignore_errors=True)

    def test_the_temporary_fixture_lives_outside_the_repository(self):
        self.assertNotIn(REPO_ROOT, self.source.resolve().parents)

    def test_target_metadata_is_read_from_the_proposed_bytes(self):
        declared = self.result["sourceDeclaredMetadata"]
        self.assertEqual(declared["sourceRevision"], RESERVED_CANDIDATE_REVISION)
        self.assertEqual(declared["maturityState"], "Candidate")
        self.assertEqual(declared["approvalState"], "Approved")
        self.assertIs(declared["declaresCandidateTargetMetadata"], True)
        self.assertIs(self.result["sourceRevisionCrossCheck"]["match"], True)

    def test_proposed_candidate_target_metadata_grants_no_authority(self):
        effects = self.result["authorityEffects"]
        self.assertIs(effects["maturityGrantedByRun"], False)
        self.assertIs(effects["approvalGrantedByRun"], False)
        self.assertIs(effects["candidateGrantedByRun"], False)
        self.assertIs(effects["evidenceAdmissionGrantedByRun"], False)
        self.assertIs(effects["claimGrantedByRun"], False)
        self.assertIs(effects["conformanceGrantedByRun"], False)
        self.assertIs(effects["humanApprovalGrantedByRun"], False)

    def test_target_metadata_is_distinguished_from_current_authority(self):
        context = self.result["executionContext"]
        self.assertEqual(context["sourceAuthorityContext"], "proposed-candidate")
        statement = context["statement"]
        self.assertIn("TARGET METADATA", statement)
        self.assertIn("NOT integrated", statement)
        self.assertIn("does not change repository maturity", statement)
        self.assertIn("does not grant Human-Maintainer", statement)
        self.assertIn("does not grant evidence admission", statement)
        boundary = self.result["sourceDeclaredMetadata"]["boundary"].lower()
        self.assertIn("not a statement of current repository maturity", boundary)

    def test_a_proposed_candidate_run_still_produces_only_an_ae1_candidate(self):
        produced = self.result["evidenceProduced"]
        self.assertEqual(produced["evidenceClass"], "AE-1 Evidence Candidate")
        self.assertIn("not admitted", produced["admissionState"])
        self.assertEqual(self.result["boundaries"]["claims"], "none")
        self.assertEqual(self.result["boundaries"]["conformanceStatement"], "none")

    def test_the_proposed_candidate_run_is_deterministic(self):
        first = json.dumps(
            execute(source_revision=RESERVED_CANDIDATE_REVISION,
                    source_authority_context="proposed-candidate",
                    token_source=self.source), ensure_ascii=False, indent=2)
        second = json.dumps(
            execute(source_revision=RESERVED_CANDIDATE_REVISION,
                    source_authority_context="proposed-candidate",
                    token_source=self.source), ensure_ascii=False, indent=2)
        self.assertEqual(first, second)

    def test_the_proposed_result_carries_no_prohibited_claim_phrase(self):
        lowered = json.dumps(self.result, ensure_ascii=False).lower()
        for phrase in FORBIDDEN_CLAIM_PHRASES:
            self.assertNotIn(phrase, lowered, phrase)

    def test_the_real_source_still_declares_the_experimental_revision(self):
        # The synthetic copy must not have touched the committed source.
        payload = (json_loader.load_path(TOKEN_SOURCE)["$extensions"]
                   [CDS_EXTENSION_ROOT])
        self.assertEqual(payload["sourceRevision"], CURRENT_SOURCE_REVISION)
        self.assertEqual(payload["maturityState"], "Experimental")
        self.assertEqual(payload["approvalState"], "Unapproved")

    def test_no_candidate_revision_artifact_exists_in_the_repository(self):
        for path in (REPO_ROOT / "tokens").rglob("*.json"):
            self.assertNotIn(RESERVED_CANDIDATE_REVISION,
                             path.read_text(encoding="utf-8"), str(path))


class HistoricalEvidenceImmutabilityTests(unittest.TestCase):
    """The format bump must not have rewritten historical evidence."""

    def test_v1_evidence_artifacts_still_declare_result_format_v1(self):
        for path in V1_EVIDENCE_RESULTS:
            self.assertTrue(path.is_file(), str(path))
            payload = json_loader.load_path(path)
            self.assertEqual(
                payload["schemaVersion"],
                "cds-wp016-candidate-accessibility-evidence-result/1", str(path))

    def test_v1_evidence_artifacts_keep_their_original_boundary_fields(self):
        # They recorded the project state as it was understood then. That record
        # is history and is never retrofitted to the v2 vocabulary.
        for path in V1_EVIDENCE_RESULTS:
            boundaries = json_loader.load_path(path)["boundaries"]
            self.assertIn("admittedAccessibilityEvidenceLevel", boundaries,
                          str(path))
            self.assertNotIn("authorityEffects", json_loader.load_path(path),
                             str(path))


class RunnerBoundaryTests(unittest.TestCase):
    """The runner is test tooling: deterministic, offline, CLI-independent."""

    def test_runner_is_not_referenced_by_the_validator_package(self):
        for path in (REPO_ROOT / "tools" / "cds_validator").glob("*.py"):
            self.assertNotIn("semantic_status_candidate_evidence_runner",
                             path.read_text(encoding="utf-8"), path.name)

    def test_runner_performs_no_network_or_git_access(self):
        source = (REPO_ROOT / "tests" / "validator"
                  / "semantic_status_candidate_evidence_runner.py"
                  ).read_text(encoding="utf-8")
        for forbidden in ("import socket", "import urllib", "import requests",
                          "import subprocess", "http://", "https://"):
            self.assertNotIn(forbidden, source, forbidden)

    def test_result_payload_is_deterministic_for_identical_inputs(self):
        first = json.dumps(execute(), ensure_ascii=False, indent=2)
        second = json.dumps(execute(), ensure_ascii=False, indent=2)
        self.assertEqual(first, second)

    def test_worktree_state_is_explicit_and_never_ambient(self):
        self.assertEqual(execute()["worktreeState"], "unknown")
        payload = execute(worktree_state="modified worktree")
        self.assertEqual(payload["worktreeState"], "modified worktree")
        self.assertEqual(payload["executionContext"]["worktreeState"],
                         "modified worktree")

    def test_runner_performs_no_ambient_repository_discovery(self):
        # The runner takes every path as an explicit argument. It must never
        # locate the repository, the working directory, or the environment.
        source = RUNNER_SOURCE.read_text(encoding="utf-8")
        for forbidden in ("import os", "os.getcwd", "os.environ", "__file__",
                          "parents[", ".git"):
            self.assertNotIn(forbidden, source, forbidden)
        self.assertIs(
            execute()["executionContext"]["derivedFromAmbientGitState"], False)

    def test_runner_writes_only_to_its_explicit_output_path(self):
        source = RUNNER_SOURCE.read_text(encoding="utf-8")
        self.assertEqual(source.count("open("), 1)
        self.assertIn(
            'with open(args.output, "w", encoding="utf-8", newline="\\n")', source)


class RuleUnitTests(unittest.TestCase):
    """Each transcribed rule fires on its own trigger and not otherwise."""

    def statement(self, **overrides):
        base = {
            "subjectIdentity": "synthetic", "declaredScope": "synthetic",
            "axes": {"condition": "nominal", "severity": "none",
                     "confidence": "supported", "freshness": "current",
                     "evidence": "available"},
            "observedOrAssessedTime": "T", "sourceOrEvidenceIdentity": "E",
            "sourceOrEvidenceResolvable": True, "rationale": None,
            "summary": {"positive": False, "qualifiersCarried": []},
            "representation": {}, "remapping": None,
        }
        axes = overrides.pop("axes", None)
        if axes:
            base["axes"] = {**base["axes"], **axes}
        base.update(overrides)
        return base

    def test_baseline_statement_triggers_nothing(self):
        self.assertEqual(runner.evaluate(self.statement()), ([], []))

    def test_each_review_required_rule_fires(self):
        expectations = (
            ("RR-1", self.statement(axes={"severity": "major"})),
            ("RR-2", self.statement(axes={"confidence": "verified",
                                          "evidence": "unavailable"})),
            ("RR-3", self.statement(observedOrAssessedTime=None)),
            ("RR-5", self.statement(axes={"condition": "unavailable"})),
            ("RR-6", self.statement(
                axes={"confidence": "unknown"},
                summary={"positive": True, "qualifiersCarried": []})),
        )
        for expected, statement in expectations:
            _, review_required = runner.evaluate(statement)
            self.assertIn(expected, review_required, expected)

    def test_rr4_and_fc6_fire_together(self):
        fail_closed, review_required = runner.evaluate(
            self.statement(axes={"evidence": "not-applicable"}))
        self.assertIn("RR-4", review_required)
        self.assertIn("FC-6", fail_closed)

    def test_each_fail_closed_rule_fires(self):
        missing = self.statement()
        del missing["axes"]["condition"]
        expectations = (
            ("FC-1", missing),
            ("FC-2", self.statement(axes={"severity": "fine"})),
            ("FC-3", self.statement(axes={"condition": "unknown"},
                                    representation={"condition": "nominal"})),
            ("FC-4", self.statement(axes={"freshness": "stale"},
                                    representation={"freshness": "current"})),
            ("FC-5", self.statement(axes={"confidence": "unverified"},
                                    representation={"confidence": "verified"})),
            ("FC-7", self.statement(sourceOrEvidenceResolvable=False)),
            ("FC-8", self.statement(
                remapping={"kind": "product-profile",
                           "preservesAxisMeaning": False, "detail": "synthetic"})),
        )
        for expected, statement in expectations:
            fail_closed, _ = runner.evaluate(statement)
            self.assertIn(expected, fail_closed, expected)

    def test_rr6_does_not_fire_when_the_qualifier_is_carried(self):
        _, review_required = runner.evaluate(self.statement(
            axes={"confidence": "unknown"},
            summary={"positive": True, "qualifiersCarried": ["confidence"]}))
        self.assertNotIn("RR-6", review_required)

    def test_expired_as_current_also_fails_closed(self):
        fail_closed, _ = runner.evaluate(self.statement(
            axes={"freshness": "expired"}, representation={"freshness": "current"}))
        self.assertIn("FC-4", fail_closed)

    def test_unresolvable_identity_only_matters_where_values_require_it(self):
        fail_closed, _ = runner.evaluate(self.statement(
            axes={"confidence": "unverified", "evidence": "partial"},
            sourceOrEvidenceResolvable=False))
        self.assertNotIn("FC-7", fail_closed)


if __name__ == "__main__":
    unittest.main()
