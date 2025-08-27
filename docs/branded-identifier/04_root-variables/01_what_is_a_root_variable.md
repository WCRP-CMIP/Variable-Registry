# What is a Root Variable?

## Role in CMIP Variable System

A **root variable** is the fundamental physical quantity at the core of every CMIP branded identifier. It answers the essential question: *"What physical process are you measuring?"* and provides the scientific foundation for all CMIP model intercomparison.

Root variables ensure that all CMIP models measure the same physical phenomena using standardized definitions, units, and scientific protocols.

## Position in Branded Identifiers

Root variables are the first component of every branded identifier:

```
[root-variable]_[temporal]-[vertical]-[horizontal]-[area]
       ↑
   This part defines WHAT you're measuring
```

All other components describe HOW, WHEN, and WHERE the measurement is processed.




## CMIP Root Variable Categories

=== "Atmospheric Variables"

    **Essential atmospheric processes for climate modeling**

    | Root Variable | Physical Quantity | CMIP Applications |
    |---------------|-------------------|-------------------|
    | `tas` | Near-surface air temperature | Climate monitoring, heat waves |
    | `pr` | Precipitation (rain + snow) | Water cycle, extreme events |
    | `ua`, `va` | Wind components | Circulation, storm tracking |
    | `ps` | Surface air pressure | Weather systems, climate indices |
    | `hurs` | Near-surface relative humidity | Drought, comfort indices |

=== "Ocean Variables"

    **Ocean processes critical for climate system**

    | Root Variable | Physical Quantity | CMIP Applications |
    |---------------|-------------------|-------------------|
    | `tos` | Sea surface temperature | El Niño, marine ecosystems |
    | `thetao` | Ocean potential temperature | Heat content, circulation |
    | `so` | Ocean salinity | Density, overturning circulation |
    | `uo`, `vo` | Ocean velocity components | Current systems, transport |
    | `zos` | Sea surface height | Sea level rise, ocean dynamics |

=== "Land Variables"

    **Terrestrial processes for Earth system modeling**

    | Root Variable | Physical Quantity | CMIP Applications |
    |---------------|-------------------|-------------------|
    | `mrsol` | Soil moisture content | Drought, agriculture |
    | `lai` | Leaf area index | Vegetation phenology, carbon cycle |
    | `gpp` | Gross primary productivity | Carbon uptake, ecosystems |
    | `mrro` | Surface runoff | Water resources, flooding |
    | `evspsbl` | Evapotranspiration | Water-energy balance |

=== "Ice Variables"

    **Cryospheric processes for polar and high-altitude regions**

    | Root Variable | Physical Quantity | CMIP Applications |
    |---------------|-------------------|-------------------|
    | `siconc` | Sea ice area fraction | Arctic/Antarctic monitoring |
    | `sithick` | Sea ice thickness | Ice volume, shipping routes |
    | `lithk` | Land ice thickness | Glaciers, ice sheet mass balance |
    | `snd` | Snow depth | Seasonal snowpack, hydrology |

## Root Variable Selection Guide

### By Scientific Domain

**Studying atmospheric processes?**

- Temperature: `tas` (2m air), `ta` (profiles), `ts` (surface skin)
- Water: `pr` (precipitation), `hurs` (humidity), `evspsbl` (evaporation)  
- Dynamics: `ua`/`va` (wind), `ps` (pressure), `wap` (vertical motion)

**Studying ocean processes?**  

- Temperature: `tos` (surface), `thetao` (3D potential), `to` (in-situ)
- Dynamics: `uo`/`vo` (currents), `zos` (sea level), `msftmz` (overturning)
- Properties: `so` (salinity), `rho` (density), `mlotst` (mixed layer)

**Studying land processes?**

- Hydrology: `mrsol` (soil moisture), `mrro` (runoff), `mrsos` (surface soil)
- Vegetation: `lai` (leaf area), `gpp` (productivity), `npp` (net productivity)  
- Carbon: `cVeg` (vegetation), `cSoil` (soil), `nbp` (net biome productivity)

**Studying ice processes?**

- Sea ice: `siconc` (concentration), `sithick` (thickness), `siu`/`siv` (velocity)
- Land ice: `lithk` (thickness), `lifmassbf` (mass flux), `ligroundf` (grounding line)
- Snow: `snd` (depth), `snw` (water equivalent), `tsn` (temperature)

### By Measurement Type

**Direct observations match:**

- Weather stations → `tas`, `pr`, `hurs`, `sfcWind`  
- Ocean buoys → `tos`, `sos`, `zos`
- Satellite data → `siconc`, `lai`, `ts`
- Flux towers → `gpp`, `evspsbl`, `hfss`

**Model diagnostics:**

- Energy fluxes → `hfds`, `hfls`, `rlut`, `rsdt`
- Circulation → `ua`, `va`, `uo`, `vo`, `wap`  
- Biogeochemistry → `o2`, `no3`, `co3`, `ph`




## Common Patterns

| Variable Type | Typical Pattern |
|---------------|----------------|
| **Surface meteorology** | `{var}_tavg-h2m-hxy-u` |
| **3D atmosphere** | `{var}_tavg-al-hxy-air` |
| **Ocean surface** | `{var}_tavg-u-hxy-sea` |
| **Ocean 3D** | `{var}_tavg-ol-hxy-sea` |
| **Land surface** | `{var}_tavg-u-hxy-lnd` |
| **Soil layers** | `{var}_tavg-sl-hxy-lnd` |


