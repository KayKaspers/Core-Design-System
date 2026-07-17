"""RFC 8785 canonicalization and SHA-256 content digests (ADR-0002, DEC-S-100).

A digest is an integrity aid over parsed content. It is NOT a signature and
proves no authorship, approval, authenticity, or release legitimacy
(RISK-072). Digests are produced only from content that passed the V1 parse;
duplicate-key input never receives a digest.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import rfc8785

from tools.cds_validator import json_loader

CANONICALIZATION_METHOD = "RFC 8785 (JSON Canonicalization Scheme)"
DIGEST_ALGORITHM = "SHA-256"
DIGEST_PREFIX = "sha256:"


class DigestError(Exception):
    """Content cannot be canonicalized (controlled failure, no repair)."""


def canonical_bytes(content: Any) -> bytes:
    """Canonicalize parsed JSON content per RFC 8785."""
    try:
        return rfc8785.dumps(content)
    except rfc8785.CanonicalizationError as exc:
        raise DigestError(f"Unsupported canonicalization input: {exc}") from exc
    except (TypeError, ValueError) as exc:
        raise DigestError(f"Unsupported canonicalization input: {exc}") from exc


def content_digest(content: Any) -> str:
    """``sha256:`` + lowercase-hex SHA-256 of the RFC 8785 canonical form."""
    return DIGEST_PREFIX + hashlib.sha256(canonical_bytes(content)).hexdigest()


def digest_file(path: Path | str) -> str:
    """Digest a local strict-JSON file.

    Raises LoaderError subclasses if V1 parsing fails (including duplicate
    keys) and DigestError for unsupported canonicalization input.
    """
    return content_digest(json_loader.load_path(Path(path)))
