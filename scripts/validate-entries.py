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

from wcrp_cmip_variable_registry_sdk import initialise_sqlite_database_from_source_root


def main() -> None:
    """
    Validate the entries
    """
    REPO_ROOT = Path(__file__).parents[1]

    initialise_sqlite_database_from_source_root(
        REPO_ROOT,
        REPO_ROOT / "validation-database.db",
    )


if __name__ == "__main__":
    main()
