# Wind & Pressure Variables

Atmospheric dynamics variables measure air movement and pressure systems.

## Wind Components

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `ua` | Eastward wind | Weather forecasting, atmospheric circulation |
| `va` | Northward wind | Storm tracking, climate dynamics |
| `sfcWind` | Surface wind speed | Wind energy, marine applications |
| `wap` | Vertical wind velocity | Convection studies, upwelling |

**Examples**:
```
ua_tavg-al-hxy-air     → Monthly average eastward wind profile
va_tpt-h10m-hxy-u      → Instant northward wind at 10m
sfcWind_tavg-h10m-hxy-u → Monthly average surface wind speed
```

## Pressure

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `ps` | Surface pressure | Weather analysis, storm tracking |
| `psl` | Sea level pressure | Climate indices, teleconnections |
| `pfull` | Pressure on model levels | Atmospheric modeling |

**Examples**:
```
ps_tpt-u-hxy-u         → Instant surface pressure
psl_tavg-u-hxy-u       → Monthly average sea level pressure
```

## Circulation Features

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `zg` | Geopotential height | Weather pattern analysis |
| `omega` | Vertical pressure velocity | Atmospheric dynamics |

**Examples**:
```
zg_tavg-p19-hxy-air    → Monthly average geopotential heights
omega_tavg-al-hxy-air  → Monthly average vertical motion
```

## Quick Selection Guide

**Need wind direction/speed?** → Use `ua`+`va` for components, `sfcWind` for speed only
**Need pressure systems?** → Use `ps` for surface, `psl` for sea level comparison
**Need atmospheric circulation?** → Use `zg` for flow patterns, `omega` for vertical motion

[Browse all dynamics variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)