## Physical Consistency Requirements

### Valid Root Variable Usage

Root variables have physical constraints that determine compatible components:

**Atmospheric variables** require:
- Vertical: Atmospheric coordinates (`al`, `p19`, `h2m`) or surface (`u`)
- Area: Atmospheric domains (`air`, `u`) or surface types (`lnd`, `sea`)

**Ocean variables** require:
- Vertical: Ocean coordinates (`ol`, `d0m`, `d100m`) or surface (`u`)  
- Area: Ocean domains (`sea`) - cannot exist over land

**Land variables** require:
- Vertical: Land coordinates (`sl`, `u`) or near-surface (`h2m`)
- Area: Land domains (`lnd`) - cannot exist over ocean

### Invalid Root Variable Combinations

```
❌ tos_tavg-al-hxy-air    # Sea temperature with atmospheric levels
❌ tas_tavg-ol-hxy-sea    # Air temperature with ocean levels  
❌ mrsol_tavg-u-hxy-sea   # Soil moisture over ocean
❌ siconc_tavg-sl-hxy-lnd # Sea ice with soil levels
```

## CMIP Registry Structure

### Root Variable Definitions

Each root variable in the registry includes:

```json
{
  "id": "tas",
  "ui-label": "Near-Surface Air Temperature", 
  "description": "Air temperature at reference height (usually 2m)",
  "standard-name": "air_temperature",
  "canonical-units": "K",
  "physical-domain": "atmosphere"
}
```

### Registry Scale

The CMIP Variable Registry contains **620+ root variables** covering:

- **Atmosphere**: 180+ variables (dynamics, thermodynamics, chemistry)
- **Ocean**: 150+ variables (physics, biogeochemistry, sea ice)  
- **Land**: 120+ variables (hydrology, vegetation, carbon cycle)
- **Ice/Snow**: 80+ variables (sea ice, land ice, snow processes)
- **Radiation**: 90+ variables (solar, thermal, cloud interactions)

## Root Variable Discovery

### Interactive Tools

[Variable Registry Explorer](../../web/branded-variable-builder.html){.md-button}

- Browse all 620+ root variables with descriptions
- Search by keyword or scientific domain
- Autocomplete functionality with variable details
- Real-time validation of variable combinations

### Browse by Category

**Atmospheric Variables**:

- **[Temperature & Energy →](temperature.md)** - Heat and radiation variables

- **[Water Cycle →](water-cycle.md)** - Precipitation, humidity, clouds

- **[Dynamics →](dynamics.md)** - Wind, pressure, circulation

**Ocean Variables**:

- **[Ocean →](ocean.md)** - Temperature, salinity, currents, biogeochemistry

**Terrestrial Variables**:  

- **[Land Ecosystems →](land-ecosystems.md)** - Vegetation, carbon, hydrology

**Cryospheric Variables**:

- **[Ice & Snow →](ice-snow.md)** - Sea ice, land ice, snow processes

### Registry Resources

**Complete root variable catalog**:
- **[GitHub Repository](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)** - All variable definitions
- **[Live API](https://wcrp-cmip.github.io/Variable-Registry/variable-root/)** - Machine-readable access
- **[Variable Search](https://wcrp-cmip.github.io/Variable-Registry/)** - Documentation website

## Most Common CMIP Variables

**Top 20 root variables by usage frequency**:

| Rank | Variable | Description | Typical Usage |
|------|----------|-------------|---------------|
| 1 | `tas` | Near-surface air temperature | Climate monitoring |
| 2 | `pr` | Precipitation rate | Water cycle studies |
| 3 | `tos` | Sea surface temperature | Ocean-atmosphere coupling |
| 4 | `ps` | Surface air pressure | Atmospheric dynamics |
| 5 | `ua` | Eastward wind | Circulation analysis |
| 6 | `va` | Northward wind | Storm tracking |
| 7 | `hurs` | Near-surface relative humidity | Drought studies |
| 8 | `rsds` | Surface solar radiation | Energy balance |
| 9 | `rlut` | Outgoing longwave radiation | Earth's energy budget |
| 10 | `siconc` | Sea ice concentration | Polar climate |

## Quality Assurance

### Before Using Root Variables

1. **Verify definition**: Check registry for complete variable description
2. **Confirm domain**: Ensure variable matches your modeling domain  
3. **Check units**: Verify canonical units match your model output
4. **Validate combinations**: Ensure compatible with other components
5. **Review precedent**: Look for similar variables in CMIP archives

### Community Standards

All CMIP root variables follow strict standards:

- **CF Convention compliance** for metadata and units
- **Physical consistency** validated by domain experts  
- **Community review** through CMIP working groups
- **Version control** for updates and corrections
- **Documentation requirements** for scientific accuracy

## Next Steps

- **[Browse variable categories →](../07_root-variables/)** - Explore by scientific domain
- **[Learn construction →](../02_How%20to%20Construct/01_general_structure.md)** - Build complete identifiers
- **[Interactive explorer →](../../web/branded-variable-builder.html)** - Try building identifiers

---

*Root variables define WHAT you're measuring in CMIP. Everything else describes HOW, WHEN, and WHERE.*