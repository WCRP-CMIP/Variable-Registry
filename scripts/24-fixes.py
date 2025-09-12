"""
Fixes from #24
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
            "reffclwtop_tavg-u-hxy-u",
            "area: time: mean where liquid_cloud (weighted by area of upper-most cloud layer)",
        ),
        (
            "reffcclwtop_tavg-u-hxy-ccl",
            "area: time: mean where convective_cloud (weighted by area of upper-most cloud layer)",
        ),
        (
            "reffsclwtop_tavg-u-hxy-scl",
            "area: time: mean where stratiform_cloud (weighted by area of upper-most cloud layer)",
        ),
        (
            "reffccwctop_tavg-u-hxy-ccl",
            "area: time: mean where convective_cloud (weighted by area of upper-most cloud layer)",
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
