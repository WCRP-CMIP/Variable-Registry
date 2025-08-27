# Temperature Variables

## Role in CMIP Temperature Measurements

Temperature variables form the backbone of CMIP climate modeling, representing thermal energy across all Earth system components. These variables enable:

- **Climate change detection** through global and regional temperature trends
- **Model validation** against observational temperature records  
- **Process understanding** of energy transfer between atmosphere, ocean, and land
- **Impact assessment** for ecosystem, agriculture, and human systems

Standardized temperature variables ensure consistent thermal measurements across all CMIP models and scientific applications.

## CMIP Temperature Variable Categories

=== "Atmospheric Temperature"

    **Temperature measurements in the atmosphere**

    | Variable | Physical Quantity | CMIP Applications |
    |----------|-------------------|-------------------|
    | `tas` | Air temperature at 2m height | Weather monitoring, climate trends |
    | `ts` | Surface skin temperature | Satellite validation, energy balance |
    | `ta` | Air temperature at all levels | Weather prediction, atmospheric heating |
    | `tmax` | Daily maximum temperature | Heat wave analysis, extreme events |
    | `tmin` | Daily minimum temperature | Cold events, frost occurrence |

    **Standard Usage Examples**:
    ```
    tas_tavg-h2m-hxy-u     # Monthly average air temperature
    ts_tavg-u-hxy-u        # Monthly average surface temperature  
    ta_tpt-al-hxy-air      # Instantaneous atmospheric profiles
    tas_tmax-h2m-hxy-u     # Daily maximum temperature
    ```

=== "Ocean Temperature"

    **Temperature measurements in marine environments**

    | Variable | Physical Quantity | CMIP Applications |
    |----------|-------------------|-------------------|
    | `tos` | Sea surface temperature | Climate indices, marine ecosystems |
    | `thetao` | Ocean potential temperature | Heat content, circulation studies |
    | `to` | In-situ ocean temperature | Observational comparisons |
    | `tob` | Sea bottom temperature | Deep ocean processes |

    **Standard Usage Examples**:
    ```
    tos_tavg-u-hxy-sea     # Monthly sea surface temperature
    thetao_tavg-ol-hxy-sea # 3D ocean temperature structure
    to_tpt-ol-hxy-sea      # Instantaneous in-situ temperature
    ```

=== "Land & Surface Temperature"

    **Temperature measurements at Earth's surface**

    | Variable | Physical Quantity | CMIP Applications |
    |----------|-------------------|-------------------|
    | `tsl` | Soil temperature | Permafrost, land-atmosphere exchange |
    | `tsn` | Snow temperature | Snow metamorphosis, avalanche risk |
    | `trsn` | Temperature of snow-covered regions | Snow hydrology studies |

    **Standard Usage Examples**:
    ```
    tsl_tavg-sl-hxy-lnd    # Soil temperature profiles
    tsn_tavg-u-hxy-sn      # Snow surface temperature
    ```

## Heat & Energy Variables

=== "Surface Heat Fluxes"

    **Energy transfer at Earth's surface**

    | Variable | Physical Quantity | CMIP Applications |
    |----------|-------------------|-------------------|
    | `hfds` | Downward heat flux at sea surface | Ocean heat uptake |
    | `hfls` | Surface latent heat flux | Evaporation, water cycle |
    | `hfss` | Surface sensible heat flux | Energy balance studies |
    | `hfdsnb` | Heat flux below snowpack base | Snow energy balance |

    **Standard Usage Examples**:
    ```
    hfds_tavg-u-hxy-sea    # Ocean heat flux (climate change)
    hfls_tavg-u-hxy-u      # Global latent heat flux
    hfss_tavg-u-hxy-lnd    # Sensible heat over land
    ```

=== "Radiation Variables"

    **Radiative energy transfer**

    | Variable | Physical Quantity | CMIP Applications |
    |----------|-------------------|-------------------|
    | `rsds` | Surface downwelling shortwave | Solar energy input |
    | `rlut` | TOA outgoing longwave | Earth's energy budget |
    | `rlds` | Surface downwelling longwave | Atmospheric heating |
    | `rsut` | TOA outgoing shortwave | Planetary albedo |

    **Standard Usage Examples**:
    ```
    rsds_tavg-u-hxy-u      # Surface solar radiation
    rlut_tavg-u-hxy-u      # Outgoing thermal radiation
    ```

## Selection Guide by Application

### Climate Monitoring Applications

**Global climate trends**:
- `tas_tavg-h2m-hxy-u` - Global mean temperature  
- `tos_tavg-u-hxy-sea` - Global ocean temperature
- `ts_tavg-u-hxy-u` - Earth system skin temperature

