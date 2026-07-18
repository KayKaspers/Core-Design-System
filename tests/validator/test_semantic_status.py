"""Unit tests for the CDS-WP-015 semantic-status validation and the
Nova-authorized additive validation-case schema correction."""

import re
import unittest
from pathlib import Path

from tools.cds_validator import json_loader, semantic_status
from tools.cds_validator.models import DocumentKind, ResultState
from tools.cds_validator.schema_registry import SchemaRegistry
from tools.cds_validator.validation import ScopeDocument, ValidationEngine

REPO_ROOT = Path(__file__).resolve().parents[2]
STATUS_FIX = REPO_ROOT / "tests" / "fixtures" / "semantic-status"
SOURCE_DIR = REPO_ROOT / "tokens" / "semantic" / "status"

NEW_CATEGORIES = [
    "semantic-status-axis", "semantic-status-value", "semantic-status-unknown",
    "semantic-status-count", "semantic-status-path-value",
    "semantic-status-collision", "semantic-status-aggregate",
    "semantic-status-visual-leakage", "semantic-status-identity",
]


def case_probe(fixture_path, category="none"):
    return {
        "caseSetVersion": "1", "profileVersion": "1",
        "cases": [{
            "caseId": "VAL-CASE-016", "title": "probe",
            "fixturePaths": [fixture_path],
            "classification": "positive", "primaryFailureReason": "none",
            "expectedV1": "Pass", "expectedV2": "Pass",
            "expectedV3": "Pass", "expectedV4": "Pass",
            "blockingLayer": "none",
            "expectedDiagnosticCategory": category,
            "applicableDecisionIds": [], "applicableRiskIds": [],
            "notes": "probe",
        }],
    }


class CaseSchemaCorrectionTests(unittest.TestCase):
    """Targeted regression tests for the additive schema correction."""

    @classmethod
    def setUpClass(cls):
        cls.registry = SchemaRegistry(REPO_ROOT)  # runs check_schema (test 10)

    def valid(self, doc):
        return self.registry.iter_errors("validation-case", doc) == []

    def test_committed_case_matrix_validates_including_new_cases(self):
        doc = json_loader.load_path(
            REPO_ROOT / "tests" / "fixtures" / "machine-readable"
            / "VALIDATION_CASES.json")
        self.assertTrue(self.valid(doc))
        self.assertEqual(len(doc["cases"]), 24)

    def test_machine_readable_paths_still_validate(self):
        for path in (
                "tests/fixtures/machine-readable/positive/reference-set.tokens.json",
                "tests/fixtures/machine-readable/negative/backward-layer-dependency.source-set.json",
                "tests/fixtures/machine-readable/positive/resolver.resolver.json"):
            self.assertTrue(self.valid(case_probe(path)), path)

    def test_semantic_status_token_paths_validate(self):
        for path in (
                "tests/fixtures/semantic-status/positive/semantic-status-valid.tokens.json",
                "tests/fixtures/semantic-status/negative/missing-axis.tokens.json"):
            self.assertTrue(self.valid(case_probe(path)), path)

    def test_unauthorized_fixture_root_rejected(self):
        self.assertFalse(self.valid(case_probe(
            "tests/fixtures/other-root/positive/x.tokens.json")))

    def test_semantic_status_source_set_and_resolver_paths_rejected(self):
        for path in (
                "tests/fixtures/semantic-status/negative/x.source-set.json",
                "tests/fixtures/semantic-status/negative/x.resolver.json"):
            self.assertFalse(self.valid(case_probe(path)), path)

    def test_backslashes_rejected(self):
        path = "tests" + chr(92) + "fixtures" + chr(92) + "semantic-status" + \
            chr(92) + "positive" + chr(92) + "x.tokens.json"
        self.assertFalse(self.valid(case_probe(path)))

    def test_path_escape_rejected(self):
        self.assertFalse(self.valid(case_probe(
            "tests/fixtures/semantic-status/positive/../x.tokens.json")))

    def test_all_nine_new_categories_accepted(self):
        good = "tests/fixtures/semantic-status/negative/missing-axis.tokens.json"
        for category in NEW_CATEGORIES:
            self.assertTrue(self.valid(case_probe(good, category)), category)

    def test_unknown_category_still_rejected(self):
        good = "tests/fixtures/semantic-status/negative/missing-axis.tokens.json"
        self.assertFalse(self.valid(case_probe(good, "semantic-status-nonsense")))

    def test_schema_identity_unchanged(self):
        schema = self.registry.schema("validation-case")
        self.assertEqual(
            schema["$id"],
            "tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-validation-case/1")
        self.assertEqual(
            schema["$schema"], "https://json-schema.org/draft/2020-12/schema")


