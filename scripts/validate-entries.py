"""
Validate entries

Currently, only validates horizontal labels
and links between variables and variable roots,
but the idea is that we eventually build this out
to validate everything.

This uses [sqlmodel](https://sqlmodel.tiangolo.com/)
to build an SQL database from our entries.
This validates that the links between entries is correct
e.g. unique IDs where there should be, no dangling links.
It also ensures that every entry matches a given schema
(which should also match context).

We could split this out into multiple files.
For now, one big file is fine.
"""

# Do not use this, it breaks  sqlmodel
# from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

REPO_ROOT = Path(__file__).parents[1]


class HorizontalLabel(SQLModel, table=True):
    """
    Label which indicates the horizontal extent/dimensionality of a given variable
    """

    # TODO: add validation that this must be lowercase
    id: str = Field(primary_key=True)
    """
    Unique ID for this horizontal label
    """

    # TODO: switch _ to - when serialising and deserialising
    validation_key: str
    """
    Value as used throughout CMIP

    Unlike `id`, this can contain uppercase characters
    """

    ui_label: str
    """
    Text to use for this label in user interfaces
    """

    description: str
    """
    Description of the meaning of this horizontal label
    """

    variables: list["Variable"] = Relationship(back_populates="horizontal_label")
    """
    Variables that use this horizontal label
    """

    # auto-inject context and type on serialisation


class VariableRoot(SQLModel, table=True):
    """
    Variable root
    """

    # TODO: add validation that this must be lowercase
    id: str = Field(primary_key=True)
    """
    Unique ID for this variable root
    """

    # TODO: switch _ to - when serialising and deserialising
    validation_key: str
    """
    Value as used throughout CMIP

    Unlike `id`, this can contain uppercase characters
    """

    ui_label: str
    """
    Text to use for this label in user interfaces
    """

    # Surely we should have a description key here

    data_type: str
    """
    [TODO]
    """

    standard_name: str
    """
    CF [TODO check] standard name for this variable root
    """
    # TODO: consider whether to validate the link with the CF standard name list

    variables: list["Variable"] = Relationship(back_populates="variable_root")
    """
    Variables that use this variable root
    """

    # auto-inject context and type on serialisation


class Variable(SQLModel, table=True):
    """
    Variable (technically, branded variable)
    """

    # TODO: add validation that this must be lowercase
    id: str = Field(primary_key=True)
    """
    Unique ID for this variable
    """

    # TODO: switch _ to - when serialising and deserialising
    validation_key: str
    """
    Value as used throughout CMIP

    Unlike `id`, this can contain uppercase characters
    """

    ui_label: str
    """
    Text to use for this label in user interfaces
    """

    description: str
    """
    Description of the variable
    """

    area_label: str  # TODO: make link
    """
    Area label associated with this variable
    """

    cell_measures: str  # TODO: make link
    """
    Cell measures associated with this variable
    """

    cell_methods: str  # TODO: make link
    """
    Cell methods associated with this variable
    """

    dimensions: str  # TODO: fix type and make link
    """
    Dimensions associated with this variable
    """

    horizontal_label_id: str = Field(foreign_key="horizontallabel.id")
    """
    ID of the horizontal label associated with this variable
    """

    horizontal_label: HorizontalLabel = Relationship(back_populates="variables")
    """
    Horizontal label associated with this variable
    """

    model_realm: str  # TODO: make link
    """
    Model realm to which this variable applies
    """

    physical_parameter_name: str
    """
    Name of the physical parameter represented by this variable
    """

    standard_name: str
    """
    CF [TODO check] standard name for this variable root
    """
    # TODO: consider whether to validate the link with the CF standard name list

    temporal_label: str  # TODO: make link
    """
    Temporal label associated with this variable
    """

    units: str  # TODO: consider validation
    """
    Units to be used with this variable
    """

    variable_root_id: str = Field(foreign_key="variableroot.id")
    """
    ID of the variable root associated with this variable
    """

    variable_root: VariableRoot = Relationship(back_populates="variables")
    """
    Variable root associated with this variable
    """

    vertical_label: str  # TODO: make link
    """
    Vertical label associated with this variable
    """

    # auto-inject context and type on serialisation


def get_horizontal_labels_by_id(
    definition_files: Iterable[Path],
) -> dict[str, HorizontalLabel]:
    """
    Get horizontal labels by ID

    Parameters
    ----------
    definition_files
        Files from which to load definitions

    Returns
    -------
    :
        Initialised [HorizontalLabel][]'s, each key is its ID
    """
    res = {}
    id_sources = {}
    for df in definition_files:
        with open(df) as fh:
            raw = json.load(fh)

        if raw["id"] in res:
            msg = f"{raw['id']} appears in both {id_sources[raw['id']]} and {df}"
            raise AssertionError(msg)
        else:
            id_sources[raw["id"]] = df

        hl = HorizontalLabel(
            id=raw["id"],
            validation_key=raw["validation-key"],
            ui_label=raw["ui-label"],
            description=raw["description"],
        )

        res[raw["id"]] = hl

    return res


