# Ice & Snow Variables

Cryosphere variables measure ice and snow across sea ice, land ice, and snow cover.

## Sea Ice

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `siconc` | Sea ice concentration (area fraction) | Arctic/Antarctic monitoring, shipping |
| `sithick` | Sea ice thickness | Ice volume, climate trends |
| `sivol` | Sea ice volume per area | Total ice amount |
| `sisnthick` | Snow thickness on sea ice | Ice energy balance |

**Examples**:
```
siconc_tavg-u-hxy-u    → Monthly average sea ice concentration
sithick_tavg-u-hxy-si  → Monthly average ice thickness
sivol_tavg-u-hxy-si    → Monthly average ice volume
```

## Land Ice (Glaciers & Ice Sheets)

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `lithk` | Land ice thickness | Ice sheet modeling, sea level |
| `licalvf` | Land ice calving flux | Ice loss to ocean |
| `limass` | Land ice mass | Total ice storage |
| `acabf` | Land ice surface mass balance | Ice gain/loss at surface |

**Examples**:
```
lithk_tavg-u-hxy-is    → Monthly average ice sheet thickness
licalvf_tavg-u-hxy-is  → Monthly average ice calving
acabf_tavg-u-hxy-is    → Monthly average surface mass balance
```

## Snow Cover

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `snd` | Snow depth | Snow hydrology, water resources |
| `snw` | Snow amount (water equivalent) | Water storage, flood forecasting |
| `snc` | Snow area fraction | Snow cover monitoring |
| `tsn` | Snow temperature | Energy balance, melting |

**Examples**:
```
snd_tavg-u-hxy-lnd     → Monthly average snow depth
snw_tavg-u-hxy-lnd     → Monthly average snow water equivalent
snc_tavg-u-hxy-u       → Monthly average snow coverage
```

## Ice Energy & Mass Balance

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `hfdsn` | Heat flux through snow | Snow melt modeling |
| `snm` | Snow melt | Runoff prediction, hydrology |
| `sbl` | Snow sublimation | Water balance, energy |
| `esn` | Snow evaporation | Arctic studies, mass balance |

**Examples**:
```
hfdsn_tavg-u-hxy-sn    → Monthly average heat flux through snow
snm_tavg-u-hxy-lnd     → Monthly average snow melt
```

## Quick Selection Guide

**Need sea ice extent?** → Use `siconc` for area coverage
**Need sea ice volume?** → Use `sithick` for thickness, `sivol` for total volume
**Need ice sheet changes?** → Use `lithk` for thickness, `acabf` for mass balance
**Need snow information?** → Use `snd` for depth, `snw` for water equivalent
**Need ice energy balance?** → Use heat flux variables like `hfdsn`

## Common Applications

**Climate Monitoring**:
```
siconc_tavg-u-hxy-u    → Arctic/Antarctic ice extent trends
snc_tavg-u-hxy-u       → Northern hemisphere snow cover
```

**Sea Level Studies**:
```
lithk_tavg-u-hxy-is    → Ice sheet thickness changes
licalvf_tavg-u-hxy-is  → Ice discharge to ocean
```

**Water Resources**:
```
snd_tavg-u-hxy-lnd     → Mountain snowpack
snw_tmax-u-hxy-lnd     → Peak snow water equivalent
```

**Arctic Studies**:
```
sithick_tavg-u-hxy-si  → Sea ice thickness trends
sisnthick_tavg-u-hxy-si → Snow on ice thickness
```

[Browse all ice & snow variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)