"""Unit tests for the machine-readable result report contract (DEC-S-101)."""

import unittest
from pathlib import Path

from tools.cds_validator import reporting
from tools.cds_validator.schema_registry import SchemaRegistry

REPO_ROOT = Path(__file__).resolve().parents[2]


def sample_case():
    return {
        "caseId": "VAL-CASE-001",
        "fixturePaths": ["tests/fixtures/machine-readable/positive/reference-set.tokens.json"],
        "classification": "positive",
        "expected": {"V1": "Pass", "V2": "Pass", "V3": "Pass",
                     "V4": "Not applicable with rationale"},
        "actual": {"V1": "Pass", "V2": "Pass", "V3": "Pass",
                   "V4": "Not applicable with rationale"},
        "expectedMatch": True,
        "blockingLayer": "none",
        "diagnostics": [],
        "contentDigests": {},
        "sourceRevisions": {},
        "executionStatus": "executed",
    }


class ReportingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = SchemaRegistry(REPO_ROOT)

    def build(self, cases):
        return reporting.build_report(
            REPO_ROOT, cases, reporting.utc_now(), ["test limitation"])

    def test_report_validates_against_the_result_schema(self):
        report = self.build([sample_case()])
        self.assertEqual(
            self.registry.iter_errors("validation-result", report), [])

    def test_independent_review_state_is_pending(self):
        report = self.build([sample_case()])
        self.assertEqual(report["independentReviewState"], "pending")

    def test_summary_counts_matches_and_errors(self):
        mismatch = sample_case()
        mismatch["caseId"] = "VAL-CASE-002"
        mismatch["expectedMatch"] = False
        broken = sample_case()
        broken["caseId"] = "VAL-CASE-003"
        broken["expectedMatch"] = False
        broken["executionStatus"] = "internal-error: boom"
        report = self.build([sample_case(), mismatch, broken])
        self.assertEqual(report["summary"]["totalCases"], 3)
        self.assertEqual(report["summary"]["expectedMatches"], 1)
        self.assertEqual(report["summary"]["expectedMismatches"], 1)
        self.assertEqual(report["summary"]["executionErrors"], 1)

    def test_summary_has_no_aggregate_score(self):
        report = self.build([sample_case()])
        for forbidden in ("score", "qualityScore", "grade", "percentage"):
            self.assertNotIn(forbidden, report["summary"])

    def test_worktree_state_is_reported_honestly(self):
        report = self.build([sample_case()])
        self.assertIn(report["worktreeState"],
                      ("clean", "modified worktree", "unknown"))

    def test_offline_mode_and_schema_ids_bound(self):
        report = self.build([sample_case()])
        self.assertTrue(report["offlineMode"])
        self.assertEqual(len(report["schemaIds"]), 5)

    def test_dependency_versions_are_exact(self):
        report = self.build([sample_case()])
        for name, version in report["dependencyVersions"].items():
            self.assertNotEqual(version, "latest", name)


if __name__ == "__main__":
    unittest.main()
