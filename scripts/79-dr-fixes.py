"""
Fixes from DR #79
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable, new_description in (
        (
            "sci_tavg-u-hxys-u",
            "Fraction of time that shallow convection occurs in the grid cell. This variable is binary, indicating whether at each time step convection occurs (1.0), or not (0.0).",
        ),
        (
            "sci_tavg-u-hxy-u",
            "Fraction of time that shallow convection occurs in the grid cell. This variable is binary, indicating whether at each time step convection occurs (1.0), or not (0.0).",
        ),
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        working["description"] = new_description

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
