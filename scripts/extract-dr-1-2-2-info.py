"""
Extract v1.2.2 of the data request
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


def main():
    """
    Extract the info
    """
    REPO_ROOT = Path(__file__).parents[1]

    variable_root_lib = {}
    for f in (REPO_ROOT / "src-data" / "variable-root").glob("*.json"):
        with open(f) as fh:
            raw = json.load(fh)

        variable_root_lib[raw["id"]] = raw

    cell_methods_lib = {}
    for f in (REPO_ROOT / "src-data" / "cell-method").glob("*.json"):
        with open(f) as fh:
            raw = json.load(fh)

        # if raw["description"] in cell_methods:
        #     msg = f"{raw=}\n" f"{cell_methods[raw['description']]}"
        #     raise AssertionError(msg)

        cell_methods_lib[raw["description"]] = raw

    DR_RELEASE_EXPORT = (
        REPO_ROOT
        / ".."
        / "CMIP7_DReq_Content"
        / "airtable_export"
        / "dreq_release_export.json"
    )

    with open(DR_RELEASE_EXPORT) as fh:
        dr_release = json.load(fh)

    dr_table = dr_release["Data Request v1.2.2"]
    records = dr_table["Variables"]["records"]
    out_info_already_recorded = {}
    dr_internal_consistency_issues = defaultdict(dict)
    for pid, record in records.items():
        dimensions = tuple(v.strip() for v in record["Dimensions"].split(","))

        key = "Cell Methods"
        cm_pid_l = record[key]
        if len(cm_pid_l) > 1:
            raise AssertionError
        cm_pid = cm_pid_l[0]
        cell_methods = dr_table[key]["records"][cm_pid][key].strip()

        key = "Cell Measures"
        try:
            cm_pid_l = record[key]
            cell_measures_l = []
            for cm_pid in cm_pid_l:
                # TODO: check values, some are clearly wrong e.g. both areacella and areacello
                cell_measures_l.append(dr_table[key]["records"][cm_pid]["Name"].strip())

            cell_measures = " ".join(cell_measures_l)
        except KeyError:
            cell_measures = None

        key = "Physical Parameter"
        pp_pid_l = record[key]
        if len(pp_pid_l) > 1:
            raise AssertionError
        pp_pid = pp_pid_l[0]
        variable_root = dr_table[f"{key}s"]["records"][pp_pid]["Name"].strip()

        key = "CMIP7 Frequency"
        freq_pid_l = record[key]
        if len(freq_pid_l) > 1:
            raise AssertionError
        freq_pid = freq_pid_l[0]
        frequency = dr_table[key]["records"][freq_pid]["Name"].strip()

        key = "Modelling Realm - Primary"
        mr_pid_l = record[key]
        if len(mr_pid_l) > 1:
            raise AssertionError
        mr_pid = mr_pid_l[0]
        model_realm = dr_table["Modelling Realm"]["records"][mr_pid]["id"].strip()

        key = "CF Standard Name (from Physical Parameter)"
        sn_pid_l = record[key]
        if len(sn_pid_l) > 1:
            raise AssertionError
        sn_pid = sn_pid_l[0]
        standard_name = dr_table["CF Standard Names"]["records"][sn_pid]["Name"].strip()

        description = record["Title"]

        units_l = record["Units (from Physical Parameter)"]
        if len(units_l) != 1:
            raise AssertionError(units_l)
        units = units_l[0]

        branded_variable = record["Branded Variable Name"]
        try:
            temporal_label, vertical_label, horizontal_label, area_label = (
                branded_variable.split("_")[1].split("-")
            )
        except IndexError:
            temporal_label = "u"
            vertical_label = "u"
            horizontal_label = "u"
            area_label = "u"

        # # TODO: check and link cell methods
        # cell_methods_lib[cell_methods]

        # TODO: check against variable root
        if variable_root.lower() not in variable_root_lib:
            raise KeyError(variable_root.lower())

        # TODO: check against air label
        # TODO: check against dimensions
        # TODO: check against horizontal label
        # TODO: check against temporal label
        # TODO: check against vertical label

        out_info = {
            "id": branded_variable,
            "validation-key": branded_variable,
            "ui-label": description,
            "description": record["Description"].strip(),
            "area-label": area_label,
            "cell-measures": cell_measures,
            "cell-methods": cell_methods,
            "dimensions": list(dimensions),
            # # Drop - npt a variable registry thing
            # # (DR thing, for example)
            # "frequency": frequency,
            "horizontal-label": horizontal_label,
            "model-realm": model_realm,
            # # Drop ?
            # "out-name"
            "physical-parameter-name": variable_root,
            # # Drop or get from cf somewhere ?
            # "positive"
            # # Drop ?
            # "remove-cmip6-table"
            # # Drop ?
            # "spatial-shape"
            # TODO: update standard name somehow because values don't seem right
            # e.g. standard name for cropFracC3 is area_fraction
            "standard-name": standard_name,
            "temporal-label": temporal_label,
            # # Drop ?
            # "temporal-shape"
            "units": units,
            "variable-root": variable_root.lower(),
            "vertical-label": vertical_label,
            "@context": "_context_",
            "type": ["wcrp:variable", "variable-registry"],
        }

        if branded_variable in out_info_already_recorded:
            for k in out_info:
                if out_info[k] != out_info_already_recorded[branded_variable][k]:
                    rcn = record["CMIP6 Compound Name"]
                    ecn = out_info_already_recorded[branded_variable][
                        "CMIP6 Compound Name"
                    ]
                    msg = (
                        f"For {branded_variable=}, "
                        f"{rcn} and {ecn} disagree. "
                        f"According to {rcn}, {k} is {out_info[k]}. "
                        f"According to {ecn}, {k} is {out_info_already_recorded[branded_variable][k]}. "
                    )
                    print(msg)

                    if k not in dr_internal_consistency_issues[branded_variable]:
                        dr_internal_consistency_issues[branded_variable][k] = {}

                    dr_internal_consistency_issues[branded_variable][k][rcn] = out_info[
                        k
                    ]
                    dr_internal_consistency_issues[branded_variable][k][ecn] = (
                        out_info_already_recorded[branded_variable][k]
                    )

        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(out_info, fh, indent=4)

        out_info_already_recorded[branded_variable] = {
            **out_info,
            "CMIP6 Compound Name": record["CMIP6 Compound Name"],
        }

    with open(REPO_ROOT / "DR-1-2-2-internal-consistency-issues.md", "w") as fh:
        for bv, issues in dr_internal_consistency_issues.items():
            fh.write(f"**{bv}**\n\n")

            for key in issues:
                fh.write(f"- {key}\n")
                for source, value in issues[key].items():
                    fh.write(f"    - {source}: {value!r}\n")

                fh.write("\n")

            fh.write("\n")

    print(f"{len(dr_internal_consistency_issues)=}")


if __name__ == "__main__":
    main()
