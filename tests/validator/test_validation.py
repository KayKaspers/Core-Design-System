"""Unit tests for the layered V1–V4 validation engine against the fixtures."""

import unittest
from pathlib import Path

from tools.cds_validator.models import ResultState
from tools.cds_validator.schema_registry import SchemaRegistry
from tools.cds_validator.validation import ValidationEngine

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "machine-readable"


class ValidationEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = ValidationEngine(REPO_ROOT, SchemaRegistry(REPO_ROOT))

    def scope(self, *relative_paths):
        return self.engine.validate_scope(
            [FIXTURES / rel for rel in relative_paths])

    def categories(self, result):
        return {d.category for d in result.outcome.diagnostics
                if d.severity == "error"}

    def test_positive_reference_set_passes_v1_to_v3(self):
        result = self.scope("positive/reference-set.tokens.json")
        self.assertEqual(result.outcome.as_dict(), {
            "V1": "Pass", "V2": "Pass", "V3": "Pass",
            "V4": "Not applicable with rationale"})

    def test_positive_full_composition_passes(self):
        result = self.scope(
            "positive/reference-set.tokens.json",
            "positive/semantic-set.tokens.json",
            "positive/component-set.tokens.json",
            "positive/product-profile-set.tokens.json",
            "positive/source-set-manifest.source-set.json",
            "positive/resolver.resolver.json")
        self.assertEqual(result.outcome.as_dict(), {
            "V1": "Pass", "V2": "Pass", "V3": "Pass",
            "V4": "Not applicable with rationale"})
        self.assertEqual(self.categories(result), set())

    def test_manifest_v2_is_not_applicable(self):
        result = self.scope("positive/source-set-manifest.source-set.json")
        self.assertEqual(result.outcome.v2, ResultState.NOT_APPLICABLE)

    def test_duplicate_key_fails_v1_and_blocks(self):
        result = self.scope("negative/duplicate-key.tokens.json")
        self.assertEqual(result.outcome.as_dict(), {
            "V1": "Fail", "V2": "Not assessed", "V3": "Not assessed",
            "V4": "Not assessed"})
        self.assertIn("duplicate-key", self.categories(result))
        self.assertEqual(result.outcome.blocking_layer(), "V1")

    def test_dangling_reference_fails_v2(self):
        result = self.scope("negative/dangling-reference.tokens.json")
        self.assertEqual(result.outcome.v2, ResultState.FAIL)
        self.assertIn("dangling-reference", self.categories(result))
        self.assertEqual(result.outcome.v3, ResultState.NOT_ASSESSED)

    def test_cross_file_cycle_fails_v2(self):
        result = self.scope("negative/circular-reference-a.tokens.json",
                            "negative/circular-reference-b.tokens.json")
        self.assertEqual(result.outcome.v2, ResultState.FAIL)
        self.assertIn("reference-cycle", self.categories(result))

    def test_type_mismatch_fails_v2(self):
        result = self.scope("negative/type-mismatch.tokens.json")
        self.assertEqual(result.outcome.v2, ResultState.FAIL)
        self.assertIn("type-mismatch", self.categories(result))

    def test_backward_layer_manifest_fails_v3(self):
        result = self.scope("negative/backward-layer-dependency.source-set.json")
        self.assertEqual(result.outcome.v2, ResultState.NOT_APPLICABLE)
        self.assertEqual(result.outcome.v3, ResultState.FAIL)
        self.assertIn("backward-layer-dependency", self.categories(result))

    def test_undeclared_cross_file_reference_fails_v3_not_v2(self):
        result = self.scope("negative/undeclared-cross-file-reference.tokens.json")
        self.assertEqual(result.outcome.v2, ResultState.PASS)
        self.assertEqual(result.outcome.v3, ResultState.FAIL)
        self.assertIn("undeclared-cross-file-reference", self.categories(result))

    def test_invalid_extension_fails_v3(self):
        result = self.scope("negative/invalid-extension.tokens.json")
        self.assertEqual(result.outcome.v3, ResultState.FAIL)
        self.assertIn("invalid-extension", self.categories(result))

    def test_preview_feature_fails_v2(self):
        result = self.scope("negative/preview-feature.tokens.json")
        self.assertEqual(result.outcome.v2, ResultState.FAIL)
        self.assertIn("preview-feature", self.categories(result))

    def test_unknown_extension_fails_v1_file_identity(self):
        result = self.engine.validate_scope(
            [REPO_ROOT / "tests" / "fixtures" / "machine-readable"
             / "VALIDATION_CASES.json"])
        self.assertEqual(result.outcome.v1, ResultState.FAIL)
        self.assertIn(
            "invalid-file-identity",
            {d.category for d in result.outcome.diagnostics})

    def test_no_aggregate_score_exists(self):
        result = self.scope("positive/reference-set.tokens.json")
        self.assertFalse(hasattr(result.outcome, "score"))


if __name__ == "__main__":
    unittest.main()
