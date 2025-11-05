# Land & Ecosystem Variables

Land variables measure terrestrial processes including vegetation, soil, and carbon cycling.

## Vegetation

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `lai` | Leaf area index | Vegetation monitoring, ecosystem modeling |
| `gpp` | Gross primary productivity | Photosynthesis, carbon uptake |
| `npp` | Net primary productivity | Plant growth, carbon storage |
| `fpc` | Foliage projective cover | Vegetation density, land cover |

**Examples**:
```
lai_tavg-u-hxy-lnd     → Monthly average leaf area
gpp_tavg-u-hxy-lnd     → Monthly average photosynthesis
npp_tavg-u-hxy-lnd     → Monthly average plant growth
```

## Soil & Hydrology

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `mrso` | Total soil moisture | Drought monitoring, agriculture |
| `mrsos` | Surface soil moisture | Satellite validation, quick response |
| `tsl` | Soil temperature | Permafrost, land-atmosphere coupling |
| `mrro` | Total runoff | River flow, flood forecasting |

**Examples**:
```
mrso_tavg-u-hxy-lnd    → Monthly average soil moisture
tsl_tavg-sl-hxy-lnd    → Monthly average soil temperature profile
mrro_tavg-u-hxy-lnd    → Monthly average runoff
```

## Carbon Cycle

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `cVeg` | Vegetation carbon | Forest biomass, carbon storage |
| `cSoil` | Soil carbon | Carbon sequestration, decomposition |
| `nep` | Net ecosystem productivity | Ecosystem carbon balance |
| `nbp` | Net biome productivity | Land carbon source/sink |

**Examples**:
```
cVeg_tavg-u-hxy-lnd    → Monthly average vegetation carbon
cSoil_tavg-u-hxy-lnd   → Monthly average soil carbon
nep_tavg-u-hxy-lnd     → Monthly average ecosystem carbon flux
```

## Energy & Water Balance

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `evspsbl` | Total evapotranspiration | Water balance, drought |
| `hfls` | Latent heat flux | Energy balance, evaporation |
| `hfss` | Sensible heat flux | Surface heating, temperature |

**Examples**:
```
evspsbl_tavg-u-hxy-lnd → Monthly average evapotranspiration
hfls_tavg-u-hxy-lnd    → Monthly average latent heat
```

## Land Use & Cover

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `cropFrac` | Crop fraction | Agriculture, food security |
| `grassFrac` | Grass fraction | Pasture, rangeland |
| `treeFrac` | Tree fraction | Forest cover, deforestation |
| `baresoilFrac` | Bare soil fraction | Desertification, erosion |

**Examples**:
```
cropFrac_tavg-u-hxy-u  → Monthly average crop coverage
treeFrac_tavg-u-hxy-lnd → Monthly average forest coverage
```

## Quick Selection Guide

**Need vegetation status?** → Use `lai` for greenness, `gpp`/`npp` for productivity
**Need soil information?** → Use `mrso` for water, `tsl` for temperature, `cSoil` for carbon
**Need water balance?** → Use `evspsbl` for evaporation, `mrro` for runoff
**Need carbon cycling?** → Use `cVeg`/`cSoil` for storage, `nep`/`nbp` for fluxes
**Need land cover?** → Use specific fraction variables like `cropFrac`, `treeFrac`

[Browse all land variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)