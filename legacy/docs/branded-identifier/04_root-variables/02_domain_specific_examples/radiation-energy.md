# Radiation & Energy Variables

Radiation variables measure energy flows and the Earth's energy balance.

## Solar (Shortwave) Radiation

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `rsdt` | Top-of-atmosphere incoming solar | Earth's energy input, solar constant |
| `rsds` | Surface downwelling solar | Solar energy, surface heating |
| `rsus` | Surface upwelling solar | Surface albedo, reflection |
| `rsut` | Top-of-atmosphere outgoing solar | Planetary albedo, energy balance |

**Examples**:
```
rsdt_tavg-u-hxy-u      → Monthly average incoming solar radiation
rsds_tavg-u-hxy-u      → Monthly average surface solar radiation
rsus_tavg-u-hxy-u      → Monthly average reflected solar radiation
```

## Thermal (Longwave) Radiation

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `rlds` | Surface downwelling longwave | Surface energy budget, greenhouse effect |
| `rlus` | Surface upwelling longwave | Surface temperature, heat loss |
| `rlut` | Top-of-atmosphere outgoing longwave | Earth's heat emission to space |

**Examples**:
```
rlds_tavg-u-hxy-u      → Monthly average longwave down at surface
rlus_tavg-u-hxy-u      → Monthly average longwave up from surface
rlut_tavg-u-hxy-u      → Monthly average outgoing longwave to space
```

## Net Radiation

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `rns` | Surface net radiation | Total energy available at surface |
| `rnt` | Net radiation at top-of-atmosphere | Global energy imbalance |
| `rsn` | Net solar radiation at surface | Solar heating effect |
| `rln` | Net longwave radiation at surface | Cooling/warming effect |

**Examples**:
```
rns_tavg-u-hxy-u       → Monthly average net surface radiation
rnt_tavg-u-hxy-u       → Monthly average net radiation at TOA
```

## Cloud Radiative Effects

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `rsutcs` | Clear-sky outgoing solar | Cloud radiative effects |
| `rlutcs` | Clear-sky outgoing longwave | Greenhouse gas effects |
| `cre` | Cloud radiative effect | Cloud impact on energy balance |

**Examples**:
```
rsutcs_tavg-u-hxy-u    → Monthly average clear-sky outgoing solar
rlutcs_tavg-u-hxy-u    → Monthly average clear-sky outgoing longwave
```

## Surface Energy Fluxes

| Variable | What It Measures | When to Use |
|----------|------------------|-------------|
| `hfls` | Surface latent heat flux | Evaporative cooling |
| `hfss` | Surface sensible heat flux | Direct heating |
| `hfds` | Downward heat flux at surface | Ocean heat uptake |

**Examples**:
```
hfls_tavg-u-hxy-u      → Monthly average latent heat flux
hfss_tavg-u-hxy-u      → Monthly average sensible heat flux
hfds_tavg-u-hxy-sea    → Monthly average ocean heat flux
```

## Quick Selection Guide

**Need Earth's energy balance?** → Use `rsdt` (input), `rlut` (output), `rnt` (net)
**Need surface energy?** → Use `rsds`/`rlds` (downward), `rsus`/`rlus` (upward)
**Need net heating?** → Use `rns` for surface, `rnt` for top-of-atmosphere
**Need cloud effects?** → Use clear-sky variables (`*cs`) vs. all-sky
**Need surface heat transfer?** → Use `hfls` (evaporation), `hfss` (direct), `hfds` (ocean)

## Energy Balance

The Earth's energy balance connects these variables:

```
Incoming Solar = Reflected Solar + Outgoing Longwave
    rsdt      =      rsut      +       rlut
```

At the surface:
```
Net Radiation = Sensible Heat + Latent Heat + Ground Heat
      rns     =      hfss     +     hfls     +     hfds
```

[Browse all radiation variables →](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)