# Common Patterns

## Role in CMIP Standardization

Common patterns represent the most frequently used variable constructions in CMIP, developed through community consensus and proven in operational use. These patterns provide:

- **Consistency** across modeling centers using similar approaches
- **Validation templates** for new variable development  
- **Best practices** established through CMIP experience
- **Efficiency** by reusing successful variable designs

Understanding these patterns accelerates CMIP variable development and ensures compatibility with existing community workflows.

## Pattern Structure Reminder

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
```


## Most Common Patterns

**Based on CMIP variable frequency analysis**:

| Pattern | Usage Frequency | Typical Domains | Example Variables |
|---------|----------------|-----------------|-------------------|
| `*_tavg-u-hxy-u` | 35% | All surface variables | `pr`, `ps`, `siconc`, `rsds` |
| `*_tavg-al-hxy-air` | 15% | 3D atmosphere | `ta`, `ua`, `hus` |
| `*_tavg-ol-hxy-sea` | 12% | 3D ocean | `thetao`, `so`, `uo` |
| `*_tavg-h2m-hxy-u` | 8% | Surface meteorology | `tas`, `hurs` |
| `*_tavg-u-hxy-lnd` | 7% | Land surface | `lai`, `gpp` |
| `*_tavg-u-hxy-sea` | 6% | Ocean surface | `tos`, `sos` |

## Pattern Selection Strategy

### For CMIP Variable Development

=== "Step 1: Domain Classification"

    **Identify the physical domain first**
    
    - **Atmosphere**: `air`, `u`, or height labels (`h2m`, `h10m`)
    - **Ocean**: `sea` area with ocean coordinates (`u`, `ol`)
    - **Land**: `lnd` area with surface or soil coordinates (`u`, `sl`)
    - **Global**: `u` area for variables spanning multiple domains

=== "Step 2: Dimensionality Matching"

    **Match vertical structure to data dimensionality**
    
    - **2D Surface**: `u` (most common)
    - **3D Atmosphere**: `al` (full profiles), `p19`/`p39` (standard levels)  
    - **3D Ocean**: `ol` (full profiles), specific depths (`d100m`, `d1000m`)
    - **Soil Profiles**: `sl` (all soil levels)
    - **Specific Heights**: `h2m`, `h10m` (standard reference levels)

=== "Step 3: Temporal Requirements"

    **Choose based on scientific application**
    
    - **Climate studies**: `tavg` (95% of CMIP variables)
    - **Extreme analysis**: `tmax`, `tmin`
    - **Weather applications**: `tpt` (instantaneous)
    - **Budget calculations**: `tsum` (accumulated totals)

=== "Step 4: Spatial Processing"

    **Almost always `hxy` for CMIP gridded output**
    
    - **Standard output**: `hxy` (regular lat-lon grid)
    - **Global monitoring**: `hm` (Earth system indicators)
    - **Circulation studies**: `hy` (zonal means)



## Domain-Specific Patterns

=== "Atmospheric Variables"

    ### Surface Meteorology
    **Standard patterns for near-surface atmospheric conditions**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **2m Temperature** | `tas_[time]-h2m-hxy-u` | `tas_tavg-h2m-hxy-u` | Climate monitoring |
    | **2m Humidity** | `hurs_[time]-h2m-hxy-u` | `hurs_tavg-h2m-hxy-u` | Comfort indices |
    | **10m Wind** | `sfcWind_[time]-h10m-hxy-u` | `sfcWind_tavg-h10m-hxy-u` | Wind energy |
    | **Surface Pressure** | `ps_[time]-u-hxy-u` | `ps_tavg-u-hxy-u` | Weather systems |

    ### 3D Atmosphere
    **Patterns for full atmospheric profiles**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Temperature** | `ta_[time]-al-hxy-air` | `ta_tavg-al-hxy-air` | Atmospheric heating |
    | **Wind Components** | `[u/v]a_[time]-al-hxy-air` | `ua_tavg-al-hxy-air` | Circulation studies |
    | **Humidity** | `hus_[time]-al-hxy-air` | `hus_tavg-al-hxy-air` | Water cycle |
    | **Vertical Motion** | `wap_[time]-al-hxy-air` | `wap_tavg-al-hxy-air` | Convection analysis |

=== "Ocean Variables"

    ### Ocean Surface
    **Patterns for sea surface properties**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Sea Surface Temperature** | `tos_[time]-u-hxy-sea` | `tos_tavg-u-hxy-sea` | Climate indices |
    | **Sea Surface Salinity** | `sos_[time]-u-hxy-sea` | `sos_tavg-u-hxy-sea` | Water cycle |
    | **Sea Surface Height** | `zos_[time]-u-hxy-sea` | `zos_tavg-u-hxy-sea` | Sea level rise |
    | **Heat Flux** | `hfds_[time]-u-hxy-sea` | `hfds_tavg-u-hxy-sea` | Ocean heat uptake |

    ### Ocean 3D
    **Patterns for full ocean depth profiles**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Ocean Temperature** | `thetao_[time]-ol-hxy-sea` | `thetao_tavg-ol-hxy-sea` | Heat content |
    | **Ocean Salinity** | `so_[time]-ol-hxy-sea` | `so_tavg-ol-hxy-sea` | Density structure |
    | **Ocean Velocity** | `[u/v]o_[time]-ol-hxy-sea` | `uo_tavg-ol-hxy-sea` | Circulation |
    | **Biogeochemistry** | `[o2/no3/po4]_[time]-ol-hxy-sea` | `o2_tavg-ol-hxy-sea` | Marine ecosystems |

=== "Precipitation Variables"

    ### Basic Precipitation
    **Standard precipitation variable patterns**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Total Precipitation** | `pr_[time]-u-hxy-u` | `pr_tavg-u-hxy-u` | Water balance |
    | **Convective Precipitation** | `prc_[time]-u-hxy-u` | `prc_tavg-u-hxy-u` | Storm systems |
    | **Snowfall** | `prsn_[time]-u-hxy-u` | `prsn_tavg-u-hxy-u` | Snow hydrology |
    | **Rainfall** | `prra_[time]-u-hxy-u` | `prra_tavg-u-hxy-u` | Liquid precipitation |

    ### Domain-Specific Precipitation
    **Precipitation patterns for specific regions**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Land Precipitation** | `pr_[time]-u-hxy-lnd` | `pr_tmax-u-hxy-lnd` | Agricultural impacts |
    | **Ocean Precipitation** | `pr_[time]-u-hxy-sea` | `pr_tavg-u-hxy-sea` | Ocean freshwater |

=== "Land Variables"

    ### Surface Land
    **Patterns for land surface processes**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Vegetation** | `[lai/gpp/npp]_[time]-u-hxy-lnd` | `lai_tavg-u-hxy-lnd` | Ecosystem monitoring |
    | **Carbon Pools** | `c[Veg/Soil]_[time]-u-hxy-lnd` | `cVeg_tavg-u-hxy-lnd` | Carbon cycle |
    | **Runoff** | `mrro_[time]-u-hxy-lnd` | `mrro_tavg-u-hxy-lnd` | Water resources |
    | **Evapotranspiration** | `evspsbl_[time]-u-hxy-lnd` | `evspsbl_tavg-u-hxy-lnd` | Water balance |

    ### Soil Layers
    **Patterns for subsurface land processes**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Soil Moisture** | `mrsol_[time]-sl-hxy-lnd` | `mrsol_tavg-sl-hxy-lnd` | Drought analysis |
    | **Soil Temperature** | `tsl_[time]-sl-hxy-lnd` | `tsl_tavg-sl-hxy-lnd` | Permafrost studies |

=== "Sea Ice Variables"

    ### Sea Ice Properties
    **Standard patterns for sea ice variables**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Ice Concentration** | `siconc_[time]-u-hxy-u` | `siconc_tavg-u-hxy-u` | Arctic monitoring |
    | **Ice Thickness** | `sithick_[time]-u-hxy-si` | `sithick_tavg-u-hxy-si` | Ice volume |
    | **Ice Velocity** | `si[u/v]_[time]-u-hxy-si` | `siu_tavg-u-hxy-si` | Ice dynamics |
    | **Ice Age** | `siage_[time]-u-hxy-si` | `siage_tavg-u-hxy-si` | Ice formation |

=== "Radiation Variables"

    ### Shortwave Radiation
    **Solar radiation patterns**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **Surface Downwelling** | `rsds_[time]-u-hxy-u` | `rsds_tavg-u-hxy-u` | Solar energy |
    | **Surface Upwelling** | `rsus_[time]-u-hxy-u` | `rsus_tavg-u-hxy-u` | Surface albedo |
    | **TOA Outgoing** | `rsut_[time]-u-hxy-u` | `rsut_tavg-u-hxy-u` | Planetary albedo |

    ### Longwave Radiation
    **Thermal radiation patterns**

    | Variable Type | Pattern | Example | CMIP Usage |
    |---------------|---------|---------|------------|
    | **TOA Outgoing** | `rlut_[time]-u-hxy-u` | `rlut_tavg-u-hxy-u` | Earth's energy budget |
    | **Surface Downwelling** | `rlds_[time]-u-hxy-u` | `rlds_tavg-u-hxy-u` | Surface energy |
    | **Surface Upwelling** | `rlus_[time]-u-hxy-u` | `rlus_tavg-u-hxy-u` | Surface emission |


## Quality Validation Checklist

### Before Adopting a Pattern

- **Physical consistency**: All components match variable domain
- **CMIP precedent**: Similar variables exist in CMIP archives  
- **Community validation**: Pattern reviewed by domain experts
- **Technical compatibility**: Works with CMIP data processing tools
- **Documentation completeness**: All components defined in registry

### Pattern Testing Workflow

1. **Build identifier** using [Variable Registry Explorer](../../web/branded-variable-builder.html)
2. **Validate physics** with domain experts
3. **Check registry** for existing similar variables
4. **Test workflows** with CMIP processing tools
5. **Document thoroughly** for community adoption

## Registry Resources

- **[Interactive Pattern Builder](../../web/branded-variable-builder.html)** - Build and test patterns
- **[Component Browser](../08_components/)** - Explore all available components  
- **[Variable Examples](examples.md)** - Detailed construction examples
- **[Registry Repository](https://github.com/WCRP-CMIP/Variable-Registry)** - Complete component definitions

---

*Pattern: root_temporal-vertical-horizontal-area with area going last*