class SemanticStatusEngineTests(unittest.TestCase):
    """The status-specific V4 rules run through the full engine."""

    @classmethod
    def setUpClass(cls):
        cls.engine = ValidationEngine(REPO_ROOT, SchemaRegistry(REPO_ROOT))

    def scope(self, *paths):
        return self.engine.validate_scope([Path(p) for p in paths])

    def categories(self, result):
        return {d.category for d in result.outcome.diagnostics
                if d.severity == "error"}

    def assert_v4_fail(self, fixture, category):
        result = self.scope(STATUS_FIX / "negative" / fixture)
        self.assertEqual(result.outcome.as_dict()["V4"], "Fail", fixture)
        self.assertEqual(result.outcome.blocking_layer(), "V4", fixture)
        self.assertIn(category, self.categories(result), fixture)

    def test_valid_vocabulary_passes_v4_despite_fixture_flags(self):
        result = self.scope(STATUS_FIX / "positive" / "semantic-status-valid.tokens.json")
        self.assertEqual(result.outcome.as_dict(), {
            "V1": "Pass", "V2": "Pass", "V3": "Pass", "V4": "Pass"})
        self.assertEqual(self.categories(result), set())

    def test_generic_v4_limits_stay_visible_for_status_docs(self):
        result = self.scope(STATUS_FIX / "positive" / "semantic-status-valid.tokens.json")
        infos = [d for d in result.outcome.diagnostics
                 if d.code == "CDS-V4-NOT-ASSESSED"]
        self.assertTrue(infos, "non-objective V4 residue must stay visible")

    def test_missing_axis_fails(self):
        self.assert_v4_fail("missing-axis.tokens.json", "semantic-status-axis")

    def test_missing_unknown_fails(self):
        self.assert_v4_fail("missing-unknown.tokens.json", "semantic-status-unknown")

    def test_extra_axis_fails(self):
        self.assert_v4_fail("extra-axis.tokens.json", "semantic-status-axis")

    def test_extra_value_fails(self):
        self.assert_v4_fail("extra-value.tokens.json", "semantic-status-value")

    def test_path_value_mismatch_fails(self):
        self.assert_v4_fail("path-value-mismatch.tokens.json",
                            "semantic-status-path-value")

    def test_case_only_value_collision_fails(self):
        self.assert_v4_fail("case-collision.tokens.json", "semantic-status-collision")

    def test_aggregate_status_fails(self):
        self.assert_v4_fail("aggregate-status.tokens.json", "semantic-status-aggregate")

    def test_visual_role_leakage_fails(self):
        self.assert_v4_fail("visual-role-leakage.tokens.json",
                            "semantic-status-visual-leakage")

    def test_token_count_check_fires(self):
        result = self.scope(STATUS_FIX / "negative" / "missing-axis.tokens.json")
        self.assertIn("semantic-status-count", self.categories(result))

    def test_real_source_set_scope_passes_and_never_fails(self):
        result = self.scope(
            SOURCE_DIR / "semantic-status.tokens.json",
            SOURCE_DIR / "semantic-status.source-set.json",
            SOURCE_DIR / "semantic-status.resolver.json")
        states = result.outcome.as_dict()
        self.assertEqual(states["V1"], "Pass")
        self.assertEqual(states["V2"], "Pass")
        self.assertEqual(states["V3"], "Pass")
        self.assertNotIn(states["V4"], ("Fail", "Blocked"))
        self.assertEqual(self.categories(result), set())


