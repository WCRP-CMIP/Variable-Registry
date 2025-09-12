"""
Software developer kit for interacting with the WCRP-CMIP variable registry
"""

import importlib.metadata

from wcrp_cmip_variable_registry_sdk.initialise_db import (
    initialise_sqlite_database_from_source_root,
)

__version__ = importlib.metadata.version("wcrp_cmip_variable_registry_sdk")

__all__ = [
    "initialise_sqlite_database_from_source_root",
]
