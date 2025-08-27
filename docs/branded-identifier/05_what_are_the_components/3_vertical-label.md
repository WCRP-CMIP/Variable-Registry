# Vertical Labels

**Vertical labels** define the vertical coordinate system, level, or dimension for climate variables in CMIP model outputs. They are the **third component** in branded identifiers.

## Role in CMIP

Vertical coordinates are essential for CMIP model intercomparison because the same physical variable can exist at different heights, depths, or pressure levels. The atmosphere, ocean, and land surface all have complex vertical structure that models must represent consistently.

### Why Vertical Labels Matter

Different vertical levels serve different scientific purposes:
- **Surface observations** (2m temperature) for human-relevant conditions
- **Atmospheric profiles** (pressure levels) for weather and circulation
- **Ocean depths** (depth levels) for marine processes and heat storage
- **Soil layers** for land-atmosphere exchange

Vertical labels ensure that variables from different models represent the same vertical location or coordinate system.

## Pattern Position

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
                                   ↑
                              Vertical position
```

## Common Vertical Labels

=== "Surface & Near-Surface"

    **Standard reference levels for surface variables:**

    | Label | Description | Height/Depth | Example Usage |
    |-------|-------------|--------------|---------------|
    | **`u`** | Unspecified/surface | Surface level | `pr_tavg-u-hxy-u` |
    | **`h2m`** | 2 meters above surface | 2m height | `tas_tavg-h2m-hxy-u` |
    | **`h10m`** | 10 meters above surface | 10m height | `sfcWind_tavg-h10m-hxy-u` |
    | **`d0m`** | At surface | Sea surface | `tos_tavg-d0m-hxy-sea` |

=== "3D Coordinate Systems"

    **Full vertical profiles for process studies:**

    | Label | Description | Coordinate System | Example Usage |
    |-------|-------------|-------------------|---------------|
    | **`al`** | All atmospheric levels | Model atmospheric levels | `ta_tavg-al-hxy-air` |
    | **`ol`** | All ocean levels | Model ocean levels | `thetao_tavg-ol-hxy-sea` |
    | **`sl`** | All soil levels | Model soil levels | `mrsol_tavg-sl-hxy-lnd` |

=== "Standard Pressure Levels"

    **CMIP-standard pressure coordinates for atmospheric variables:**

    | Label | Description | Pressure Levels | Example Usage |
    |-------|-------------|-----------------|---------------|
    | **`p19`** | CMIP6 standard levels | 19 pressure levels | `ta_tavg-p19-hxy-air` |
    | **`p39`** | Extended pressure levels | 39 pressure levels | `ua_tavg-p39-hy-air` |
    | **`p1000`** | 1000 hPa level | Single pressure level | `hur_tavg-p1000-hxy-air` |

=== "Specific Depths"

    **Ocean depth coordinates:**

    | Label | Description | Ocean Depth | Example Usage |
    |-------|-------------|-------------|---------------|
    | **`d100m`** | 100m depth | Fixed depth | `thetao_tavg-d100m-hxy-sea` |
    | **`d1000m`** | 1000m depth | Deep ocean | `so_tavg-d1000m-hxy-sea` |

## Selection Guide

### By Model Component
- **Surface meteorology** → `h2m` (temperature), `h10m` (wind), `u` (precipitation)
- **Atmospheric dynamics** → `al` (full profiles), `p19`/`p39` (standard levels)
- **Ocean processes** → `ol` (full profiles), `d0m` (surface), `d100m`/`d1000m` (specific depths)
- **Land surface** → `u` (surface), `sl` (soil profiles)
- **Sea ice** → `u` (ice surface properties)

### By Scientific Application
- **Climate monitoring** → `h2m`, `d0m` (standard observation levels)
- **Weather prediction** → `p19`, `p39` (atmospheric profiles)
- **Ocean circulation** → `ol`, `d100m` (full ocean structure)
- **Land-atmosphere exchange** → `h2m`, `sl` (interface processes)
- **Carbon cycle** → `u`, `sl` (surface and soil carbon)

### By Data Requirements
- **Single level analysis** → `h2m`, `d0m`, `u`
- **Profile analysis** → `al`, `ol`, `sl`
- **Standard comparisons** → `p19` (atmospheric), `d100m` (ocean)
- **Process studies** → Domain-specific levels

## Physical Consistency Examples

### Valid Combinations
```
✓ tas_tavg-h2m-hxy-u     # Air temperature at 2m (surface meteorology)
✓ ta_tavg-al-hxy-air     # Temperature profiles (atmospheric dynamics)
✓ tos_tavg-u-hxy-sea     # Sea surface temperature (ocean surface)
✓ thetao_tavg-ol-hxy-sea # Ocean temperature profiles (ocean dynamics)
✓ mrsol_tavg-sl-hxy-lnd  # Soil moisture profiles (land hydrology)
```

### Physically Inconsistent
```
❌ tos_tavg-h2m-hxy-sea  # Sea surface temp at 2m height (impossible)
❌ tas_tavg-ol-hxy-air   # Air temperature at ocean levels (wrong domain)
❌ mrsol_tavg-al-hxy-lnd # Soil moisture at atmospheric levels (nonsensical)
```

## CMIP Standard Levels

The **p19** pressure levels (standard CMIP6 atmospheric levels):
1000, 925, 850, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 5, 1 hPa

These levels are specifically chosen to capture:
- **Boundary layer** (1000-850 hPa)
- **Free troposphere** (850-200 hPa) 
- **Upper troposphere/lower stratosphere** (200-50 hPa)
- **Middle stratosphere** (50-1 hPa)

## Next Steps

- **[Browse all vertical labels](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/vertical-label)** in the registry
- **[Horizontal labels →](4_horizontal-label.md)**
- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)**

---

*Vertical labels specify the level or coordinate system for consistent CMIP model comparison.*