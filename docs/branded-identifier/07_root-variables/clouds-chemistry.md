# Clouds & Chemistry Variables

Atmospheric composition and cloud variables measure air quality, greenhouse gases, and cloud properties.

## Cloud Properties

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `clt` | Total cloud fraction | Climate monitoring, radiation |
| `cl` | Cloud area fraction (3D) | Detailed cloud modeling |
| `clw` | Cloud liquid water content | Precipitation processes |
| `cli` | Cloud ice content | Cold cloud processes |

**Examples**:
```
clt_tavg-u-hxy-u       → Monthly average total cloud cover
cl_tavg-al-hxy-air     → Monthly average cloud fraction profile
clw_tavg-al-hxy-air    → Monthly average liquid water content
```

## Greenhouse Gases

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `co2` | Carbon dioxide concentration | Climate forcing, carbon cycle |
| `ch4` | Methane concentration | Greenhouse gas monitoring |
| `n2o` | Nitrous oxide concentration | Agricultural emissions |
| `o3` | Ozone concentration | Air quality, UV protection |

**Examples**:
```
co2_tavg-u-hm-u        → Monthly average global mean CO₂
ch4_tavg-al-hxy-air    → Monthly average methane profile
o3_tavg-h2m-hxy-u      → Monthly average surface ozone
```

## Aerosols (Particles)

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `od550aer` | Aerosol optical depth | Air quality, climate forcing |
| `abs550aer` | Aerosol absorption | Atmospheric heating effects |
| `mmrbc` | Black carbon mass mixing ratio | Air pollution, heating |
| `mmrdust` | Dust mass mixing ratio | Desert dust, transport |

**Examples**:
```
od550aer_tavg-u-hxy-u  → Monthly average aerosol optical depth
mmrbc_tavg-h2m-hxy-u   → Monthly average surface black carbon
mmrdust_tavg-al-hxy-air → Monthly average dust concentration profile
```

## Air Quality

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `no2` | Nitrogen dioxide | Urban pollution, vehicle emissions |
| `so2` | Sulfur dioxide | Industrial pollution, acid rain |
| `co` | Carbon monoxide | Combustion sources, air quality |
| `pm2p5` | Particulate matter (PM2.5) | Health impacts, air quality |

**Examples**:
```
no2_tavg-h2m-hxy-u     → Monthly average surface NO₂
pm2p5_tavg-h2m-hxy-u   → Monthly average surface PM2.5
co_tavg-h2m-hxy-u      → Monthly average surface carbon monoxide
```

## Chemical Species

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `oh` | Hydroxyl radical | Atmospheric oxidation capacity |
| `hno3` | Nitric acid | Atmospheric chemistry |
| `h2o` | Water vapor | Atmospheric chemistry, humidity |

**Examples**:
```
oh_tavg-al-hxy-air     → Monthly average OH radical concentration
hno3_tavg-al-hxy-air   → Monthly average nitric acid profile
```

## Quick Selection Guide

**Need cloud information?** → Use `clt` for total cover, `cl` for detailed 3D structure
**Need greenhouse gases?** → Use `co2` for climate, `ch4`/`n2o` for agriculture, `o3` for air quality
**Need air pollution?** → Use `no2`/`so2` for gases, `mmrbc`/`pm2p5` for particles
**Need aerosol effects?** → Use `od550aer` for visibility, `abs550aer` for heating
**Need atmospheric chemistry?** → Use specific chemical species like `oh`, `hno3`

## Common Applications

**Climate Studies**:
```
co2_tavg-u-hm-u        → Global CO₂ monitoring
clt_tavg-u-hxy-u       → Cloud feedback studies
od550aer_tavg-u-hxy-u  → Aerosol climate effects
```

**Air Quality**:
```
no2_tavg-h2m-hxy-u     → Urban pollution monitoring
pm2p5_tavg-h2m-hxy-u   → Health impact assessment
o3_tmax-h2m-hxy-u      → Ozone air quality standards
```

**Atmospheric Chemistry**:
```
oh_tavg-al-hxy-air     → Oxidation capacity studies
ch4_tavg-al-hxy-air    → Methane chemistry and transport
```

[Browse all atmospheric composition variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)