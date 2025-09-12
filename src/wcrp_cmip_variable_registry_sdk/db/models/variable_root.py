"""
Variable root
"""
# TODO: auto-generate this

# Do not use this, it breaks sqlmodel
# from __future__ import annotations

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
