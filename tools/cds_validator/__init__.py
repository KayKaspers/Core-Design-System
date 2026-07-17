"""CDS offline token profile validator (CDS-WP-013).

Experimental, executor-produced tooling for the pinned CDS Token Format
Profile v1 over DTCG 2025.10. Runs fully offline after installation of the
pinned dependencies in ``requirements-validator.lock``.

Boundaries (DEC-S-093 … DEC-S-104):
- no runtime network access, no remote schema resolution, no telemetry;
- layered V1–V4 results are never collapsed into an aggregate score;
- a successful run is executor-produced evidence, not independent review,
  and never a Candidate, Stable, conformance, or release statement.
"""

from tools.cds_validator.version import VALIDATOR_VERSION

__all__ = ["VALIDATOR_VERSION"]
