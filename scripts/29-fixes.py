"""
Fixes from #29
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Apply the fixes
    """
    REPO_ROOT = Path(__file__).parents[1]

    for branded_variable, new_units, new_description in (
        ("clmodis_tavg-p7c-hxy-air", "%", "MODIS Cloud Area Percentage"),
        ("clmodisice_tavg-p7c-hxy-air", "%", "MODIS Ice Topped Cloud Area Percentage"),
        ("clmodisiceReff_tavg-u-hxy-u", "%", "MODIS Ice Topped Cloud Area Percentage"),
        (
            "clmodisliquid_tavg-p7c-hxy-air",
            "%",
            "MODIS Liquid Topped Cloud Area Percentage",
        ),
        (
            "clmodisliquidReff_tavg-u-hxy-u",
            "%",
            "MODIS Liquid Topped Cloud Area Percentage",
        ),
        (
            "siconc_tavg-u-hxy-u",
            "%",
            "Percentage of a given grid cell that is covered by sea ice on the ocean grid, independent of the thickness of that ice.",
        ),
        (
            "siitdconc_tavg-u-hxy-u",
            "%",
            "Percentage of grid cell covered by each ice thickness category (vector with one entry for each ice thickness category starting from the thinnest category, netcdf file should use thickness bounds of the categories as third coordinate axis).",
        ),
        (
            "siitdsnconc_tavg-u-hxy-si",
            "%",
            "Percentage of grid cell covered by snow in each ice thickness category (vector with one entry for each ice thickness category starting from the thinnest category, netcdf file should use thickness bounds of the categories as third coordinate axis).",
        ),
        (
            "snc_tavg-u-hxy-si",
            "%",
            "Percentage of the sea-ice surface that is covered by snow. In many models that do not explicitly resolve a percentage of snow, this variable will always be either 0 or 100.",
        ),
        (
            "siextent_tavg-u-hm-u",
            None,
            "Total integrated area of all grid cells that are covered by at least 15% sea ice (siconc >= 15). Does not include grid cells partially covered by land.",
        ),
    ):
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json"
        ) as fh:
            working = json.load(fh)

        if new_units is not None:
            working["units"] = new_units

        if new_description is not None:
            working["description"] = new_description

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
