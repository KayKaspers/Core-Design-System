"""Unit tests for the local, offline schema registry (DEC-S-096)."""

import unittest
from pathlib import Path

from tools.cds_validator import json_loader
from tools.cds_validator.schema_registry import (
    SCHEMA_FILES,
    SchemaRegistry,
    UnknownSchemaError,
)
from tools.cds_validator.version import SCHEMA_IDS

REPO_ROOT = Path(__file__).resolve().parents[2]


class SchemaRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = SchemaRegistry(REPO_ROOT)

    def test_contains_exactly_five_schemas(self):
        self.assertEqual(len(SCHEMA_FILES), 5)
        self.assertEqual(sorted(SCHEMA_FILES), sorted(SCHEMA_IDS))

    def test_all_schemas_pass_check_schema_and_ids_match(self):
        # SchemaRegistry.__init__ runs check_schema and verifies every $id;
        # reaching this point without an exception is the assertion.
        for key, expected_id in SCHEMA_IDS.items():
            self.assertEqual(self.registry.schema(key)["$id"], expected_id)

    def test_unknown_schema_key_fails_closed(self):
        with self.assertRaises(UnknownSchemaError):
            self.registry.schema("does-not-exist")
        with self.assertRaises(UnknownSchemaError):
            self.registry.validator("does-not-exist")

    def test_no_remote_references_in_committed_schemas(self):
        for key in SCHEMA_FILES:
            refs = _collect_refs(self.registry.schema(key))
            for ref in refs:
                self.assertTrue(
                    ref.startswith("#/"),
                    f"{key}: non-local $ref {ref!r} would require remote resolution")

    def test_validator_validates_a_committed_fixture(self):
        fixture = json_loader.load_path(
            REPO_ROOT / "tests" / "fixtures" / "machine-readable" / "positive"
            / "reference-set.tokens.json")
        errors = self.registry.iter_errors("token-document", fixture)
        self.assertEqual(errors, [])

    def test_validator_rejects_missing_cds_extension(self):
        errors = self.registry.iter_errors("token-document", {"$extensions": {}})
        self.assertTrue(errors)


def _collect_refs(node, found=None):
    if found is None:
        found = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                found.append(value)
            else:
                _collect_refs(value, found)
    elif isinstance(node, list):
        for item in node:
            _collect_refs(item, found)
    return found


if __name__ == "__main__":
    unittest.main()
