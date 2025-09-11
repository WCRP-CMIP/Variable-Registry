"""
Fixes from DR #80
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable, new_cell_methods, new_dimensions in (
        (
            "o3ref_tclm-al-hxy-u",
            "area: mean time: mean within years time: mean over years",
            ("longitude", "latitude", "alevel", "time2"),
        ),
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        working["cell-methods"] = new_cell_methods
        working["dimensions"] = list(new_dimensions)

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
