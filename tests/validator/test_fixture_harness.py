"""Unit tests for the full fixture harness (DEC-S-102).

Runs all committed validation cases and asserts that every actual layered
outcome matches the committed expected outcome. Expected failure of a
negative fixture is a successful harness observation, not a passing token
artifact.
"""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from tools.cds_validator import cli, json_loader
from tools.cds_validator.schema_registry import SchemaRegistry

REPO_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = REPO_ROOT / "tests" / "fixtures" / "machine-readable" / "VALIDATION_CASES.json"


class FixtureHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        report_path = Path(cls.tmp.name) / "results.json"
        digest_path = Path(cls.tmp.name) / "digests.json"
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            cls.exit_code = cli.main([
                "--repository-root", str(REPO_ROOT), "validate-cases",
                str(CASES_PATH), "--report", str(report_path),
                "--digests", str(digest_path)])
        cls.report = json_loader.load_path(report_path)
        cls.digests = json_loader.load_path(digest_path)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exit_code_zero_when_all_expected_match(self):
        self.assertEqual(self.exit_code, cli.EXIT_OK)

    def test_all_twenty_four_cases_executed(self):
        self.assertEqual(self.report["summary"]["totalCases"], 24)
        self.assertEqual(
            [case["caseId"] for case in self.report["cases"]],
            [f"VAL-CASE-{n:03d}" for n in range(1, 25)])

    def test_all_expected_results_match_actual_results(self):
        for case in self.report["cases"]:
            self.assertTrue(case["expectedMatch"], case["caseId"])
            self.assertEqual(case["actual"], case["expected"], case["caseId"])
        self.assertEqual(self.report["summary"]["expectedMatches"], 24)
        self.assertEqual(self.report["summary"]["expectedMismatches"], 0)
        self.assertEqual(self.report["summary"]["executionErrors"], 0)

    def test_original_fifteen_cases_keep_their_baseline_outcomes(self):
        # The committed WP-013 baseline expectations are immutable (DEC-S-120).
        for case in self.report["cases"][:15]:
            self.assertTrue(case["expectedMatch"], case["caseId"])
        duplicate = next(c for c in self.report["cases"]
                         if c["caseId"] == "VAL-CASE-008")
        self.assertEqual(duplicate["blockingLayer"], "V1")

    def test_new_status_cases_block_at_v4_with_status_categories(self):
        expectations = {
            "VAL-CASE-017": "semantic-status-axis",
            "VAL-CASE-018": "semantic-status-unknown",
            "VAL-CASE-019": "semantic-status-axis",
            "VAL-CASE-020": "semantic-status-value",
            "VAL-CASE-021": "semantic-status-path-value",
            "VAL-CASE-022": "semantic-status-aggregate",
            "VAL-CASE-023": "semantic-status-visual-leakage",
            "VAL-CASE-024": "semantic-status-collision",
        }
        for case_id, category in expectations.items():
            case = next(c for c in self.report["cases"] if c["caseId"] == case_id)
            self.assertEqual(case["blockingLayer"], "V4", case_id)
            self.assertIn(category,
                          {d["category"] for d in case["diagnostics"]}, case_id)
        positive = next(c for c in self.report["cases"]
                        if c["caseId"] == "VAL-CASE-016")
        self.assertEqual(positive["actual"]["V4"], "Pass")

    def test_report_validates_against_result_schema(self):
        registry = SchemaRegistry(REPO_ROOT)
        self.assertEqual(
            registry.iter_errors("validation-result", self.report), [])

    def test_duplicate_key_case_blocked_at_v1_without_digest(self):
        case = next(c for c in self.report["cases"]
                    if c["caseId"] == "VAL-CASE-008")
        self.assertEqual(case["blockingLayer"], "V1")
        self.assertEqual(case["contentDigests"], {})
        self.assertIn(
            "tests/fixtures/machine-readable/negative/duplicate-key.tokens.json",
            self.digests["undigestible"])

    def test_cycle_manifest_and_preview_cases_recognized(self):
        expectations = {
            "VAL-CASE-010": ("V2", "reference-cycle"),
            "VAL-CASE-011": ("V3", "backward-layer-dependency"),
            "VAL-CASE-015": ("V2", "preview-feature"),
        }
        for case_id, (layer, category) in expectations.items():
            case = next(c for c in self.report["cases"] if c["caseId"] == case_id)
            self.assertEqual(case["blockingLayer"], layer, case_id)
            categories = {d["category"] for d in case["diagnostics"]}
            self.assertIn(category, categories, case_id)

    def test_twenty_three_parsable_fixtures_received_digests(self):
        # 14 machine-readable (duplicate-key excluded) + 9 semantic-status.
        self.assertEqual(len(self.digests["digests"]), 23)
        for digest in self.digests["digests"].values():
            self.assertRegex(digest, r"^sha256:[0-9a-f]{64}$")

    def test_report_is_executor_produced_and_unreviewed(self):
        self.assertEqual(self.report["independentReviewState"], "pending")
        self.assertIn("executor-produced",
                      self.report["executionIdentity"]["evidenceClass"])


if __name__ == "__main__":
    unittest.main()
