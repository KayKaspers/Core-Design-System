"""Module entry point: ``python -m tools.cds_validator`` (DEC-S-094)."""

import sys

from tools.cds_validator.cli import main

if __name__ == "__main__":
    sys.exit(main())
