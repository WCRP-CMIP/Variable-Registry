# What is a Root Variable?

A **root variable** is the fundamental physical quantity at the core of every branded identifier. It answers the simple question: *"What are you measuring?"*

## The Basics

Root variables are the first part of every branded identifier:

```
[root-variable]_[temporal]-[vertical]-[horizontal]-[area]
       ↑
   This part
```

## Common Examples

| Root Variable | What It Measures | Example Use |
|---------------|------------------|-------------|
| `tas` | Near-surface air temperature | Weather stations, climate monitoring |
| `tos` | Sea surface temperature | Ocean heat content, El Niño tracking |
| `pr` | Precipitation (rain + snow) | Drought monitoring, flood forecasting |
| `ua` | Eastward wind | Weather prediction, storm tracking |
| `siconc` | Sea ice concentration | Arctic studies, shipping routes |

## How to Choose

**Step 1: Identify the physical quantity**
- Temperature? → `tas`, `tos`, `ta`
- Precipitation? → `pr`, `prc`, `prsn`
- Wind? → `ua`, `va`, `sfcWind`

**Step 2: Consider the domain**
- Atmosphere: `tas`, `ua`, `pr`
- Ocean: `tos`, `uo`, `so`
- Land: `mrso`, `lai`, `gpp`
- Ice: `siconc`, `sithick`, `lithk`

## Main Categories

| Domain | Common Variables | What They Measure |
|--------|------------------|-------------------|
| **Atmosphere** | `tas`, `pr`, `ua`, `va`, `ps` | Temperature, precipitation, wind, pressure |
| **Ocean** | `tos`, `uo`, `vo`, `so`, `zos` | Temperature, currents, salinity, sea level |
| **Land** | `mrso`, `lai`, `gpp`, `evspsbl` | Soil moisture, vegetation, carbon, evaporation |
| **Ice** | `siconc`, `sithick`, `lithk`, `snd` | Sea ice, land ice, snow |

## Browse by Category

- **[Temperature & Energy →](temperature.md)** - Heat and radiation variables
- **[Water Cycle →](water-cycle.md)** - Precipitation, humidity, soil moisture

## Quick Reference

**Most used variables**:
- `tas` - Air temperature at 2m height
- `tos` - Sea surface temperature  
- `pr` - Total precipitation
- `ua` - Eastward wind component
- `va` - Northward wind component

**Find all 620+ variables**: [GitHub Repository](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)

---

*Root variables define what physical quantity you're measuring. Everything else in the identifier describes how, when, and where.*