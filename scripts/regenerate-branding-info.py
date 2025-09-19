"""
Regenerate branding info

You will need an environment with `cmip-branded-variable-mapper` installed
"""

from __future__ import annotations

import json
from pathlib import Path

import cmip_branded_variable_mapper
from cmip_branded_variable_mapper import map_to_cmip_branded_variable


def main():
    """
    Apply the fixes
    """
    print(f"{cmip_branded_variable_mapper.__version__=}")
    REPO_ROOT = Path(__file__).parents[1]

    for variable_definition_file in (REPO_ROOT / "src-data" / "variable").glob(
        "*.json"
    ):
        with open(variable_definition_file) as fh:
            working = json.load(fh)

        branded_variable = map_to_cmip_branded_variable(
            variable_name=working["variable-root"],
            cell_methods=working["cell-methods"],
            dimensions=tuple(working["dimensions"]),
        )
        temporal_label, vertical_label, horizontal_label, area_label = (
            branded_variable.split("_")[1].split("-")
        )

        working["id"] = branded_variable
        working["validation-key"] = branded_variable
        working["area-label"] = area_label
        working["horizontal-label"] = horizontal_label
        working["temporal-label"] = temporal_label
        working["vertical-label"] = vertical_label

        variable_definition_file.unlink()

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json",
            "w",
        ) as fh:
            json.dump(working, fh, indent=4)


if __name__ == "__main__":
    main()
