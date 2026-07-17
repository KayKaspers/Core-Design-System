"""Unit tests for the controlled duplicate-key-rejecting JSON loader."""

import tempfile
import unittest
from pathlib import Path

from tools.cds_validator import json_loader

REPO_ROOT = Path(__file__).resolve().parents[2]
NEGATIVE = REPO_ROOT / "tests" / "fixtures" / "machine-readable" / "negative"


class JsonLoaderTests(unittest.TestCase):
    def test_normal_parse(self):
        content = json_loader.parse_text('{"a": 1, "b": {"c": [1, 2]}}', "inline")
        self.assertEqual(content["b"]["c"], [1, 2])

    def test_duplicate_key_rejected_at_top_level(self):
        with self.assertRaises(json_loader.DuplicateKeyError) as ctx:
            json_loader.parse_text('{"a": 1, "a": 2}', "inline")
        self.assertEqual(ctx.exception.key, "a")

    def test_duplicate_key_rejected_when_nested(self):
        with self.assertRaises(json_loader.DuplicateKeyError):
            json_loader.parse_text('{"outer": {"x": 1, "x": 2}}', "inline")

    def test_no_first_or_last_key_wins(self):
        # The loader must raise, never silently keep either value.
        try:
            json_loader.parse_text('{"k": "first", "k": "last"}', "inline")
        except json_loader.DuplicateKeyError:
            return
        self.fail("duplicate keys were silently accepted")

    def test_invalid_json_raises_parse_error(self):
        with self.assertRaises(json_loader.JsonParseError):
            json_loader.parse_text('{"a": 1,}', "inline")

    def test_non_utf8_file_raises_encoding_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "latin1.tokens.json"
            path.write_bytes('{"a": "ä"}'.encode("latin-1"))
            with self.assertRaises(json_loader.EncodingError):
                json_loader.load_path(path)

    def test_duplicate_key_fixture_fails_the_controlled_load(self):
        with self.assertRaises(json_loader.DuplicateKeyError) as ctx:
            json_loader.load_path(NEGATIVE / "duplicate-key.tokens.json")
        self.assertEqual(ctx.exception.key, "alpha")

    def test_missing_file_raises_loader_error(self):
        with self.assertRaises(json_loader.LoaderError):
            json_loader.load_path(NEGATIVE / "does-not-exist.tokens.json")


if __name__ == "__main__":
    unittest.main()
