"""
Fixes from #26
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable, new_cell_methods in (
        (
            # ImonAnt.tsn, ImonGre.tsn, LImon.tsnIs
            "tsn_tavg-u-hxy-is",
            "depth: area: time: mean where ice_sheet (weighted by snow mass on ice_sheet)",
        ),
        (
            # LImon.tsn, Eday.tsn
            "tsn_tavg-u-hxy-lnd",
            "depth: area: mean where land time: mean (weighted by snow mass on land)",
        ),
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        working["cell-methods"] = new_cell_methods

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
