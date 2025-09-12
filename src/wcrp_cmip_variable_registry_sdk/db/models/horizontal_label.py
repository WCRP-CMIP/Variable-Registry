"""
Horizontal label
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

    @classmethod
    def from_source_json(cls, df: Path) -> "HorizontalLabel":
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
            description=raw["description"],
        )

        return res
