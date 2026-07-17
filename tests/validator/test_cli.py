"""Unit tests for the CLI commands and their exit-code contract (DEC-S-094)."""

import contextlib
import io
import json
import unittest
from pathlib import Path

from tools.cds_validator import cli

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "machine-readable"


def run_cli(*argv):
    stdout, stderr = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        code = cli.main(list(argv))
    return code, stdout.getvalue(), stderr.getvalue()


class CliTests(unittest.TestCase):
    def test_version_exits_zero_and_reports_identities(self):
        code, out, _ = run_cli("--repository-root", str(REPO_ROOT), "version")
        self.assertEqual(code, cli.EXIT_OK)
        payload = json.loads(out)
        self.assertEqual(payload["cdsProfileVersion"], "1")
        self.assertEqual(payload["dtcgReportVersion"], "2025.10")
        self.assertEqual(len(payload["schemaIds"]), 5)
        self.assertIn("jsonschema", payload["dependencyVersions"])
        self.assertIn("rfc8785", payload["dependencyVersions"])

    def test_validate_file_positive_exits_zero(self):
        code, out, _ = run_cli(
            "--repository-root", str(REPO_ROOT), "validate-file",
            str(FIXTURES / "positive" / "reference-set.tokens.json"))
        self.assertEqual(code, cli.EXIT_OK)
        payload = json.loads(out)
        self.assertEqual(payload["results"]["V1"], "Pass")

    def test_validate_file_negative_exits_one(self):
        code, out, _ = run_cli(
            "--repository-root", str(REPO_ROOT), "validate-file",
            str(FIXTURES / "negative" / "dangling-reference.tokens.json"))
        self.assertEqual(code, cli.EXIT_FAIL)
        payload = json.loads(out)
        self.assertEqual(payload["results"]["V2"], "Fail")

    def test_validate_file_duplicate_key_exits_one_blocking_v1(self):
        code, out, _ = run_cli(
            "--repository-root", str(REPO_ROOT), "validate-file",
            str(FIXTURES / "negative" / "duplicate-key.tokens.json"))
        self.assertEqual(code, cli.EXIT_FAIL)
        payload = json.loads(out)
        self.assertEqual(payload["blockingLayer"], "V1")

    def test_digest_positive_fixture_exits_zero(self):
        code, out, _ = run_cli(
            "--repository-root", str(REPO_ROOT), "digest",
            str(FIXTURES / "positive" / "reference-set.tokens.json"))
        self.assertEqual(code, cli.EXIT_OK)
        self.assertRegex(out.strip(), r"^sha256:[0-9a-f]{64}$")

    def test_digest_duplicate_key_exits_one_without_digest(self):
        code, out, err = run_cli(
            "--repository-root", str(REPO_ROOT), "digest",
            str(FIXTURES / "negative" / "duplicate-key.tokens.json"))
        self.assertEqual(code, cli.EXIT_FAIL)
        self.assertNotIn("sha256:", out)
        self.assertIn("no digest", err)

    def test_missing_input_is_blocked_not_a_crash(self):
        code, _, err = run_cli(
            "--repository-root", str(REPO_ROOT), "validate-cases",
            str(FIXTURES / "no-such-file.json"))
        self.assertEqual(code, cli.EXIT_BLOCKED)
        self.assertIn("BLOCKED", err)


if __name__ == "__main__":
    unittest.main()
