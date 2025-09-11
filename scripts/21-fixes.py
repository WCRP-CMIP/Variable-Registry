"""
Fixes from #21
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable in (
        "uos_tavg-u-hxy-sea",
        "vos_tavg-u-hxy-sea",
        "dpco2_tavg-u-hxy-sea",
        "spco2_tavg-u-hxy-sea",
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        working["dimensions"].pop(working["dimensions"].index("depth0m"))

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
