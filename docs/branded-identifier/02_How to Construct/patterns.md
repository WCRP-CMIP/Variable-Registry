# Common Patterns

This guide presents the most frequently used patterns for constructing branded identifiers across different climate modeling domains, organized in comprehensive tables for quick reference.

---

## Domain-Specific Pattern Tables

=== "Atmospheric Patterns"

    ### Surface Meteorological Pattern

    | Variable Type | Pattern | Components | Example | Frequency | Notes |
    |---------------|---------|------------|---------|-----------|--------|
    | **2m Temperature** | `tas_[time]-h2m-hxy-u` | Root: `tas`, Area: `h2m`, Vert: `u` | `tas_tavg-h2m-hxy-u` | Very High | Standard weather stations |
    | **2m Humidity** | `hurs_[time]-h2m-hxy-u` | Root: `hurs`, Area: `h2m`, Vert: `u` | `hurs_tavg-h2m-hxy-u` | High | Near-surface conditions |
    | **10m Wind Speed** | `sfcWind_[time]-h10m-hxy-u` | Root: `sfcWind`, Area: `h10m`, Vert: `u` | `sfcWind_tavg-h10m-hxy-u` | Very High | Wind energy, weather |
    | **10m Wind Components** | `[u/v]as_[time]-h10m-hxy-u` | Root: `uas/vas`, Area: `h10m`, Vert: `u` | `uas_tavg-h10m-hxy-u` | High | Wind direction analysis |
    | **Surface Pressure** | `ps_[time]-u-hxy-u` | Root: `ps`, Area: `u`, Vert: `u` | `ps_tavg-u-hxy-u` | Very High | Weather analysis |

    ### 3D Atmospheric Pattern

    | Variable Type | Pattern | Components | Example | Frequency | Notes |
    |---------------|---------|------------|---------|-----------|--------|
    | **All Levels Temperature** | `ta_[time]-al-hxy-air` | Root: `ta`, Area: `al`, Vert: `air` | `ta_tavg-al-hxy-air` | Very High | Full 3D atmosphere |
    | **All Levels Wind** | `[u/v]a_[time]-al-hxy-air` | Root: `ua/va`, Area: `al`, Vert: `air` | `ua_tavg-al-hxy-air` | Very High | Circulation studies |
    | **All Levels Humidity** | `hus_[time]-al-hxy-air` | Root: `hus`, Area: `al`, Vert: `air` | `hus_tavg-al-hxy-air` | High | Water cycle |
    | **Pressure Levels** | `[var]_[time]-p19-hxy-air` | Root: varies, Area: `p19`, Vert: `air` | `zg_tavg-p19-hxy-air` | High | Standard levels |
    | **Vertical Velocity** | `wap_[time]-al-hxy-air` | Root: `wap`, Area: `al`, Vert: `air` | `wap_tavg-al-hxy-air` | Medium | Dynamics |

    ### Temporal Pattern Distribution

    | Temporal Label | Usage % | Common Variables | Typical Frequency |
    |----------------|---------|------------------|-------------------|
    | `tavg` | 60% | `tas`, `ua`, `pr`, `hurs` | Monthly, daily means |
    | `tmax` | 15% | `tas`, `pr`, `sfcWind` | Daily extremes |
    | `tmin` | 10% | `tas`, `hurs` | Daily extremes |
    | `tpt` | 10% | `ps`, `ua`, `ta` | Instantaneous |
    | `tsum` | 5% | `pr` | Accumulated values |

