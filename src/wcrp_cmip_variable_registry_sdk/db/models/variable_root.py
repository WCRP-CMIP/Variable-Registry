"""
Variable root
"""
# TODO: auto-generate this

# Do not use this, it breaks sqlmodel
# from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from wcrp_cmip_variable_registry_sdk.db.models.variable import Variable

REPO_ROOT = Path(__file__).parents[1]


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

    @classmethod
    def from_source_json(cls, df: Path) -> "VariableRoot":
        """
        Initialise from a source `.json` file

        Parameters
        ----------
        df
            Definition file from which to initialise

        Returns
        -------
        :
            Initialised instance
        """
        with open(df) as fh:
            raw = json.load(fh)

        res = cls(
            id=raw["id"],
            validation_key=raw["validation-key"],
            ui_label=raw["ui-label"],
            data_type=raw["data-type"],
            # TODO: update if we start using more cross-links
            standard_name=raw["standard-name"],
        )

        return res
