"""The single controlled JSON loader for every CDS validation path.

Every JSON input to the validator MUST pass through this module (DEC-S-095,
RISK-076): UTF-8, strict JSON per RFC 8259, duplicate-object-member detection
via ``object_pairs_hook``. There is no first-key-wins or last-key-wins repair
and no network access. Direct, uncontrolled ``json.load`` paths are
prohibited elsewhere in the validator.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class LoaderError(Exception):
    """Base error for controlled-loader failures."""

    def __init__(self, message: str, source: str, json_pointer: str | None = None):
        super().__init__(message)
        self.source = source
        self.json_pointer = json_pointer


class EncodingError(LoaderError):
    """Input is not valid UTF-8."""


class JsonParseError(LoaderError):
    """Input is not strict RFC 8259 JSON."""


class DuplicateKeyError(LoaderError):
    """A JSON object repeats a member name (fails V1, DEC-S-088)."""

    def __init__(self, key: str, source: str, json_pointer: str):
        super().__init__(
            f"Duplicate object member name {key!r} at {json_pointer or '/'} "
            "(prohibited; not repaired via first-key-wins or last-key-wins)",
            source,
            json_pointer,
        )
        self.key = key


class _DuplicateTrackingDict(dict):
    """Marker type so nested hooks can locate child object positions."""


def _pairs_hook_factory(source: str):
    def hook(pairs: list[tuple[str, Any]]) -> dict:
        obj = _DuplicateTrackingDict()
        for key, value in pairs:
            if key in obj:
                raise DuplicateKeyError(key, source, _pointer_of(obj, key))
            obj[key] = value
        return obj

    return hook


def _pointer_of(obj: dict, key: str) -> str:
    # The hook runs bottom-up, so the absolute document pointer of the parent
    # is unknown at detection time; report the duplicated member itself.
    escaped = key.replace("~", "~0").replace("/", "~1")
    return f"/{escaped}"


def parse_text(text: str, source: str) -> Any:
    """Parse strict JSON text with duplicate-key rejection."""
    try:
        return json.loads(text, object_pairs_hook=_pairs_hook_factory(source))
    except DuplicateKeyError:
        raise
    except json.JSONDecodeError as exc:
        raise JsonParseError(
            f"Invalid strict JSON: {exc.msg} (line {exc.lineno}, column {exc.colno})",
            source,
        ) from exc


def load_path(path: Path | str) -> Any:
    """Load a local file as UTF-8 strict JSON with duplicate-key rejection."""
    path = Path(path)
    source = str(path)
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise LoaderError(f"Cannot read file: {exc}", source) from exc
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise EncodingError(f"Not valid UTF-8: {exc}", source) from exc
    return parse_text(text, source)
