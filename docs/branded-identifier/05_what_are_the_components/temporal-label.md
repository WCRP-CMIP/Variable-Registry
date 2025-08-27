# Temporal Labels

**Temporal labels** define how climate variables are sampled, aggregated, or processed in time within CMIP model outputs. They are the **second component** in branded identifiers.

## Role in CMIP

Temporal processing is fundamental to climate model intercomparison. Different scientific applications require different temporal representations of the same physical variable. For example:
- **Climate change studies** need long-term averages (`tavg`)
- **Extreme event analysis** requires maximum/minimum values (`tmax`, `tmin`)
- **Weather prediction** uses instantaneous snapshots (`tpt`)
- **Water cycle studies** need accumulated totals (`tsum`)

Temporal labels ensure that all CMIP models provide data with consistent temporal processing, enabling direct comparison and analysis.

### Why Temporal Labels Matter

Without standardized temporal processing, "temperature" could mean:
- Model A: instantaneous values every 6 hours
- Model B: daily averages
- Model C: monthly means

Temporal labels eliminate this ambiguity by explicitly specifying the temporal treatment in the variable identifier.

## Pattern Position

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
                  ↑
             Temporal position
```

## Common Temporal Labels

=== "Time Aggregations"

    **Standard temporal averaging methods:**

    | Label | Description | Physical Meaning | Example Usage |
    |-------|-------------|------------------|---------------|
    | **`tavg`** | Time average | Mean value over period | `tas_tavg-h2m-hxy-u` |
    | **`tmax`** | Maximum in period | Peak value reached | `tas_tmax-h2m-hxy-u` |
    | **`tmin`** | Minimum in period | Lowest value reached | `tas_tmin-h2m-hxy-u` |
    | **`tsum`** | Sum over period | Accumulated total | `pr_tsum-u-hxy-u` |

=== "Instantaneous"

    **Point-in-time sampling:**

    | Label | Description | Physical Meaning | Example Usage |
    |-------|-------------|------------------|---------------|
    | **`tpt`** | Time point/snapshot | Instantaneous value | `ps_tpt-u-hxy-u` |
    | **`ti`** | Time invariant | Fixed/constant field | `orog_ti-u-hxy-u` |

=== "Climatological"

    **Long-term reference fields:**

    | Label | Description | Physical Meaning | Example Usage |
    |-------|-------------|------------------|---------------|
    | **`tclm`** | Climatological mean | Long-term average | `co2_tclm-u-hm-u` |
    | **`tclmdc`** | Diurnal cycle climatology | Daily cycle patterns | `tas_tclmdc-h2m-hxy-u` |

## Selection Guide

### By Variable Type
- **Intensive quantities** (temperature, pressure, concentrations) → `tavg`, `tmax`, `tmin`, `tpt`
- **Extensive quantities** (precipitation, fluxes, energy) → `tsum`, `tavg`
- **Fixed fields** (topography, land masks) → `ti`
- **Reference datasets** → `tclm`

### By Scientific Application
- **Climate monitoring** → `tavg` (monthly/seasonal means)
- **Extreme events** → `tmax`, `tmin` (heat waves, cold snaps)
- **Weather forecasting** → `tpt` (initial conditions)
- **Water balance** → `tsum` (precipitation, evaporation totals)
- **Model benchmarks** → `tclm` (climatological references)

### By Temporal Scale
- **Daily extremes** → `tmax`, `tmin`
- **Monthly statistics** → `tavg`, `tsum`
- **Annual cycles** → `tclmdc`
- **Climate normals** → `tclm`

## Physical Consistency Examples

### Valid Combinations
```
✓ tas_tavg-*      # Temperature averages (intensive)
✓ pr_tsum-*       # Precipitation totals (extensive) 
✓ pr_tmax-*       # Peak precipitation rates (intensive rate)
✓ ps_tpt-*        # Instantaneous pressure (intensive)
✓ orog_ti-*       # Fixed topography (time-invariant)
```

### Physically Meaningless
```
❌ ps_tsum-*      # Pressure "totals" are undefined
❌ tas_tsum-*     # Temperature "totals" have no meaning
❌ co2_tmax-*     # CO₂ "maximum" lacks context without specification
```

## Next Steps

- **[Browse all temporal labels](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/temporal-label)** in the registry
- **[Vertical labels →](vertical-label.md)**
- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)**

---

*Temporal labels ensure consistent time processing across CMIP model outputs.*