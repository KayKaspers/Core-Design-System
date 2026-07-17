"""Unit tests for RFC 8785 canonicalization and SHA-256 digests (ADR-0002)."""

import re
import unittest
from pathlib import Path

from tools.cds_validator import json_loader
from tools.cds_validator.canonicalization import (
    DigestError,
    content_digest,
    digest_file,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
NEGATIVE = REPO_ROOT / "tests" / "fixtures" / "machine-readable" / "negative"

DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


class CanonicalizationInvarianceTests(unittest.TestCase):
    def test_indentation_does_not_change_the_digest(self):
        compact = json_loader.parse_text('{"a":1,"b":[1,2]}', "inline")
        indented = json_loader.parse_text(
            '{\n  "a": 1,\n  "b": [\n    1,\n    2\n  ]\n}', "inline")
        self.assertEqual(content_digest(compact), content_digest(indented))

    def test_key_order_does_not_change_the_digest(self):
        one = json_loader.parse_text('{"a": 1, "b": 2}', "inline")
        two = json_loader.parse_text('{"b": 2, "a": 1}', "inline")
        self.assertEqual(content_digest(one), content_digest(two))

    def test_changed_logical_value_changes_the_digest(self):
        one = json_loader.parse_text('{"a": 1}', "inline")
        two = json_loader.parse_text('{"a": 2}', "inline")
        self.assertNotEqual(content_digest(one), content_digest(two))

    def test_duplicate_key_input_gets_no_digest(self):
        with self.assertRaises(json_loader.DuplicateKeyError):
            digest_file(NEGATIVE / "duplicate-key.tokens.json")

    def test_unsupported_canonicalization_input_fails_controlled(self):
        with self.assertRaises(DigestError):
            content_digest(float("nan"))
        with self.assertRaises(DigestError):
            content_digest({"x": object()})


class DigestFormatTests(unittest.TestCase):
    def test_digest_format_is_prefixed_lowercase_hex(self):
        digest = content_digest({"a": 1})
        self.assertTrue(DIGEST_RE.match(digest), digest)

    def test_known_rfc8785_vector(self):
        # RFC 8785 canonicalizes {"b":2,"a":1} to {"a":1,"b":2}; the digest of
        # both spellings must therefore equal the digest of the sorted form.
        import hashlib
        expected = "sha256:" + hashlib.sha256(b'{"a":1,"b":2}').hexdigest()
        self.assertEqual(content_digest({"b": 2, "a": 1}), expected)

    def test_fixture_digest_is_deterministic(self):
        path = (REPO_ROOT / "tests" / "fixtures" / "machine-readable"
                / "positive" / "reference-set.tokens.json")
        self.assertEqual(digest_file(path), digest_file(path))


if __name__ == "__main__":
    unittest.main()
