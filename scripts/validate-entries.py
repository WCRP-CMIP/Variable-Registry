"""
Validate entries in `src-data`

This uses [sqlmodel](https://sqlmodel.tiangolo.com/)
to build an SQL database from our entries.
Doing this validates that the links between entries are correct
e.g. unique IDs where there should be, no dangling links.
It also ensures that every entry matches a given schema
(which should also match context).
"""

from pathlib import Path

from sqlmodel import Session, select

from wcrp_cmip_variable_registry_sdk import initialise_sqlite_database_from_source_root
from wcrp_cmip_variable_registry_sdk.db.models import Variable


def main() -> None:
    """
    Validate the entries
    """
    REPO_ROOT = Path(__file__).parents[1]
    sqlite_db_path = REPO_ROOT / "validation-database.db"
    if sqlite_db_path.exists():
        sqlite_db_path.unlink()

    engine = initialise_sqlite_database_from_source_root(
        REPO_ROOT,
        sqlite_db_path,
    )

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
