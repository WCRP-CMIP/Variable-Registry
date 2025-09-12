"""
Test operations

This file is just there to help demonstrate the initial setup.
You will probably delete it early in the project.
"""

from wcrp_cmip_variable_registry_sdk.operations import add_two


def test_add_two():
    assert add_two(3.3, 4.4) == 7.7
