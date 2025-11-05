# Water Cycle Variables

Water cycle variables track water movement through atmosphere, land, and ocean.

## Precipitation

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `pr` | Total precipitation (rain + snow) | General climate studies, water balance |
| `prc` | Convective precipitation | Thunderstorm analysis, extreme weather |
| `prsn` | Snowfall only | Snow hydrology, winter climate |
| `prra` | Rainfall only | Tropical studies, flooding |

**Examples**:
```
pr_tavg-u-hxy-u        → Monthly average total precipitation
prc_tmax-u-hxy-u       → Daily maximum convective precipitation
prsn_tsum-u-hxy-u      → Monthly total snowfall
```

## Humidity

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `hus` | Specific humidity (atmospheric levels) | Weather modeling, moisture transport |
| `hurs` | Relative humidity at 2m | Weather analysis, human comfort |
| `prw` | Total atmospheric water vapor | Climate monitoring, weather forecasting |

**Examples**:
```
hus_tavg-al-hxy-air    → Monthly average humidity profile
hurs_tavg-h2m-hxy-u    → Monthly average surface humidity
prw_tavg-u-hxy-u       → Monthly average water vapor column
```

## Evaporation

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `evspsbl` | Total evapotranspiration | Water balance, drought studies |
| `evspsblsoi` | Soil evaporation only | Land surface modeling |
| `evspsblveg` | Plant transpiration | Ecosystem studies, agriculture |

**Examples**:
```
evspsbl_tavg-u-hxy-lnd → Monthly average total evapotranspiration
evspsblsoi_tavg-u-hxy-lnd → Monthly average soil evaporation
```

## Soil Moisture

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `mrso` | Total soil moisture | Drought monitoring, climate studies |
| `mrsos` | Surface soil moisture (top 10cm) | Satellite validation, quick response |
| `mrsol` | Soil moisture by layer | Detailed land modeling |

**Examples**:
```
mrso_tavg-u-hxy-lnd    → Monthly average total soil moisture
mrsos_tavg-u-hxy-lnd   → Monthly average surface soil moisture
mrsol_tavg-sl-hxy-lnd  → Monthly average soil moisture profile
```

## Runoff & Rivers

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `mrro` | Total runoff | River flow, flood forecasting |
| `mrros` | Surface runoff | Flash flooding, erosion |
| `mrrob` | Subsurface runoff | Groundwater discharge, baseflow |

**Examples**:
```
mrro_tavg-u-hxy-lnd    → Monthly average total runoff
mrros_tmax-u-hxy-lnd   → Daily maximum surface runoff
```

## Quick Selection Guide

**Need precipitation?** → Use `pr` for total, `prc` for storms, `prsn` for snow
**Need humidity?** → Use `hus` for atmospheric, `hurs` for surface conditions  
**Need evaporation?** → Use `evspsbl` for total, specific types for detailed studies
**Need soil water?** → Use `mrso` for drought, `mrsos` for quick response
**Need runoff?** → Use `mrro` for rivers, `mrros` for flooding

[Browse all water cycle variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)