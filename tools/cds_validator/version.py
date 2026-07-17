"""Version and identity constants for the CDS offline token validator."""

from __future__ import annotations

import platform
import sys
from importlib import metadata

VALIDATOR_VERSION = "0.1.0"
PROFILE_VERSION = "1"
DTCG_REPORT_VERSION = "2025.10"

SCHEMA_IDS = {
    "token-document": "tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-token-document/1",
    "source-set-manifest": "tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-source-set-manifest/1",
    "resolver-document": "tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-resolver-document/1",
    "validation-case": "tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-validation-case/1",
    "validation-result": "tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-validation-result/1",
}

DIRECT_DEPENDENCIES = ("jsonschema", "rfc8785")


def dependency_versions() -> dict[str, str]:
    """Exact installed versions of the pinned direct dependencies."""
    versions: dict[str, str] = {}
    for name in DIRECT_DEPENDENCIES:
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = "not installed"
    return versions


def runtime_identity() -> dict[str, str]:
    """Exact executed runtime identity for evidence binding (DEC-S-101)."""
    return {
        "pythonVersion": platform.python_version(),
        "pythonImplementation": platform.python_implementation(),
        "platform": sys.platform,
    }
