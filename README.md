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
[Variable Registry Explorer](web/branded-variable-builder.html){ .md-button }.


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

- **`src-data/`** - Source data files for all components (data)
- **`docs/`** - Documentation (this site) 
- **`Variable-Registry_<name>.json/`** - Summary files for the data in src-data. For a user-friendly version of these, view the documentation, followed by selecting data-content from the menu. 

## External Resources

- **[GitHub Repository](https://github.com/WCRP-CMIP/Variable-Registry)**
- **[CMIP Website](https://www.wcrp-cmip.org)**

---

*Pattern: root_temporal-vertical-horizontal-area*
