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
    cell_methods_clashes = defaultdict(list)
    for f in (REPO_ROOT / "src-data" / "cell-method").glob("*.json"):
        with open(f) as fh:
            raw = json.load(fh)

        try:
            cell_methods_lib[raw["validation-key"]] = raw
        except KeyError:
            print(f)
            raise

        cell_methods_clashes[raw["validation-key"]].append((f, raw))

    for cell_methods_string, supplied_by in cell_methods_clashes.items():
        if len(supplied_by) == 1:
            continue

        all_keys = set(k for v in [sb[1] for sb in supplied_by] for k in v)
        differing_vals = defaultdict(dict)
        for k in all_keys:
            first_val = supplied_by[0][1][k]
            if all(sb[1][k] == first_val for sb in supplied_by):
                continue

            for sb in supplied_by:
                differing_vals[sb[0]][k] = sb[1][k]

        supplier_info_l = []
        for sb in supplied_by:
            diff_s = [f"{k}: {v}" for k, v in differing_vals[sb[0]].items()]
            diff_s_rendered = "  - " + "\n  - ".join(diff_s)
            sm = f"{sb[0].relative_to(REPO_ROOT)}\n{diff_s_rendered}"
            supplier_info_l.append(sm)

        supplier_info = "- " + "\n- ".join(supplier_info_l)
        msg = f"{cell_methods_string} is supplied by:\n{supplier_info}"
        print(msg)
        print()

    # Only one clash: the amnsi*-twm files
    # Questions to put in an issue:
    # - they all say weighted time mean, but the cell methods don't indicate any weighting
    #   (except where sea ice which is a masking, not a weighting)
    # - assuming we can just get rid of amnsia-twm (atmos grid)
    #   and amnsib-twm (weighting in bands)
    #   as this information is provided by grid and dimensions
    #   so isn't needed in cell methods
    # - mask isn't a thing for cell methods
    #   (or, if it is, it needs to be shown elsewhere i.e. in the methods themselves?)
    #   Put another way, can we drop the `mask` key from all cell methods entries?
    # - how to describe cell methods. They're describing the methods applied in the cell
    #   not what the data represents (kind of)
    #   e.g. "time: area: mean" still applies to data with lat, lon, time,
    #   it just tells you that each cell represents average values,
    #   rather than e.g. instantaneous values
    # - Is "area: time: mean where ice_free_sea over sea" a valid cell method?
    # - I'm not sure that these cell methods achieve what the DR wants?
    #   "area: time: mean where stratiform_cloud (weighted by total stratiform cloud area)"
    # - Is "depth: sum where sea time: mean" a valid cell methods?
    # - can we strip 'mask' from everything in cell methods
    # - Is "area: mean where sea depth: sum where sea (over entire ocean column) time: mean"
    #   actually what is desired?
    # - Double space in "dlsmszz-tmn"
    # Notes:
    # - helpful link for understanding 'where' in cell methods:
    #   https://cfconventions.org/Data/area-type-table/current/build/area-type-table.html
    # TODO: check hard-coding
    cell_methods_replacements = {
        "amnsia-twm": "amnsi-twm",
        "amnsib-twm": "amnsi-twm",
    }

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
        cell_methods_pid = cm_pid_l[0]
        cell_methods = dr_table[key]["records"][cell_methods_pid][key].strip()
        cell_methods_id = dr_table["Cell Methods"]["records"][cell_methods_pid]["label"]

        key = "Cell Measures"
        try:
            cm_pid_l = record[key]
            cell_measures_l = []
            for cm_pid in cm_pid_l:
                # TODO: check values, some are clearly wrong e.g. both areacella and areacello
                cell_measures_l.append(dr_table[key]["records"][cm_pid]["Name"].strip())

            cell_measures = " ".join(cell_measures_l)
        except KeyError:
            cell_measures = ""
            # # TODO: update to saner convention
            # cell_measures = None

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

        units_l = record["Units (from Physical Parameter)"]
        if len(units_l) != 1:
            raise AssertionError(units_l)
        units = units_l[0]

        spatial_shape_pid_l = record["Spatial Shape"]
        if len(spatial_shape_pid_l) != 1:
            raise AssertionError(spatial_shape_pid_l)
        spatial_shape_pid = spatial_shape_pid_l[0]
        spatial_shape = dr_table["Spatial Shape"]["records"][spatial_shape_pid]["Name"]

        temporal_shape_pid_l = record["Temporal Shape"]
        if len(temporal_shape_pid_l) != 1:
            raise AssertionError(temporal_shape_pid_l)
        temporal_shape_pid = temporal_shape_pid_l[0]
        temporal_shape = dr_table["Temporal Shape"]["records"][temporal_shape_pid][
            "Name"
        ]

        cmip6_table_pid_l = record["CMIP6 Table (legacy)"]
        if len(cmip6_table_pid_l) != 1:
            raise AssertionError(cmip6_table_pid_l)
        cmip6_table_pid = cmip6_table_pid_l[0]
        cmip6_table = dr_table["CMIP6 Table Identifiers (legacy)"]["records"][
            cmip6_table_pid
        ]["Name"]

        if "Positive Direction" in record:
            positive = record["Positive Direction"]
        else:
            positive = ""
            # # TODO: update to saner convention
            # positive = None

        branded_variable = record["Branded Variable Name"]
        try:
            cell_methods_lib[cell_methods]
        except KeyError:
            print(branded_variable)
            print(cell_methods_id)
            raise
        try:
            temporal_label, vertical_label, horizontal_label, area_label = (
                branded_variable.split("_")[1].split("-")
            )
        except IndexError:
            temporal_label = "u"
            vertical_label = "u"
            horizontal_label = "u"
            area_label = "u"

        # # TODO: check against variable root
        # if variable_root.lower() not in variable_root_lib:
        #     raise KeyError(variable_root.lower())

        # TODO: check against air label
        # TODO: check against dimensions
        # TODO: check against horizontal label
        # TODO: check against temporal label
        # TODO: check against vertical label
        # Note: checking like this is silly, it's reinventing SQL.
        # Do this instead by trying to populate a table using pydantic/sqlmodel.
        # That will raise if we try to have duplicate IDs, missing cross-links or similar
        # and it brings the side benefit of defining pydantic models for all our data.

        # ID is all lowercase
        id = branded_variable.lower()
        # validation-key is the value as it should appear in files etc.
        validation_key = branded_variable

        out_info = {
            "id": id,
            "validation-key": validation_key,
            "ui-label": record["Title"],
            "description": record["Description"].strip(),
            "area-label": area_label,
            "cell-measures": cell_measures,
            "cell-methods": cell_methods_id,
            "dimensions": list(dimensions),
            # TODO: Drop - npt a variable registry thing
            # (DR thing, for example)
            "frequency": frequency,
            "horizontal-label": horizontal_label,
            "model-realm": model_realm,
            # TODO: Drop ?
            "out-name": variable_root,
            "physical-parameter-name": variable_root,
            # TODO: Drop ?
            "positive": positive,
            # TODO: Drop ?
            "remove-cmip6-table": cmip6_table,
            # TODO: Drop ?
            "spatial-shape": spatial_shape,
            # TODO: update standard name somehow because values don't seem right
            # e.g. standard name for cropFracC3 is area_fraction
            "standard-name": standard_name,
            "temporal-label": temporal_label,
            # TODO: Drop ?
            "temporal-shape": temporal_shape,
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

        with open(REPO_ROOT / "src-data" / "variable" / f"{id}.json", "w") as fh:
            json.dump(out_info, fh, indent=4)
            fh.write("\n")

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
