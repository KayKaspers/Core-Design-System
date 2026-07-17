"""Local, offline schema registry for the CDS validator (DEC-S-096).

Contains exactly the five committed CDS-owned JSON Schema Draft 2020-12
contracts, resolved by their stable ``tag:`` identities through a local
``referencing.Registry``. There is no HTTP retrieval; an unknown schema
identity fails closed.
"""

from __future__ import annotations

from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry
from referencing.jsonschema import DRAFT202012

from tools.cds_validator import json_loader
from tools.cds_validator.version import SCHEMA_IDS

#: schema key -> committed local schema file (relative to the repository root).
SCHEMA_FILES = {
    "token-document": "schemas/cds-token-document.schema.json",
    "source-set-manifest": "schemas/cds-source-set-manifest.schema.json",
    "resolver-document": "schemas/cds-resolver-document.schema.json",
    "validation-case": "schemas/cds-validation-case.schema.json",
    "validation-result": "schemas/cds-validation-result.schema.json",
}


class UnknownSchemaError(Exception):
    """Requested schema identity is not in the local registry (fail closed)."""


class SchemaRegistry:
    """Loads, checks, and serves the five CDS schemas fully offline."""

    def __init__(self, repository_root: Path | str):
        self.repository_root = Path(repository_root)
        self._schemas: dict[str, dict] = {}
        resources = []
        for key, rel_path in SCHEMA_FILES.items():
            schema = json_loader.load_path(self.repository_root / rel_path)
            expected_id = SCHEMA_IDS[key]
            actual_id = schema.get("$id")
            if actual_id != expected_id:
                raise UnknownSchemaError(
                    f"Schema {rel_path} carries $id {actual_id!r}; expected {expected_id!r}"
                )
            # check_schema raises SchemaError on an invalid 2020-12 schema.
            Draft202012Validator.check_schema(schema)
            self._schemas[key] = schema
            resources.append((expected_id, DRAFT202012.create_resource(schema)))
        self._registry = Registry().with_resources(resources)

    @property
    def schema_ids(self) -> dict[str, str]:
        return dict(SCHEMA_IDS)

    def schema(self, key: str) -> dict:
        if key not in self._schemas:
            raise UnknownSchemaError(f"Unknown schema key: {key!r}")
        return self._schemas[key]

    def validator(self, key: str) -> Draft202012Validator:
        return Draft202012Validator(self.schema(key), registry=self._registry)

    def iter_errors(self, key: str, instance) -> list:
        return sorted(
            self.validator(key).iter_errors(instance), key=lambda e: list(e.absolute_path)
        )
