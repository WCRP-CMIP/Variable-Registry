"""
Fixes from #19
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable in set(
        [
            # Could have removed duplication, but set does the job
            "tob_tavg-u-hxy-sea",
            "pbo_tavg-u-hxy-sea",
            "sob_tavg-u-hxy-sea",
            "expcalcob_tavg-u-hxy-sea",
            "expfeob_tavg-u-hxy-sea",
            "expcob_tavg-u-hxy-sea",
            "expcob_tavg-u-hxy-sea",
            "expnob_tavg-u-hxy-sea",
            "exppob_tavg-u-hxy-sea",
            "expsiob_tavg-u-hxy-sea",
            "hfgeou_ti-u-hxy-sea",
            "fric_tavg-u-hxy-sea",
            "froc_tavg-u-hxy-sea",
            "deptho_ti-u-hxy-sea",
            "exparagob_tavg-u-hxy-sea",
            "expcalcob_tavg-u-hxy-sea",
            "expfeob_tavg-u-hxy-sea",
            "expcob_tavg-u-hxy-sea",
            "expcob_tavg-u-hxy-sea",
            "expnob_tavg-u-hxy-sea",
            "exppob_tavg-u-hxy-sea",
            "expsiob_tavg-u-hxy-sea",
            "hfgeou_ti-u-hxy-sea",
            "hfgeou_ti-u-hxy-sea",
        ]
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        try:
            working["dimensions"].pop(working["dimensions"].index("depthseafloor"))
        except ValueError:
            print(f"Didn't find depthseafloor for {branded_variable}")

        try:
            working["dimensions"].pop(working["dimensions"].index("seafloor"))
        except ValueError:
            print(f"Didn't find seafloor for {branded_variable}")

        if "at_sea_floor" not in working["standard-name"]:
            working["standard-name"] = working["standard-name"].replace(
                "mole_flux", "mole_flux_at_sea_floor"
            )

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
