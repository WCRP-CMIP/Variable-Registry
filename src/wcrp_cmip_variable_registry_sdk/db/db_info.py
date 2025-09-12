"""
Helper class for handling the database's information i.e. content
"""

from __future__ import annotations

from collections.abc import Iterable
from functools import partial
from pathlib import Path
from typing import Protocol, TypeVar

from pydantic import BaseModel

from wcrp_cmip_variable_registry_sdk.db.models import (
    HorizontalLabel,
    Variable,
    VariableRoot,
)


def get_definition_files(dir: str, source_root: Path) -> tuple[Path, ...]:
    """
    Get files which define values for a given 'model'

    Parameters
    ----------
    dir
        Directory in `source_root` in which to find files

    source_root
        Path to the root of the variable registry repository

    Returns
    -------
    :
        Files defining the entries for the given model
    """
    return tuple(
        f
        for f in (source_root / "src-data" / dir).glob("*.json")
        if f.name != "_context_"
    )


class Initialisable(Protocol):
    """
    A class we can initialise via [get_instances_by_id][]
    """

    @classmethod
    def from_source_json(cls, df: Path) -> Initialisable:
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


T = TypeVar("T", bound=Initialisable)
# Probably not the correct type hinting.
# We can fix this another day


def get_instances_by_id(
    definition_files: Iterable[Path], cls_to_initialise: type[T]
) -> dict[str, T]:
    """
    Get instances, keyed by ID

    Parameters
    ----------
    definition_files
        Files from which to load definitions

    cls_to_initialise
        Class to initialise

    Returns
    -------
    :
        Initialised `cls_to_initialise`'s, keyed by ID
    """
    res = {}
    id_sources = {}
    for df in definition_files:
        instance = cls_to_initialise.from_source_json(df)
        if instance.id in res:
            msg = f"{instance.id} is defined in both {id_sources[instance.id]} and {df}"
            raise AssertionError(msg)

        res[instance.id] = instance
        id_sources[instance.id] = df

    return res


class DBInfo(BaseModel):
    """
    Database information

    A convenience class for use while loading from source
    """

    horizontal_labels_by_id: dict[str, HorizontalLabel]
    """
    Horizontal labels, keyed by ID
    """

    variables_by_id: dict[str, Variable]
    """
    Variable, keyed by ID
    """

    variable_roots_by_id: dict[str, VariableRoot]
    """
    Variable roots, keyed by ID
    """

    @classmethod
    def from_source_root(cls, source_root: Path) -> DBInfo:
        """
        Initialise from the path to the root of the variable registry repository

        Parameters
        ----------
        source_root
            Path to the root of the variable registry repository

        Returns
        -------
        :
            Initialised [DBInfo][]
        """
        gdf = partial(get_definition_files, source_root=source_root)

        horizontal_labels_by_id = get_instances_by_id(
            gdf("horizontal-label"), HorizontalLabel
        )
        variable_roots_by_id = get_instances_by_id(gdf("variable-root"), VariableRoot)
        variables_by_id = get_instances_by_id(
            gdf("variable"),
            Variable,
            # horizontal_labels_by_id=horizontal_labels_by_id,
            # variable_roots_by_id=variable_roots_by_id,
        )
        # TODO: remove
        variables_by_id_keys = tuple(variables_by_id.keys())
        for k in variables_by_id_keys:
            if variables_by_id[k].cell_measures is None:
                variables_by_id.pop(k)

        return cls(
            horizontal_labels_by_id=horizontal_labels_by_id,
            variables_by_id=variables_by_id,
            variable_roots_by_id=variable_roots_by_id,
        )
