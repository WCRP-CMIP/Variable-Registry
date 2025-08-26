# Horizontal Labels

**Horizontal labels** define how climate variables are distributed, processed, or aggregated in horizontal space within CMIP model outputs. They are the **fourth component** in branded identifiers.

## Role in CMIP

Horizontal representation is crucial for CMIP model comparison because climate models use different grid resolutions, coordinate systems, and analysis methods. The same physical process can be represented as:
- **Full spatial fields** for detailed regional analysis
- **Zonal averages** for circulation studies  
- **Global means** for monitoring Earth system changes
- **Cross-sections** for specific process investigations

Horizontal labels ensure that all CMIP models provide data with consistent spatial processing and representation.

### Why Horizontal Labels Matter

Different horizontal representations serve different scientific needs:
- **Gridded fields** (`hxy`) preserve spatial patterns for regional impacts
- **Global means** (`hm`) track Earth system energy and mass budgets
- **Zonal means** (`hy`) reveal atmospheric and oceanic circulation patterns
- **Cross-sections** (`hys`, `ht`) examine specific transport processes

This standardization enables direct comparison of spatial analysis methods across different climate models.

## Pattern Position

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
                                                   ↑
                                              Horizontal position
```

## Common Horizontal Labels

=== "Gridded Data"

    **Full spatial resolution data:**

    | Label | Description | Spatial Structure | Example Usage |
    |-------|-------------|-------------------|---------------|
    | **`hxy`** | Regular lat-lon grid | Full 2D spatial field | `tas_tavg-h2m-hxy-u` |
    | **`hxys`** | Site/station data | Point locations | `tas_tpt-h2m-hxys-u` |

=== "Spatial Averages"

    **Aggregated spatial representations:**

    | Label | Description | Spatial Structure | Example Usage |
    |-------|-------------|-------------------|---------------|
    | **`hm`** | Global mean | Single value per time | `co2_tavg-u-hm-u` |
    | **`hy`** | Zonal mean | Latitude-dependent | `ta_tavg-p39-hy-air` |

=== "Cross-Sections"

    **Specific spatial slices for process studies:**

    | Label | Description | Spatial Structure | Example Usage |
    |-------|-------------|-------------------|---------------|
    | **`hys`** | Meridional section | Latitude-depth/height | `thetao_tavg-ol-hys-sea` |
    | **`ht`** | Transect/path | Along specific route | `tos_tpt-u-ht-sea` |

## Selection Guide

### By Analysis Purpose
- **Regional impacts** → `hxy` (preserve spatial detail)
- **Global monitoring** → `hm` (Earth system budgets)
- **Circulation studies** → `hy` (zonal patterns), `hys` (meridional transport)
- **Model validation** → Match observational structure (`hxys` for stations)
- **Process investigation** → `ht` (specific transects)

### By Computational Requirements
- **High resolution analysis** → `hxy` (full spatial detail)
- **Efficient storage** → `hm`, `hy` (reduced data volume)
- **Targeted analysis** → `hys`, `ht` (focused domains)

### By Scientific Domain
- **Atmospheric dynamics** → `hy` (zonal winds), `hxy` (storm tracks)
- **Ocean circulation** → `hys` (overturning), `hxy` (surface currents)
- **Land processes** → `hxy` (heterogeneous surface)
- **Global change** → `hm` (planetary averages)

## Physical Applications

### Atmospheric Science
```
✓ ua_tavg-p39-hy-air     # Zonal wind patterns (Hadley/jet stream)
✓ ta_tavg-al-hxy-air     # Temperature fields (heat waves, cold fronts)
✓ slp_tavg-u-hm-u        # Global mean sea level pressure (climate indices)
```

### Ocean Science
```
✓ thetao_tavg-ol-hys-sea # Meridional overturning circulation
✓ tos_tavg-u-hxy-sea     # Sea surface temperature patterns (El Niño)
✓ zostoga_tavg-u-hm-sea  # Global mean sea level rise
```

### Land Science
```
✓ mrsol_tavg-sl-hxy-lnd  # Soil moisture spatial patterns (drought)
✓ gpp_tavg-u-hm-lnd      # Global primary productivity (carbon cycle)
```

## CMIP Standard Grids

Most CMIP models provide `hxy` data on regular latitude-longitude grids:
- **Low resolution**: ~200-400 km (1-2 degrees)
- **Standard resolution**: ~100-200 km (0.5-1 degrees)  
- **High resolution**: ~25-50 km (0.25 degrees)

Zonal means (`hy`) typically use the same latitude resolution as the native model grid.

## Consistency Examples

### Valid Combinations
```
✓ tas_tavg-h2m-hxy-u     # Surface temperature on regular grid
✓ co2_tavg-u-hm-u        # Global mean CO₂ concentration
✓ ua_tavg-p19-hy-air     # Zonal mean winds at standard levels
✓ msftmz_tavg-ol-hys-sea # Meridional overturning streamfunction
```

### Physically Appropriate Choices
```
✓ Global budgets       → hm  (energy, water, carbon)
✓ Regional patterns    → hxy (precipitation, temperature extremes)
✓ Circulation studies  → hy  (westerlies), hys (overturning)
✓ Validation studies   → hxys (match station/buoy locations)
```

## Next Steps

- **[Browse all horizontal labels](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/horizontal-label)** in the registry
- **[Area labels →](area-label.md)**
- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)**

---

*Horizontal labels specify spatial processing for consistent CMIP model analysis.*