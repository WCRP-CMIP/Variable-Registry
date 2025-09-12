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
from pathlib import Path
from typing import Iterable

from sqlmodel import Field, Session, SQLModel, create_engine

REPO_ROOT = Path(__file__).parents[1]


# Defining the classes in the same file like this also registers them with sqlmodl.
# Normally this is a not ideal pattern as you would rather have them registered on import.
# For now, it doesn't matter, but it will be better if/when we split this out into a package
# so we can put the class definitions into separate files.
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
    [TODO]
    """

    ui_label: str
    """
    Text to use for this label in user interfaces
    """

    description: str
    """
    Description of the meaning of this horizontal label
    """

    # auto-inject context and type on serialisation


def get_horizontal_labels(
    definition_files: Iterable[Path],
) -> tuple[HorizontalLabel, ...]:
    """
    Get horizontal labels

    Parameters
    ----------
    definition_files
        Files from which to load definitions

    Returns
    -------
    :
        Initialised [HorizontalLabel][]'s
    """
    res_l = []
    for df in definition_files:
        with open(df) as fh:
            raw = json.load(fh)

        hl = HorizontalLabel(
            id=raw["id"],
            validation_key=raw["validation-key"],
            ui_label=raw["ui-label"],
            description=raw["description"],
        )

        res_l.append(hl)

    res = tuple(res_l)

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
        horizontal_labels = get_horizontal_labels(
            get_definition_files("horizontal-label")
        )
        session.add_all(horizontal_labels)

        session.commit()


if __name__ == "__main__":
    main()