**Regional climate studies**:
- `tas_tavg-h2m-hxy-u` - Regional air temperature patterns
- `tsl_tavg-sl-hxy-lnd` - Soil thermal conditions  
- `tsn_tavg-u-hxy-sn` - Snow-covered region temperature

### Extreme Event Analysis

**Heat wave detection**:
- `tas_tmax-h2m-hxy-u` - Daily maximum temperature
- `tas_tmin-h2m-hxy-u` - Nighttime cooling analysis
- `ts_tmax-u-hxy-u` - Surface temperature extremes

**Cold event analysis**:
- `tas_tmin-h2m-hxy-u` - Frost occurrence
- `tsl_tmin-sl-hxy-lnd` - Soil freezing depth
- `tsn_tavg-u-hxy-sn` - Snow thermal stability

### Model Validation

**Observational comparisons**:
- `tas_tavg-h2m-hxy-u` - Weather station validation
- `tos_tavg-u-hxy-sea` - SST buoy/satellite comparison
- `ts_tavg-u-hxy-u` - Satellite skin temperature validation

**Energy balance validation**:
- `hfds_tavg-u-hxy-sea` - Ocean heat flux measurements
- `hfls_tavg-u-hxy-u` - Flux tower comparisons
- `rsds_tavg-u-hxy-u` - Solar radiation networks

## Physical Consistency Guidelines

### Valid Temperature Combinations

**Atmospheric measurements**:
```
✓ tas_tavg-h2m-hxy-u      # Air temperature at standard height
✓ ta_tpt-al-hxy-air       # 3D atmospheric temperature  
✓ ts_tavg-u-hxy-u         # Surface skin temperature (all surfaces)
```

**Ocean measurements**:
```
✓ tos_tavg-u-hxy-sea      # Sea surface temperature over ocean
✓ thetao_tavg-ol-hxy-sea  # 3D ocean temperature in water column
✓ to_tpt-ol-hxy-sea       # Instantaneous ocean profiles
```

**Land measurements**:
```
✓ tsl_tavg-sl-hxy-lnd     # Soil temperature in ground
✓ tsn_tavg-u-hxy-sn       # Snow temperature over snow-covered areas
```

### Invalid Temperature Combinations

**Domain mismatches**:
```
❌ tos_tavg-al-hxy-air     # Sea temperature with atmospheric levels
❌ tas_tavg-ol-hxy-sea     # Air temperature with ocean coordinates
❌ tsl_tavg-u-hxy-sea      # Soil temperature over ocean
```

**Coordinate mismatches**:
```
❌ tos_tavg-h2m-hxy-sea    # Sea surface temperature at 2m height  
❌ tsl_tavg-al-hxy-lnd     # Soil temperature at atmospheric levels
```

## Most Common CMIP Temperature Variables

**Top 10 by usage frequency**:

1. `tas_tavg-h2m-hxy-u` - Near-surface air temperature (most used)
2. `tos_tavg-u-hxy-sea` - Sea surface temperature
3. `ta_tavg-al-hxy-air` - 3D atmospheric temperature  
4. `ts_tavg-u-hxy-u` - Surface skin temperature
5. `thetao_tavg-ol-hxy-sea` - Ocean temperature profiles
6. `tas_tmax-h2m-hxy-u` - Daily maximum temperature
7. `tas_tmin-h2m-hxy-u` - Daily minimum temperature
8. `tsl_tavg-sl-hxy-lnd` - Soil temperature
9. `hfds_tavg-u-hxy-sea` - Ocean heat flux
10. `hfls_tavg-u-hxy-u` - Surface latent heat

## Interactive Temperature Variable Builder

Use the [Variable Registry Explorer](../../web/branded-variable-builder.html) to build temperature variables:

**Try these examples**:
- [tas_tavg-h2m-hxy-u](../../web/branded-variable-builder.html?branding=tas_tavg-h2m-hxy-u) - Standard air temperature
- [tos_tavg-u-hxy-sea](../../web/branded-variable-builder.html?branding=tos_tavg-u-hxy-sea) - Sea surface temperature  
- [hfds_tavg-u-hxy-sea](../../web/branded-variable-builder.html?branding=hfds_tavg-u-hxy-sea) - Ocean heat flux

## Registry Resources

- **[Complete temperature variable list](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)** - All temperature variables
- **[Water cycle variables →](water-cycle.md)** - Related humidity and precipitation
- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)** - Build custom identifiers

---

*Temperature variables measure thermal energy across all Earth system components in CMIP.*