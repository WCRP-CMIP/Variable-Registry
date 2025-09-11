"""
Fixes from DR #87
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
            "ci_tavg-u-hxy-u",
            "Fraction of time that convection occurs in the grid cell. If native cell data is regridded, the area-weighted mean of the contributing cells should be reported.",
        ),
        (
            "sci_tavg-u-hxy-u",
            "Fraction of time that convection occurs in the grid cell. If native cell data is regridded, the area-weighted mean of the contributing cells should be reported.",
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