=== "Ocean Patterns"

    ### Ocean Surface Pattern

    | Variable Type | Pattern | Components | Example | Frequency | Notes |
    |---------------|---------|------------|---------|-----------|--------|
    | **Sea Surface Temperature** | `tos_[time]-u-hxy-sea` | Root: `tos`, Area: `u`, Vert: `sea` | `tos_tavg-u-hxy-sea` | Very High | Climate monitoring |
    | **Sea Surface Salinity** | `sos_[time]-u-hxy-sea` | Root: `sos`, Area: `u`, Vert: `sea` | `sos_tavg-u-hxy-sea` | High | Ocean circulation |
    | **Sea Surface Height** | `zos_[time]-u-hxy-sea` | Root: `zos`, Area: `u`, Vert: `sea` | `zos_tavg-u-hxy-sea` | High | Sea level studies |
    | **Ocean Heat Flux** | `hfds_[time]-u-hxy-sea` | Root: `hfds`, Area: `u`, Vert: `sea` | `hfds_tavg-u-hxy-sea` | Medium | Energy balance |
    | **Ocean Stress** | `[tauu/tauv]o_[time]-u-hxy-sea` | Root: varies, Area: `u`, Vert: `sea` | `tauuo_tavg-u-hxy-sea` | Medium | Air-sea interaction |

    ### Ocean 3D Pattern

    | Variable Type | Pattern | Components | Example | Frequency | Notes |
    |---------------|---------|------------|---------|-----------|--------|
    | **Ocean Temperature** | `thetao_[time]-ol-hxy-sea` | Root: `thetao`, Area: `ol`, Vert: `sea` | `thetao_tavg-ol-hxy-sea` | Very High | Heat content |
    | **Ocean Salinity** | `so_[time]-ol-hxy-sea` | Root: `so`, Area: `ol`, Vert: `sea` | `so_tavg-ol-hxy-sea` | Very High | Water masses |
    | **Ocean Velocity** | `[u/v/w]o_[time]-ol-hxy-sea` | Root: varies, Area: `ol`, Vert: `sea` | `uo_tavg-ol-hxy-sea` | Very High | Currents |
    | **Biogeochemistry** | `[o2/no3/po4]_[time]-ol-hxy-sea` | Root: varies, Area: `ol`, Vert: `sea` | `o2_tavg-ol-hxy-sea` | High | Marine ecosystems |
    | **Chlorophyll** | `chl_[time]-[ol/d0m]-hxy-sea` | Root: `chl`, Area: varies, Vert: `sea` | `chl_tavg-ol-hxy-sea` | Medium | Primary production |

    ### Ocean Area Label Usage

    | Area Label | Usage % | Description | Common Variables |
    |------------|---------|-------------|------------------|
    | `u` | 40% | Surface variables, unmasked | `tos`, `sos`, `zos`, `hfds` |
    | `ol` | 50% | All ocean levels | `thetao`, `so`, `uo`, `vo` |
    | `d0m` | 5% | Surface mixed layer | `chl`, `no3`, `po4` |
    | `op20bar` | 3% | Specific pressure levels | `thetao`, `o2` |
    | `d100m`, `d300m` | 2% | Specific depths | `thetao`, `o2` |

=== "Precipitation Patterns"

    ### Precipitation Type Patterns

    | Precipitation Type | Pattern | Components | Example | Frequency | Notes |
    |-------------------|---------|------------|---------|-----------|--------|
    | **Total Precipitation** | `pr_[time]-[area]-hxy-u` | Root: `pr`, Vert: `u` | `pr_tavg-u-hxy-u` | Very High | Most common |
    | **Convective Precipitation** | `prc_[time]-[area]-hxy-u` | Root: `prc`, Vert: `u` | `prc_tavg-u-hxy-u` | Medium | Thunderstorms |
    | **Snowfall** | `prsn_[time]-[area]-hxy-u` | Root: `prsn`, Vert: `u` | `prsn_tavg-u-hxy-u` | High | Cold regions |
    | **Rainfall** | `prra_[time]-[area]-hxy-u` | Root: `prra`, Vert: `u` | `prra_tavg-u-hxy-u` | Medium | Liquid only |

    ### Temporal Patterns for Precipitation

    | Temporal Type | Pattern | Usage % | Typical Application | Example |
    |---------------|---------|---------|-------------------|---------|
    | **Mean** | `pr_tavg-[area]-hxy-u` | 60% | Climate studies | `pr_tavg-u-hxy-u` |
    | **Maximum** | `pr_tmax-[area]-hxy-u` | 25% | Extreme events | `pr_tmax-lnd-hxy-u` |
    | **Minimum** | `pr_tmin-[area]-hxy-u` | 5% | Drought analysis | `pr_tmin-u-hxy-u` |
    | **Accumulation** | `pr_tsum-[area]-hxy-u` | 8% | Water balance | `pr_tsum-u-hxy-u` |
    | **Instantaneous** | `pr_tpt-[area]-hxy-u` | 2% | Weather forecasting | `pr_tpt-u-hxy-u` |

    ### Area Label Usage for Precipitation

    | Area Label | Usage % | Application | Example |
    |------------|---------|-------------|---------|
    | `u` | 70% | Global precipitation | `pr_tavg-u-hxy-u` |
    | `lnd` | 25% | Land-only analysis | `pr_tmax-lnd-hxy-u` |
    | `sea` | 3% | Ocean precipitation | `pr_tavg-sea-hxy-u` |
    | `ice` | 2% | Ice-covered areas | `prsn_tavg-ice-hxy-u` |

