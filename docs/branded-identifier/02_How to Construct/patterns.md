# Common Patterns

Frequently used patterns for constructing branded identifiers across different climate domains.

## Pattern Reminder

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
```

## Domain-Specific Patterns

=== "Atmospheric"

    ### Surface Meteorology
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **2m Temperature** | `tas_[time]-h2m-hxy-u` | `tas_tavg-h2m-hxy-u` |
    | **2m Humidity** | `hurs_[time]-h2m-hxy-u` | `hurs_tavg-h2m-hxy-u` |
    | **10m Wind** | `sfcWind_[time]-h10m-hxy-u` | `sfcWind_tavg-h10m-hxy-u` |
    | **Surface Pressure** | `ps_[time]-u-hxy-u` | `ps_tavg-u-hxy-u` |

    ### 3D Atmosphere
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Temperature** | `ta_[time]-al-hxy-air` | `ta_tavg-al-hxy-air` |
    | **Wind Components** | `[u/v]a_[time]-al-hxy-air` | `ua_tavg-al-hxy-air` |
    | **Humidity** | `hus_[time]-al-hxy-air` | `hus_tavg-al-hxy-air` |
    | **Vertical Motion** | `wap_[time]-al-hxy-air` | `wap_tavg-al-hxy-air` |

=== "Ocean"

    ### Ocean Surface
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Sea Surface Temperature** | `tos_[time]-u-hxy-sea` | `tos_tavg-u-hxy-sea` |
    | **Sea Surface Salinity** | `sos_[time]-u-hxy-sea` | `sos_tavg-u-hxy-sea` |
    | **Sea Surface Height** | `zos_[time]-u-hxy-sea` | `zos_tavg-u-hxy-sea` |
    | **Heat Flux** | `hfds_[time]-u-hxy-sea` | `hfds_tavg-u-hxy-sea` |

    ### Ocean 3D
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Ocean Temperature** | `thetao_[time]-ol-hxy-sea` | `thetao_tavg-ol-hxy-sea` |
    | **Ocean Salinity** | `so_[time]-ol-hxy-sea` | `so_tavg-ol-hxy-sea` |
    | **Ocean Velocity** | `[u/v]o_[time]-ol-hxy-sea` | `uo_tavg-ol-hxy-sea` |
    | **Biogeochemistry** | `[o2/no3/po4]_[time]-ol-hxy-sea` | `o2_tavg-ol-hxy-sea` |

=== "Precipitation"

    ### Basic Precipitation
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Total Precipitation** | `pr_[time]-u-hxy-u` | `pr_tavg-u-hxy-u` |
    | **Convective Precipitation** | `prc_[time]-u-hxy-u` | `prc_tavg-u-hxy-u` |
    | **Snowfall** | `prsn_[time]-u-hxy-u` | `prsn_tavg-u-hxy-u` |
    | **Rainfall** | `prra_[time]-u-hxy-u` | `prra_tavg-u-hxy-u` |

    ### Domain-Specific Precipitation
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Land Precipitation** | `pr_[time]-u-hxy-lnd` | `pr_tmax-u-hxy-lnd` |
    | **Ocean Precipitation** | `pr_[time]-u-hxy-sea` | `pr_tavg-u-hxy-sea` |

=== "Land"

    ### Surface Land
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Vegetation** | `[lai/gpp/npp]_[time]-u-hxy-lnd` | `lai_tavg-u-hxy-lnd` |
    | **Carbon Pools** | `c[Veg/Soil]_[time]-u-hxy-lnd` | `cVeg_tavg-u-hxy-lnd` |
    | **Runoff** | `mrro_[time]-u-hxy-lnd` | `mrro_tavg-u-hxy-lnd` |
    | **Evapotranspiration** | `evspsbl_[time]-u-hxy-lnd` | `evspsbl_tavg-u-hxy-lnd` |

    ### Soil Layers
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Soil Moisture** | `mrsol_[time]-sl-hxy-lnd` | `mrsol_tavg-sl-hxy-lnd` |
    | **Soil Temperature** | `tsl_[time]-sl-hxy-lnd` | `tsl_tavg-sl-hxy-lnd` |

=== "Sea Ice"

    ### Sea Ice Properties
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Ice Concentration** | `siconc_[time]-u-hxy-u` | `siconc_tavg-u-hxy-u` |
    | **Ice Thickness** | `sithick_[time]-u-hxy-si` | `sithick_tavg-u-hxy-si` |
    | **Ice Velocity** | `si[u/v]_[time]-u-hxy-si` | `siu_tavg-u-hxy-si` |
    | **Ice Age** | `siage_[time]-u-hxy-si` | `siage_tavg-u-hxy-si` |

=== "Radiation"

    ### Shortwave Radiation
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Surface Downwelling** | `rsds_[time]-u-hxy-u` | `rsds_tavg-u-hxy-u` |
    | **Surface Upwelling** | `rsus_[time]-u-hxy-u` | `rsus_tavg-u-hxy-u` |
    | **TOA Outgoing** | `rsut_[time]-u-hxy-u` | `rsut_tavg-u-hxy-u` |

    ### Longwave Radiation
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **TOA Outgoing** | `rlut_[time]-u-hxy-u` | `rlut_tavg-u-hxy-u` |
    | **Surface Downwelling** | `rlds_[time]-u-hxy-u` | `rlds_tavg-u-hxy-u` |
    | **Surface Upwelling** | `rlus_[time]-u-hxy-u` | `rlus_tavg-u-hxy-u` |

=== "Heat Fluxes"

    ### Surface Heat Fluxes
    | Variable Type | Pattern | Example |
    |---------------|---------|---------|
    | **Latent Heat** | `hfls_[time]-u-hxy-u` | `hfls_tavg-u-hxy-u` |
    | **Sensible Heat** | `hfss_[time]-u-hxy-u` | `hfss_tavg-u-hxy-u` |
    | **Ocean Heat Flux** | `hfds_[time]-u-hxy-sea` | `hfds_tavg-u-hxy-sea` |

## Most Common Patterns

| Pattern | Frequency | Domains | Example Variables |
|---------|-----------|---------|-------------------|
| `*_tavg-u-hxy-u` | 35% | All | `pr`, `ps`, `siconc`, `rsds` |
| `*_tavg-al-hxy-air` | 15% | Atmosphere 3D | `ta`, `ua`, `hus` |
| `*_tavg-ol-hxy-sea` | 12% | Ocean 3D | `thetao`, `so`, `uo` |
| `*_tavg-h2m-hxy-u` | 8% | Surface Met | `tas`, `hurs` |
| `*_tavg-u-hxy-lnd` | 7% | Land Surface | `lai`, `gpp` |
| `*_tavg-u-hxy-sea` | 6% | Ocean Surface | `tos`, `sos` |

## Pattern Selection Guide

### For New Variables

1. **Domain first**: Choose appropriate area label
   - Atmosphere: `air`, `u`, or height (`h2m`, `h10m`)
   - Ocean: `sea`
   - Land: `lnd`
   - Global: `u`

2. **Vertical structure**: Match the data dimensionality
   - Surface: `u`
   - 3D atmosphere: `al`
   - 3D ocean: `ol` 
   - Soil layers: `sl`
   - Specific heights: `h2m`, `h10m`

3. **Temporal needs**: Choose sampling method
   - Climate studies: `tavg`
   - Extremes: `tmax`, `tmin`
   - Weather: `tpt`

4. **Horizontal**: Almost always `hxy` for gridded data

### Validation Checklist

✅ **Physical consistency**: Components match the variable domain  
✅ **Pattern exists**: Similar variables use this pattern  
✅ **File availability**: Check if similar files exist in registry  
✅ **Standard compliance**: Follows CMIP conventions  

## Interactive Tools

- **[Variable Registry Explorer](../web/branded-variable-builder.html)** - Build and validate patterns
- **[Component Browser](../08_components/)** - Explore all components
- **[Construction Guide](01_general_structure.md)** - Step-by-step instructions

---

*Pattern: root_temporal-vertical-horizontal-area*
