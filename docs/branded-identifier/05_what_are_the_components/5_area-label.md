# Area Labels

**Area labels** define the spatial coverage or domain masking applied to climate variables in CMIP. They are the **final component** in branded identifiers.

## Role in CMIP

Area labels are critical for CMIP model intercomparison because they ensure that variables are compared across consistent spatial domains. When comparing sea surface temperature from different models, for example, area labels guarantee that all models are reporting values specifically over ocean areas, not mixing ocean and land data.

### Why Area Labels Matter

In climate modeling, physical processes occur over specific surface types or atmospheric regions. A variable might be:
- **Physically meaningful** only over certain areas (e.g., sea ice thickness over sea ice)
- **Scientifically relevant** when isolated to specific domains (e.g., precipitation over land for agriculture)
- **Computationally defined** by model grid characteristics (e.g., atmospheric chemistry in air column)

Area labels prevent confusion and ensure scientific consistency across CMIP model outputs.

## Pattern Position

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
                                                                      ↑
                                                                Area goes last
```

## Common Area Labels

=== "Surface Types"

    **Most frequently used area labels for surface processes:**

    | Label | Description | Typical Variables |
    |-------|-------------|-------------------|
    | **`u`** | Unmasked/Global coverage | Global temperature, precipitation |
    | **`lnd`** | Land areas only | Soil moisture, vegetation, runoff |
    | **`sea`** | Ocean/sea areas only | Sea surface temperature, currents |
    | **`si`** | Sea ice regions | Ice thickness, concentration |
    | **`is`** | Ice sheet areas | Land ice, glacial processes |

=== "Atmospheric Regions"

    **Area labels for atmospheric and upper-level processes:**

    | Label | Description | Typical Variables |
    |-------|-------------|-------------------|
    | **`air`** | Atmospheric column | 3D wind fields, atmospheric chemistry |
    | **`ccl`** | Convective clouds | Cloud properties in convection |
    | **`scl`** | Stratiform clouds | Large-scale cloud processes |

=== "Specialized Domains"

    **Area labels for specific scientific applications:**

    | Label | Description | Typical Variables |
    |-------|-------------|-------------------|
    | **`crp`** | Crop areas | Agricultural variables |
    | **`ng`** | Natural grasslands | Ecosystem carbon fluxes |
    | **`tree`** | Forest areas | Forest carbon, phenology |
    | **`veg`** | Vegetated areas | Plant functional types |

## Selection Guide

### By Variable Domain
- **Global climate studies** → `u`
- **Land surface processes** → `lnd`
- **Ocean processes** → `sea`
- **Sea ice dynamics** → `si`
- **Ice sheet modeling** → `is`
- **Atmospheric chemistry** → `air`

### By Scientific Application
- **Climate model evaluation** → Match observational coverage (`sea`, `lnd`, `air`)
- **Impact assessments** → Domain-specific (`lnd` for agriculture, `sea` for marine)
- **Process studies** → Focused domains (`si` for ice, `ccl` for convection)

## Physical Consistency Examples

### Valid Combinations
```
✓ tos_tavg-u-hxy-sea     # Sea surface temp over ocean
✓ mrsol_tavg-sl-hxy-lnd  # Soil moisture over land
✓ siconc_tavg-u-hxy-si   # Sea ice over ice regions
✓ co2_tavg-al-hxy-air    # CO₂ in atmospheric column
```

### Invalid Combinations
```
❌ tos_tavg-u-hxy-lnd    # Sea temp over land (impossible)
❌ mrsol_tavg-sl-hxy-sea # Soil moisture over ocean (nonsensical)
❌ sithick_tavg-u-hxy-lnd # Sea ice thickness over land (wrong domain)
```

## Next Steps

- **[Browse all area labels](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/area-label)** in the registry
- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)**
- **[Component examples →](component-examples.md)**

---

*Area labels ensure variables are compared across consistent spatial domains in CMIP.*