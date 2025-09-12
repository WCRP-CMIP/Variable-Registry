"""
Variable
"""
# TODO: auto-generate this

# Do not use this, it breaks sqlmodel
# from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from wcrp_cmip_variable_registry_sdk.db.models.horizontal_label import (
        HorizontalLabel,
    )
    from wcrp_cmip_variable_registry_sdk.db.models.variable_root import VariableRoot

REPO_ROOT = Path(__file__).parents[1]


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

    horizontal_label: "HorizontalLabel" = Relationship(back_populates="variables")
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

    variable_root: "VariableRoot" = Relationship(back_populates="variables")
    """
    Variable root associated with this variable
    """

    vertical_label: str  # TODO: make link
    """
    Vertical label associated with this variable
    """

    # auto-inject context and type on serialisation
