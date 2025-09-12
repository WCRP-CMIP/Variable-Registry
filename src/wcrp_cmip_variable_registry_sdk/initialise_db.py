"""
Database initialisation/generation
"""

from __future__ import annotations

from pathlib import Path

import sqlalchemy.engine.base
from sqlmodel import Session, SQLModel, create_engine

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

        session.add_all(
            (
                *db_info.horizontal_labels_by_id.values(),
                *db_info.variables.values(),
                *db_info.variable_roots.values(),
            )
        )

        session.commit()

    return engine
