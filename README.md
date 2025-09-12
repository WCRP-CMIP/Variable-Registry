# Variable-Registry
!!! warning TESTING ONLY: 
    Contents of this repository are a work in progress and are likely to change drastically until this notice is removed. 

The CMIP Variable Registry provides standardized, unique identifiers for climate variables through a **Branded Identifier System**.


## Current contents
The testing version of the variable registry has been generated from the data request version 1.2.2, as exported by the CMIP7 Data Request Software Package: https://github.com/CMIP-Data-Request/CMIP7_DReq_Software/releases/tag/v1.2.2

If you see any inaccuracies, or mistakes, please flag these in the issues tab. 

## Documentation and WIKI location:
For further information or the documentation, visit https://wcrp-cmip.github.io/Variable-Registry/docs/

--- 


## What is a Branded Identifier?

A structured naming system that creates unique, self-documenting variable names:

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
```

### Examples

| Traditional Name | Branded Identifier | Meaning |
|------------------|-------------------|---------|
| "Surface temperature" | `tas_tavg-h2m-hxy-u` | Near-surface air temperature, time-averaged, at 2m height, gridded, unmasked |
| "Sea temperature" | `tos_tavg-u-hxy-sea` | Sea surface temperature, time-averaged, surface, gridded, over sea |
| "Heat flux" | `hfds_tavg-u-hxy-sea` | Downward heat flux, time-averaged, surface, gridded, over sea |

## Interactive Explorer

Build and validate variable identifiers using the 

[Variable Registry Explorer](https://wcrp-cmip.github.io/Variable-Registry/docs/variable-builder.html){ .md-button }.



Try with examples:

- [hfds_tavg-u-hxy-sea](https://wcrp-cmip.github.io/Variable-Registry/docs/variable-builder.html?branding=hfds_tavg-u-hxy-sea)

- [tas_tavg-h2m-hxy-u](https://wcrp-cmip.github.io/Variable-Registry/docs/variable-builder.html?branding=tas_tavg-h2m-hxy-u)

- [abs550aer_tavg-u-hxy-u](https://wcrp-cmip.github.io/Variable-Registry/docs/variable-builder.html?branding=abs550aer_tavg-u-hxy-u)

## Quick Start

1. **[What is a branded identifier?](https://wcrp-cmip.github.io/Variable-Registry/docs/branded-identifier/01-what-is-branded-identifier/)** - Learn the basics
2. **[How to construct](https://wcrp-cmip.github.io/Variable-Registry/docs/branded-identifier/02_How%20to%20Construct/01_general_structure/)** - Step-by-step guide  
3. **[Root variables](https://wcrp-cmip.github.io/Variable-Registry/docs/branded-identifier/04_root-variables/01_what_is_a_root_variable/)** - Available variables
4. **[Components](https://wcrp-cmip.github.io/Variable-Registry/docs/branded-identifier/05_what_are_the_components/)** - Component reference

## Registry Contents

- **620+ Root Variables** across all climate domains
- **Complete component definitions** for temporal, vertical, horizontal, and area labels
- **Validation system** ensuring physical consistency
- **Interactive tools** for building and exploring variables

## Repository Structure

- **`src-data/`** - Source data files for all components (data)
- **`docs/`** - Documentation (this site) 
- **`Variable-Registry_<name>.json/`** - Summary files for the data in src-data. For a user-friendly version of these, view the documentation, followed by selecting data-content from the menu. 

## External Resources

- **[GitHub Repository](https://github.com/WCRP-CMIP/Variable-Registry)**
- **[CMIP Website](https://www.wcrp-cmip.org)**

## Software developer kit (SDK)

This repository also includes an SDK.
It is found in `src`.

**Key info :**
[![Main branch: supported Python versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FWCRP-CMIP%2FVariable-Registry%2Fmain%2Fpyproject.toml)](https://github.com/WCRP-CMIP/Variable-Registry/blob/main/pyproject.toml)
[![Licence](https://img.shields.io/pypi/l/wcrp-cmip-variable-registry-sdk?label=licence)](https://github.com/WCRP-CMIP/Variable-Registry/blob/main/LICENCE)

**PyPI :**
[![PyPI](https://img.shields.io/pypi/v/wcrp-cmip-variable-registry-sdk.svg)](https://pypi.org/project/wcrp-cmip-variable-registry-sdk/)
[![PyPI install](https://github.com/WCRP-CMIP/Variable-Registry/actions/workflows/install-pypi.yaml/badge.svg?branch=main)](https://github.com/WCRP-CMIP/Variable-Registry/actions/workflows/install-pypi.yaml)

**Tests :**
[![CI](https://github.com/WCRP-CMIP/Variable-Registry/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/WCRP-CMIP/Variable-Registry/actions/workflows/ci.yaml)
[![Coverage](https://codecov.io/gh/WCRP-CMIP/Variable-Registry/branch/main/graph/badge.svg)](https://codecov.io/gh/WCRP-CMIP/Variable-Registry)

**Other info :**
[![Last Commit](https://img.shields.io/github/last-commit/WCRP-CMIP/Variable-Registry.svg)](https://github.com/WCRP-CMIP/Variable-Registry/commits/main)
[![Contributors](https://img.shields.io/github/contributors/WCRP-CMIP/Variable-Registry.svg)](https://github.com/WCRP-CMIP/Variable-Registry/graphs/contributors)

### Status

<!---

We recommend having a status line in your repo
to tell anyone who stumbles on your repository where you're up to.
Some suggested options:

- prototype: the project is just starting up and the code is all prototype
- development: the project is actively being worked on
- finished: the project has achieved what it wanted
  and is no longer being worked on, we won't reply to any issues
- dormant: the project is no longer worked on
  but we might come back to it,
  if you have questions, feel free to raise an issue
- abandoned: this project is no longer worked on
  and we won't reply to any issues
-->

- development: the project is actively being worked on

<!--- --8<-- [end:description] -->

### Installation

<!--- --8<-- [start:installation] -->
#### As an application

If you want to use WCRP-CMIP Variable Registry SDK as an application,
then we recommend using the 'locked' version of the package.
This version pins the version of all dependencies too,
which reduces the chance of installation issues
because of breaking updates to dependencies.

The locked version of WCRP-CMIP Variable Registry SDK can be installed with

=== "pip"
    ```sh
    pip install 'wcrp-cmip-variable-registry-sdk[locked]'
    ```

#### As a library

If you want to use WCRP-CMIP Variable Registry SDK as a library,
for example you want to use it
as a dependency in another package/application that you're building,
then we recommend installing the package with the commands below.
This method provides the loosest pins possible of all dependencies.
This gives you, the package/application developer,
as much freedom as possible to set the versions of different packages.
However, the tradeoff with this freedom is that you may install
incompatible versions of WCRP-CMIP Variable Registry SDK's dependencies
(we cannot test all combinations of dependencies,
particularly ones which haven't been released yet!).
Hence, you may run into installation issues.
If you believe these are because of a problem in WCRP-CMIP Variable Registry SDK,
please [raise an issue](https://github.com/WCRP-CMIP/Variable-Registry/issues).

The (non-locked) version of WCRP-CMIP Variable Registry SDK can be installed with

=== "pip"
    ```sh
    pip install wcrp-cmip-variable-registry-sdk
    ```

#### For developers

For development, we rely on [uv](https://docs.astral.sh/uv/)
for all our dependency management.
To get started, you will need to make sure that uv is installed
([instructions here](https://docs.astral.sh/uv/getting-started/installation/)
(we found that the self-managed install was best,
particularly for upgrading uv later).

<!--- --8<-- [end:installation] -->

---

*Pattern: root_temporal-vertical-horizontal-area*
