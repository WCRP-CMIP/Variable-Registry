# Variable Registry Documentation

## Overview

The CMIP Variable Registry provides standardized, unique identifiers for climate variables through a **Branded Identifier System**.

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

Build and validate variable identifiers using the [Variable Registry Explorer](web/branded-variable-builder.html).

Try with examples:
- [hfds_tavg-u-hxy-sea](web/branded-variable-builder.html?branding=hfds_tavg-u-hxy-sea)
- [tas_tavg-h2m-hxy-u](web/branded-variable-builder.html?branding=tas_tavg-h2m-hxy-u)
- [abs550aer_tavg-u-hxy-u](web/branded-variable-builder.html?branding=abs550aer_tavg-u-hxy-u)

## Quick Start

1. **[What is a branded identifier?](branded-identifier/01-what-is-branded-identifier.md)** - Learn the basics
2. **[How to construct](branded-identifier/02_How%20to%20Construct/01_general_structure.md)** - Step-by-step guide  
3. **[Root variables](branded-identifier/05-root-variables.md)** - Available variables
4. **[Components](branded-identifier/08_components/)** - Component reference

## Registry Contents

- **620+ Root Variables** across all climate domains
- **Complete component definitions** for temporal, vertical, horizontal, and area labels
- **Validation system** ensuring physical consistency
- **Interactive tools** for building and exploring variables

## Repository Structure

- **`src-data/`** - Source data files for all components
- **`docs/`** - Documentation (this site)
- **`docs/web/`** - Interactive web tools

## External Resources

- **[GitHub Repository](https://github.com/WCRP-CMIP/Variable-Registry)**
- **[CMIP Website](https://www.wcrp-cmip.org)**

---

*Pattern: root_temporal-vertical-horizontal-area*