class SemanticStatusCheckerDirectTests(unittest.TestCase):
    """Direct checker tests for rules the harness cannot reach (schema blocks
    uppercase keys at V3) and for identity/candidate boundaries."""

    def doc_for(self, content, path="synthetic.tokens.json"):
        return ScopeDocument(path=Path(path), kind=DocumentKind.TOKEN_DOCUMENT,
                             v1=ResultState.PASS, content=content)

    def build(self, status, payload_extra=None):
        payload = {"profileVersion": "1", "sourceSetId": "fixture/direct",
                   "layer": "semantic", "dtcgReportVersion": "2025.10",
                   "sourceRevision": "fixture-rev-0001-synthetic",
                   "testOnly": True, "nonNormative": True}
        payload.update(payload_extra or {})
        return {"$extensions": {"io.github.kaykaspers.cds": payload},
                "status": status}

    def full_status(self):
        return {axis: {v: {"$type": "string", "$value": v}
                       for v in values}
                for axis, values in semantic_status.AUTHORIZED_AXES.items()}

    def test_is_status_vocabulary_detection(self):
        self.assertTrue(semantic_status.is_status_vocabulary(
            self.build(self.full_status())))
        self.assertFalse(semantic_status.is_status_vocabulary(
            {"test-primitive": {"alpha": {"$type": "number", "$value": 0}}}))

    def test_key_level_case_collision_detected_directly(self):
        status = self.full_status()
        status["Condition"] = {"nominal": {"$type": "string", "$value": "nominal"}}
        doc = self.doc_for(self.build(status))
        found = semantic_status.check_status_document(doc)
        self.assertIn("CDS-V4-STATUS-COLLISION", {d.code for d in found})

    def test_candidate_maturity_statement_rejected(self):
        doc = self.doc_for(self.build(
            self.full_status(), {"maturityState": "Candidate"}))
        found = semantic_status.check_status_document(doc)
        self.assertIn("CDS-V4-STATUS-IDENTITY", {d.code for d in found})

    def test_approved_state_statement_rejected(self):
        doc = self.doc_for(self.build(
            self.full_status(), {"approvalState": "Approved"}))
        found = semantic_status.check_status_document(doc)
        self.assertIn("CDS-V4-STATUS-IDENTITY", {d.code for d in found})

    def test_manifest_identity_mismatch_detected(self):
        doc = self.doc_for(self.build(self.full_status(),
                                      {"sourceSetId": "semantic/status"}))
        manifest = {"sourceSets": [{
            "sourceSetId": "semantic/status", "layer": "semantic",
            "sourceRevision": "some-other-revision",
            "expectedProfileVersion": "1", "expectedDtcgVersion": "2025.10"}]}
        found = semantic_status.check_status_document(doc, manifest)
        self.assertIn("CDS-V4-STATUS-IDENTITY", {d.code for d in found})

    def test_manifest_identity_agreement_passes(self):
        doc = self.doc_for(self.build(self.full_status(),
                                      {"sourceSetId": "semantic/status"}))
        manifest = {"sourceSets": [{
            "sourceSetId": "semantic/status", "layer": "semantic",
            "sourceRevision": "fixture-rev-0001-synthetic",
            "expectedProfileVersion": "1", "expectedDtcgVersion": "2025.10"}]}
        found = semantic_status.check_status_document(doc, manifest)
        self.assertEqual([d.code for d in found], [])

    def test_authorized_vocabulary_constants(self):
        self.assertEqual(len(semantic_status.AUTHORIZED_AXES), 5)
        for axis, values in semantic_status.AUTHORIZED_AXES.items():
            self.assertEqual(len(values), 5, axis)
            self.assertIn("unknown", values, axis)
        self.assertEqual(semantic_status.EXPECTED_TOKEN_COUNT, 25)

    def test_real_source_matches_vocabulary_one_to_one(self):
        content = json_loader.load_path(SOURCE_DIR / "semantic-status.tokens.json")
        status = content["status"]
        axes = {k for k in status if not k.startswith("$")}
        self.assertEqual(axes, set(semantic_status.AUTHORIZED_AXES))
        for axis, values in semantic_status.AUTHORIZED_AXES.items():
            names = {k for k in status[axis] if not k.startswith("$")}
            self.assertEqual(names, set(values), axis)
            for name in values:
                self.assertEqual(status[axis][name]["$value"], name)
                self.assertEqual(status[axis][name]["$type"], "string")


if __name__ == "__main__":
    unittest.main()
