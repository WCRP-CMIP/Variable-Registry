"""
Check branded variable names against the latest version of the algorithm

Requires a virtual environment with `requirements.txt` installed, e.g.

```
python3 -m venv venv
source venv/bin/activate
pip install -Ur requirements.txt
```
"""

import json
from pathlib import Path

import pandas as pd
from cmip_branded_variable_mapper import map_to_cmip_branded_variable


def split_branded_variable_into_components(bv: str) -> dict[str, str]:
    variable_root_dd, branding_suffix = bv.split("_")
    temporal_label, vertical_label, horizontal_label, area_label = (
        branding_suffix.split("-")
    )

    return {
        "variableRootDD": variable_root_dd,
        "temporal_label": temporal_label,
        "vertical_label": vertical_label,
        "horizontal_label": horizontal_label,
        "area_label": area_label,
    }


def main():
    """Run the checks"""
    IN_FILE = Path(".src") / "v1.2.2_vars.json"
    with open(IN_FILE) as fh:
        raw_json = json.load(fh)

    failures = []
    for compound_name, info in raw_json["Compound Name"].items():
        dimensions = tuple(info["dimensions"].split(" "))
        if any("," in v for v in dimensions):
            msg = (
                f"Dimensions should not contain commas, received: {info['dimensions']}"
            )
            raise ValueError(msg)

        if info["variableRootDD"].startswith("unknown"):
            # No point checking this branded variable
            continue

        # This is how you can generate a branded variable from other info.
        # This would need to sit behind any branded variable generator
        # (might require a local API or something,
        # I assume we can't put this on the front-end side).
        exp_branded_variable = map_to_cmip_branded_variable(
            variable_name=info["variableRootDD"],
            cell_methods=info["cell_methods"],
            dimensions=dimensions,
        )
        if exp_branded_variable != info["branded_variable_name"]:
            # Can do whatever with this, report it,
            # make an issue, fail CI.
            # At least now you see the pattern.
            # For now just print
            msg = (
                f"For {compound_name}, "
                f"branded_variable_name={info['branded_variable_name']} "
                f"but it should be {exp_branded_variable} "
                f"given variableRootDD={info['variableRootDD']}, "
                f"cell_methods={info['cell_methods']!r} "
                f"and dimensions={info['dimensions']!r}"
            )
            print()
            print(msg)

            exp_components = split_branded_variable_into_components(
                exp_branded_variable
            )
            info_components = split_branded_variable_into_components(
                info["branded_variable_name"]
            )

            for k, v_exp in exp_components.items():
                if v_exp != info_components[k]:
                    failure_summary = {
                        "compound_name": compound_name,
                        "component": k,
                        "exp_value": v_exp,
                        "actual_value": info_components[k],
                    }

                    failures.append(failure_summary)

    # Can also make this a pandas dataframe if we want
    failures_df = pd.DataFrame(failures)
    print(failures_df)
    print()
    print(f"Issues for {len(failures_df['compound_name'].unique())} compound names")
    print(failures_df["component"].value_counts())
    disp_cols = ["component", "exp_value", "actual_value"]
    print(failures_df[disp_cols].drop_duplicates().sort_values(by=disp_cols))


if __name__ == "__main__":
    main()
