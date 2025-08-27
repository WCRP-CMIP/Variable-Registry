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
    # Make long cell_methods display
    pd.options.display.max_colwidth = 200
    # pd.options.display.max_columns = 10

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
                        "cell_methods": info["cell_methods"],
                        "dimensions": info["dimensions"],
                    }

                    failures.append(failure_summary)

    # Can also make this a pandas dataframe if we want
    failures_df = pd.DataFrame(failures)
    print(failures_df)
    print()
    print(f"Issues for {len(failures_df['compound_name'].unique())} compound names")

    print()
    print(failures_df["component"].value_counts())

    disp_cols = ["component", "exp_value", "actual_value", "cell_methods", "dimensions"]
    error_types = failures_df[disp_cols].drop_duplicates().sort_values(by=disp_cols)
    failing_compounds = (
        failures_df.groupby(disp_cols)
        .apply(lambda x: x["compound_name"].unique().tolist(), include_groups=False)
        .to_frame("affected_compounds")
    )
    failing_compounds["n_affected"] = failing_compounds["affected_compounds"].apply(len)
    failing_compounds["affected_compounds"] = failing_compounds[
        "affected_compounds"
    ].apply(lambda x: x if len(x) <= 5 else f"{str(x[:5])[:-1]}...")
    failing_compounds = failing_compounds[["n_affected", "affected_compounds"]]
    print()
    print(error_types)
    print()
    print(f"{error_types.shape[0]} different kinds of errors")

    print()
    print(
        failing_compounds.reset_index(
            ["cell_methods", "dimensions"], drop=True
        ).sort_index()
    )

    error_types["comment"] = (
        # None
        "Error applying branding algorithm, "
        "should be fixed with a simple re-run over the DR (?)"
    )
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "lnd")
        & (error_types["actual_value"] == "sn")
        & (error_types["cell_methods"] == "area: mean where land time: mean"),
        "comment",
    ] = "cell_methods should be 'area: mean where snow'?"
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "lnd")
        & (error_types["actual_value"] == "sn")
        & (
            error_types["cell_methods"]
            == "area: mean where land time: mean (weighted by snow area)"
        ),
        "comment",
    ] = "cell_methods should be 'area: mean where snow'?"
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "lnd")
        & (error_types["actual_value"] == "veg"),
        "comment",
    ] = "cell_methods should be 'area: mean where vegetation'?"
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "lsi")
        & (error_types["actual_value"] == "u"),
        "comment",
    ] = "needs re-run of branding algorithm to fix known issue"
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "sea")
        & (error_types["actual_value"] == "si"),
        "comment",
    ] = "cell_methods should be 'area: mean where sea_ice'?"
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "sea")
        & (error_types["actual_value"] == "u"),
        "comment",
    ] = "cell_methods should be 'area: mean where sea_ice'?"
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "si")
        & (error_types["actual_value"] == "u"),
        "comment",
    ] = (
        "unclear if branding algorithm needs an update "
        "(i.e. actual_value is correct, this should be unspecified because of the weird masking) "
        "or actual_value is just wrong "
        "(i.e. need to re-run the branding algorithm on the DR)"
    )
    error_types.loc[
        (error_types["component"] == "area_label")
        & (error_types["exp_value"] == "u")
        & (error_types["actual_value"] == "lnd"),
        "comment",
    ] = "cell_methods should be 'area: mean where sea_ice' (same as day.snc)?"
    error_types.loc[
        (error_types["component"] == "horizontal_label"),
        "comment",
    ] = "Need to check branding algorithm logic with Karl"
    error_types.loc[
        (error_types["component"] == "temporal_label")
        & (error_types["exp_value"] == "ti")
        & (error_types["actual_value"] == "tclm"),
        "comment",
    ] = "is dimension 'timefxc' a thing? If yes, need to update the branding algorithm. If no, need to fix the dimensions"
    error_types.loc[
        (error_types["component"] == "vertical_label")
        & (error_types["exp_value"] == "u")
        & (error_types["actual_value"] == "d0m"),
        "comment",
    ] = "need to add depth0m to the dimensions?"
    error_types.loc[
        (error_types["component"] == "vertical_label")
        & (error_types["exp_value"] == "u")
        & (error_types["actual_value"] == "h2m"),
        "comment",
    ] = "need to add height2m to the dimensions? Is 'lowerModelLayer' a dimension we should be able to handle?"

    pd.options.display.max_colwidth = 130
    print(
        error_types[
            [
                "comment",
                "component",
                "exp_value",
                "actual_value",
            ]
        ]
    )


if __name__ == "__main__":
    main()
