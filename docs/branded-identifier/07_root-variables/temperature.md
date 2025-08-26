# Temperature Variables

Temperature variables measure heat in the atmosphere, ocean, and land systems.

## Atmosphere

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `tas` | Air temperature at 2m height | Weather monitoring, climate studies |
| `ts` | Surface skin temperature | Satellite data, energy balance |
| `ta` | Air temperature at all levels | Weather prediction, atmospheric modeling |

**Examples**:
```
tas_tavg-h2m-hxy-u     → Monthly average air temperature
ts_tavg-u-hxy-u        → Monthly average surface temperature
ta_tpt-al-hxy-air      → Instant atmospheric temperature profile
```

## Ocean

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `tos` | Sea surface temperature | Climate monitoring, marine ecosystems |
| `thetao` | Ocean temperature (all depths) | Ocean modeling, heat content |
| `to` | In-situ ocean temperature | Observational data |

**Examples**:
```
tos_tavg-u-hxy-sea     → Monthly average sea surface temperature
thetao_tavg-ol-hxy-sea → Monthly average ocean temperature profile
```

## Land & Ice

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `tsl` | Soil temperature | Land modeling, permafrost studies |
| `tsn` | Snow temperature | Snow hydrology, avalanche research |

**Examples**:
```
tsl_tavg-sl-hxy-lnd    → Monthly average soil temperature
tsn_tavg-u-hxy-sn      → Monthly average snow temperature
```

## Heat & Energy

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `hfds` | Downward heat flux at sea surface | Ocean heat uptake |
| `hfls` | Surface latent heat flux | Energy balance studies |
| `hfss` | Surface sensible heat flux | Land-atmosphere coupling |

**Examples**:
```
hfds_tavg-u-hxy-sea    → Monthly average ocean heat flux
hfls_tavg-u-hxy-u      → Monthly average latent heat flux
```

## Quick Selection Guide

**Need air temperature?** → Use `tas` for 2m height or `ta` for atmospheric profiles
**Need ocean temperature?** → Use `tos` for surface or `thetao` for full ocean
**Need surface temperature?** → Use `ts` for all surfaces (land, ocean, ice)
**Need soil temperature?** → Use `tsl` for subsurface temperatures

[Browse all temperature variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)