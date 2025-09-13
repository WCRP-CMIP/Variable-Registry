"""
Create entity relationship diagram(s) for the data in this repository

Note that these diagrams do not match the JSON in `src-data` exactly.
Most notably, in `src-data` it is common to set values as IDs
even though the key is not labelled as being an ID.
For example, in `src-data/variable`, entries have a "variable-root" key.
The value of this key is the ID of the variable root,
not the actual variable root (or its name/validation-key) itself.
We are considering whether to change this
or whether it has to be like this
because of the differences between JSON-LD and SQL.
"""

from pathlib import Path

from eralchemy import render_er
from eralchemy.cst import (
    dot_crowfoot,
    dot_digraph,
    dot_left_right,
    dot_star_primary,
    dot_star_underline,
    dot_top_down,
    reset_config,
)
from sqlalchemy.orm import declarative_base
from sqlmodel import SQLModel


def custom():
    """
    Set custom eralchemy settings
    """
    dot_star_primary()
    dot_digraph()


def main() -> None:
    """
    Create entity relationship diagram(s)
    """
    REPO_ROOT = Path(__file__).parents[1]

    Base = declarative_base()
    SQLModel.metadata = Base.metadata

    # Import the tables,
    # which has the side effect of binding them to SQLModel.metadata
    from wcrp_cmip_variable_registry_sdk.db.models import (  # noqa: F401
        HorizontalLabel,
        Variable,
        VariableRoot,
    )

    for settings, out_name in (
        (None, "er-default.pdf"),
        (dot_crowfoot, "er-crowfoot.pdf"),
        (dot_digraph, "er-digraph.pdf"),
        (dot_star_primary, "er-dot-star-primary.pdf"),
        (dot_star_underline, "er-dot-star-underline.pdf"),
        (dot_top_down, "er-dot-top-down.pdf"),
        (dot_left_right, "er-dot-left-right.pdf"),
        (custom, "er-custom.pdf"),
    ):
        reset_config()
        if settings is not None:
            settings()

        print(f"Rendering {out_name}")
        render_er(Base, str(REPO_ROOT / out_name))


if __name__ == "__main__":
    main()
