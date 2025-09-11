"""
Fixes from #23
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable, new_cell_methods, new_description in (
        (
            "albisccp_tavg-u-hxy-cl",
            "area: time: mean where cloud (weighted by the ISCCP total cloud area)",
            "Time-means are weighted by the ISCCP Total Cloud Fraction - see cfmip.org/tools-and-data/cosp. Values will be missing where there are no clouds or no sunlight.",
        ),
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        working["cell-methods"] = new_cell_methods
        working["description"] = new_description

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
