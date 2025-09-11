"""
Fixes from DR #84
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
            "esn_tavg-u-hxy-sn",
            "area: mean where snow (on land only) time: mean",
            "Evapotranspiration flux due to conversion of liquid or solid water into vapor at the surface where there is snow on land",
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
