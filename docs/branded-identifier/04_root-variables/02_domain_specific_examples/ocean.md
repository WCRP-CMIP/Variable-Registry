# Ocean Variables

Ocean variables measure physical and biogeochemical properties of seawater.

## Ocean Physics

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `tos` | Sea surface temperature | Climate monitoring, marine ecosystems |
| `thetao` | Ocean potential temperature | Ocean modeling, heat content |
| `so` | Ocean salinity | Ocean circulation, water masses |
| `zos` | Sea surface height | Sea level rise, ocean dynamics |
| `uo` | Eastward ocean velocity | Current analysis, transport |
| `vo` | Northward ocean velocity | Ocean circulation, upwelling |

**Examples**:
```
tos_tavg-u-hxy-sea     → Monthly average sea surface temperature
so_tavg-ol-hxy-sea     → Monthly average salinity profile
uo_tavg-ol-hxy-sea     → Monthly average eastward currents
```

## Ocean Biogeochemistry

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `chl` | Chlorophyll concentration | Marine productivity, ecosystem health |
| `pp` | Primary productivity | Carbon cycle, fisheries |
| `o2` | Dissolved oxygen | Ocean health, dead zones |
| `no3` | Nitrate concentration | Nutrient cycles, productivity |
| `co3` | Carbonate ion | Ocean acidification |

**Examples**:
```
chl_tavg-d0m-hxy-sea   → Monthly average surface chlorophyll
pp_tavg-ol-hxy-sea     → Monthly average primary productivity
o2_tavg-ol-hxy-sea     → Monthly average oxygen concentration
```

## Ocean Carbon

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `fgco2` | Air-sea CO₂ flux | Carbon cycle, ocean uptake |
| `dissic` | Dissolved inorganic carbon | Ocean carbon content |
| `talk` | Total alkalinity | Ocean chemistry, acidification |

**Examples**:
```
fgco2_tavg-u-hxy-sea   → Monthly average CO₂ flux into ocean
dissic_tavg-ol-hxy-sea → Monthly average dissolved carbon
```

## Quick Selection Guide

**Need ocean temperature?** → Use `tos` for surface, `thetao` for full ocean
**Need ocean currents?** → Use `uo`+`vo` for horizontal flow, check vertical components
**Need marine biology?** → Use `chl` for plants, `pp` for productivity
**Need ocean chemistry?** → Use `o2` for oxygen, `no3` for nutrients, carbon variables for acidification

[Browse all ocean variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)