def get_variable_roots_by_id(
    definition_files: Iterable[Path],
) -> dict[str, VariableRoot]:
    """
    Get variable roots

    Parameters
    ----------
    definition_files
        Files from which to load definitions

    Returns
    -------
    :
        Initialised [VariableRoot][]'s, each key is an ID
    """
    res = {}
    id_sources = {}
    for df in definition_files:
        with open(df) as fh:
            raw = json.load(fh)

        if raw["id"] in res:
            msg = f"{raw['id']} appears in both {id_sources[raw['id']]} and {df}"
            raise AssertionError(msg)
        else:
            id_sources[raw["id"]] = df

        vr = VariableRoot(
            id=raw["id"],
            validation_key=raw["validation-key"],
            ui_label=raw["ui-label"],
            data_type=raw["data-type"],
            standard_name=raw["standard-name"],
        )

        res[raw["id"]] = vr

    return res


def get_variables_by_id(
    definition_files: Iterable[Path],
    horizontal_labels_by_id: dict[str, HorizontalLabel],
    variable_roots_by_id: dict[str, VariableRoot],
) -> dict[str, Variable]:
    """
    Get variables

    Parameters
    ----------
    definition_files
        Files from which to load definitions

    horizontal_labels_by_id
        Horizontal labels, keyed by ID

    variable_roots_by_id
        Variable roots, keyed by ID

    Returns
    -------
    :
        Initialised [Variable][]'s, each key is an ID
    """
    res = {}
    id_sources = {}
    for df in definition_files:
        with open(df) as fh:
            raw = json.load(fh)

        if raw["id"] in res:
            msg = f"{raw['id']} appears in both {id_sources[raw['id']]} and {df}"
            raise AssertionError(msg)
        else:
            id_sources[raw["id"]] = df

        horizontal_label = horizontal_labels_by_id[raw["horizontal-label"]]
        # try:
        #     horizontal_label = horizontal_labels_by_id[raw["horizontal-label"]]
        # except KeyError:
        #     print(f"Missing {raw['horizontal-label']} used by {raw['id']}")
        #     continue

        variable_root = variable_roots_by_id[raw["variable-root"]]
        # try:
        #     variable_root = variable_roots_by_id[raw["variable-root"]]
        # except KeyError:
        #     print(f"Missing {raw['variable-root']} used by {raw['id']}")
        #     continue

        cell_measures = raw["cell-measures"]
        # if cell_measures is None:
        #     print(f"cell_measures are None for {raw['id']}")
        #     continue

        variable_inst = Variable(
            id=raw["id"],
            validation_key=raw["validation-key"],
            ui_label=raw["ui-label"],
            description=raw["description"],
            area_label=raw["area-label"],
            cell_measures=cell_measures,
            cell_methods=raw["cell-methods"],
            # TODO: fix
            dimensions=" ".join(raw["dimensions"]),
            horizontal_label=horizontal_label,
            model_realm=raw["model-realm"],
            physical_parameter_name=raw["physical-parameter-name"],
            standard_name=raw["standard-name"],
            temporal_label=raw["temporal-label"],
            units=raw["units"],
            variable_root=variable_root,
            vertical_label=raw["vertical-label"],
        )

        res[raw["id"]] = variable_inst

    return res


def get_definition_files(dir: str) -> tuple[Path, ...]:
    """
    Get files which define values for a given 'facet'

    Parameters
    ----------
    dir
        Directory in `src-data` in which to find files

    Returns
    -------
    :
        Files defining the entries
    """
    return tuple(
        f
        for f in (REPO_ROOT / "src-data" / dir).glob("*.json")
        if f.name != "_context_"
    )


def main() -> None:
    """
    Read all the entries and build our SQL tables
    """
    db_file = Path("validation-database.db")
    # Start fresh every time
    if db_file.exists():
        db_file.unlink()

    sqlite_url = f"sqlite:///{db_file.as_posix()}"
    engine = create_engine(
        sqlite_url,
        # echo=True,
    )

    # Create all the tables
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        horizontal_labels = get_horizontal_labels_by_id(
            get_definition_files("horizontal-label")
        )
        session.add_all(horizontal_labels.values())

        variable_roots = get_variable_roots_by_id(get_definition_files("variable-root"))
        session.add_all(variable_roots.values())
        # breakpoint()
        variables = get_variables_by_id(
            get_definition_files("variable"),
            horizontal_labels_by_id=horizontal_labels,
            variable_roots_by_id=variable_roots,
        )
        session.add_all(variables.values())

        session.commit()

    # Once it's in a database, obviously way easier to read out too
    with Session(engine) as session:
        statement = select(Variable).where(
            # Hmmm, some special syntax needed probably
            Variable.variable_root_id == "tas",
        )

        result_exec = session.exec(statement)

        results = list(result_exec.all())
        print("Loaded results")
        print()
        for r in results:
            print(f"{r.model_dump()=}")
            print(f"{r.horizontal_label=}")
            print(f"{r.horizontal_label.description=}")
            print(f"{r.horizontal_label.validation_key=}")
            print(f"{r.variable_root=}")
            print(f"{r.variable_root.validation_key=}")
            print()

        statement = select(Variable)

        result_exec = session.exec(statement)

        results = list(result_exec.all())
        print(f"{set(v.variable_root.data_type for v in results)}")


if __name__ == "__main__":
    main()
