"""
Extract v1.2.2 of the data request
"""

from __future__ import annotations

import json
from pathlib import Path


def main():
    """
    Extract the info
    """
    REPO_ROOT = Path(__file__).parents[1]

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
    records_l = []
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

        record = {
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
            "variable-root": variable_root,
            "vertical-label": vertical_label,
            "@context": "_context_",
            "type": ["wcrp:variable", "variable-registry"],
        }

        # records_l.append(record)
        with open(
            REPO_ROOT / "src-data" / "variable" / f"{branded_variable}.json", "w"
        ) as fh:
            json.dump(record, fh, indent=4)

        # break


if __name__ == "__main__":
    main()
