"""
Data models used in our database
"""

# TODO: auto-generate this
from wcrp_cmip_variable_registry_sdk.db.models.horizontal_label import HorizontalLabel
from wcrp_cmip_variable_registry_sdk.db.models.variable import Variable
from wcrp_cmip_variable_registry_sdk.db.models.variable_root import VariableRoot

__all__ = [
    "HorizontalLabel",
    "Variable",
    "VariableRoot",
]
