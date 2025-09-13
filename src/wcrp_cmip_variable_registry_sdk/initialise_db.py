"""
Database initialisation/generation
"""

from __future__ import annotations

from pathlib import Path

import sqlalchemy.engine.base
from sqlmodel import Session, SQLModel, create_engine, text

from wcrp_cmip_variable_registry_sdk.db import DBInfo


def initialise_sqlite_database_from_source_root(
    source_root: Path, sqlite_db_path: Path
) -> sqlalchemy.engine.base.Engine:
    """
    Initialise the database from variable registry source files

    Parameters
    ----------
    source_root
        Path to the root of the variable registry source

        TODO: support a URL here too

    sqlite_db_path
        Path to the SQLite database to initialise

    Returns
    -------
    :
        Engine that uses the initialised database
    """
    sqlite_url = f"sqlite:///{sqlite_db_path.as_posix()}"
    engine = create_engine(
        sqlite_url,
        # echo=True,
    )
    # Ensure that trying to add data which points to foreign keys
    # that don't exist will fail
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))

    # Make sure that the needed classes are registered by importing them
    from wcrp_cmip_variable_registry_sdk.db.models import (
        HorizontalLabel,
        Variable,
        VariableRoot,
    )

    HorizontalLabel, VariableRoot, Variable
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        db_info = DBInfo.from_source_root(source_root)

        tmp = list(db_info.variables_by_id.values())
        tmp_safe = []
        for v in tmp:
            if (
                v.variable_root_id in db_info.variable_roots_by_id
                and v.horizontal_label_id in db_info.horizontal_labels_by_id
            ):
                tmp_safe.append(v)
            else:
                print(f"Missing references for {v.validation_key}")

        print("")
        print(f"{len(tmp_safe)} variables will be included in the DB")
        print(
            f"{len(tmp) - len(tmp_safe)} variables have issues "
            "and will not be included in the DB"
        )
        print("")

        session.add_all(
            (
                *db_info.horizontal_labels_by_id.values(),
                *db_info.variable_roots_by_id.values(),
                *tmp_safe,
            )
        )

        session.commit()

    return engine