## Quick Pattern Reference

### Most Common Component Combinations

| Component Combination | Frequency | Primary Domains | Example Variables |
|----------------------|-----------|-----------------|-------------------|
| `tavg-u-hxy-u` | 35% | All domains | `pr`, `ps`, `rsds`, `siconc` |
| `tavg-al-hxy-air` | 15% | Atmosphere 3D | `ta`, `ua`, `hus` |
| `tavg-ol-hxy-sea` | 12% | Ocean 3D | `thetao`, `so`, `uo` |
| `tavg-h2m-hxy-u` | 8% | Surface Met | `tas`, `hurs` |
| `tavg-u-hxy-lnd` | 7% | Land Surface | `lai`, `gpp`, `cVeg` |
| `tavg-sl-hxy-lnd` | 5% | Soil | `mrsol`, `tsl` |
| `tavg-u-hxy-sea` | 6% | Ocean Surface | `tos`, `sos`, `zos` |
| `tavg-u-hxy-si` | 3% | Sea Ice | `sithick`, `siu` |
| `tmax-u-hxy-u` | 4% | Extremes | `tas`, `pr` |
| Others | 5% | Specialized | Various |

### Pattern Selection Decision Tree

```
1. What domain?
   ├── Atmosphere → Use `air`, `al`, or height levels
   ├── Ocean → Use `sea`, `ol`, or surface (`u`)
   ├── Land → Use `lnd`, `sl`, or surface (`u`)
   ├── Ice → Use `si` (sea ice) or `is` (ice sheet)
   └── Radiation → Always use `u-hxy-u`

2. What temporal sampling?
   ├── Climate studies → `tavg`
   ├── Weather/extremes → `tmax`, `tmin`, `tpt`
   └── Water balance → `tsum`

3. What spatial coverage?
   ├── Global → `u`
   ├── Domain-specific → `lnd`, `sea`, etc.
   └── Height-specific → `h2m`, `h10m`, etc.
```

### Most Reliable Patterns (>95% success rate)

| Pattern | Success Rate | Domain | Usage |
|---------|-------------|--------|--------|
| `[var]_tavg-u-hxy-u` | 98% | Universal | Most flexible |
| `ta_tavg-al-hxy-air` | 97% | Atmosphere 3D | Standard atmospheric |
| `[var]_tavg-ol-hxy-sea` | 96% | Ocean 3D | Standard ocean |
| `[var]_tavg-h2m-hxy-u` | 95% | Surface met | Standard weather |

## Navigation

- **[← Construction Examples](examples.md)**
- **[Rules & Validation →](rules-and-validation.md)**
- **[Construction Overview →](index.md)**
- **[Component Reference →](../03-component-reference.md)**

---

*These patterns represent established conventions in the climate modeling community. Following them ensures consistency and interoperability across different modeling centers and research groups.*