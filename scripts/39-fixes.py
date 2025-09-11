"""
Fixes from #39
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable, mapping in (("ncfc22_tavg-u-hm-u", ("ncfc", "hcfc")),):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        for key in working:
            if working[key] is None:
                continue

            if isinstance(working[key], list):
                working[key] = [v.replace(*mapping) for v in working[key]]

            else:
                working[key] = working[key].replace(*mapping)

        with open(
            REPO_ROOT
            / "src-data"
            / "variable"
            / f"{branded_variable.replace(*mapping)}.json",
            "w",
        ) as fh:
            json.dump(working, fh, indent=4)

        (REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json").unlink()


if __name__ == "__main__":
    main()
