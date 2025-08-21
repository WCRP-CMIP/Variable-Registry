# Common Patterns

This guide presents the most frequently used patterns for constructing branded identifiers across different climate modeling domains.

## Pattern Categories

Understanding these patterns will help you construct identifiers that follow established conventions and ensure consistency across the climate modeling community.

---

## Domain-Specific Patterns

=== "Atmospheric Variables"

    ### Surface Meteorological Variables
    **Pattern**: `[variable]_[time]-h[height]-hxy-u`
    
    ```yaml
    # Near-surface weather variables
    tas_tavg-h2m-hxy-u      # 2m air temperature (monthly mean)
    tas_tmax-h2m-hxy-u      # 2m air temperature (daily max)
    tas_tmin-h2m-hxy-u      # 2m air temperature (daily min)
    hurs_tavg-h2m-hxy-u     # 2m relative humidity
    sfcWind_tavg-h10m-hxy-u # 10m wind speed
    uas_tavg-h10m-hxy-u     # 10m eastward wind
    vas_tavg-h10m-hxy-u     # 10m northward wind
    ```
    
    **Usage**: Weather station data, near-surface climate analysis

    ---

    ### 3D Atmospheric Variables  
    **Pattern**: `[variable]_[time]-al-hxy-air`
    
    ```yaml
    # Full atmospheric column
    ta_tavg-al-hxy-air      # Air temperature (all levels)
    ua_tavg-al-hxy-air      # Eastward wind (all levels)
    va_tavg-al-hxy-air      # Northward wind (all levels)
    hus_tavg-al-hxy-air     # Specific humidity (all levels)
    wap_tavg-al-hxy-air     # Vertical velocity (all levels)
    ```
    
    **Usage**: Atmospheric circulation studies, climate model output

    ---

    ### Pressure Level Variables
    **Pattern**: `[variable]_[time]-p[levels]-hxy-air`
    
    ```yaml
    # Standard pressure levels
    ta_tavg-p19-hxy-air     # Temperature on 19 standard levels
    ua_tavg-p19-hxy-air     # Eastward wind on pressure levels
    va_tavg-p19-hxy-air     # Northward wind on pressure levels
    zg_tavg-p19-hxy-air     # Geopotential height on pressure levels
    ```
    
    **Usage**: Weather analysis, reanalysis products, forecasting

    ---

    ### Surface Pressure Variables
    **Pattern**: `[variable]_[time]-u-hxy-u`
    
    ```yaml
    # Surface pressure fields
    ps_tavg-u-hxy-u         # Surface pressure (monthly mean)
    ps_tpt-u-hxy-u          # Surface pressure (instantaneous)
    psl_tavg-u-hxy-u        # Sea level pressure (monthly mean)
    ```
    
    **Usage**: Pressure system analysis, weather patterns

=== "Ocean Variables"

    ### Sea Surface Variables
    **Pattern**: `[variable]_[time]-u-hxy-sea`
    
    ```yaml
    # Ocean surface properties
    tos_tavg-u-hxy-sea      # Sea surface temperature
    sos_tavg-u-hxy-sea      # Sea surface salinity  
    zos_tavg-u-hxy-sea      # Sea surface height
    wfo_tavg-u-hxy-sea      # Water flux into ocean
    hfds_tavg-u-hxy-sea     # Heat flux into ocean
    ```
    
    **Usage**: Ocean-atmosphere interaction, marine ecosystems

    ---

    ### 3D Ocean Variables
    **Pattern**: `[variable]_[time]-ol-hxy-sea`
    
    ```yaml
    # Full ocean column
    thetao_tavg-ol-hxy-sea  # Potential temperature (all levels)
    so_tavg-ol-hxy-sea      # Salinity (all levels)
    uo_tavg-ol-hxy-sea      # Eastward velocity (all levels)
    vo_tavg-ol-hxy-sea      # Northward velocity (all levels)
    wo_tavg-ol-hxy-sea      # Upward velocity (all levels)
    ```
    
    **Usage**: Ocean circulation, heat transport, mixing studies

    ---

    ### Ocean Biogeochemistry
    **Pattern**: `[variable]_[time]-[level]-hxy-sea`
    
    ```yaml
    # Marine biogeochemical variables
    chl_tavg-d0m-hxy-sea    # Chlorophyll at surface
    chl_tavg-ol-hxy-sea     # Chlorophyll (all levels)
    o2_tavg-ol-hxy-sea      # Dissolved oxygen
    no3_tavg-ol-hxy-sea     # Nitrate concentration
    po4_tavg-ol-hxy-sea     # Phosphate concentration
    ```
    
    **Usage**: Marine productivity, biogeochemical cycling

=== "Land Variables"

    ### Land Surface Variables
    **Pattern**: `[variable]_[time]-u-hxy-lnd`
    
    ```yaml
    # Surface land properties
    mrsos_tavg-u-hxy-lnd    # Surface soil moisture
    ts_tavg-u-hxy-lnd       # Surface temperature over land
    lai_tavg-u-hxy-lnd      # Leaf area index
    fFire_tavg-u-hxy-lnd    # Fire carbon flux
    gpp_tavg-u-hxy-lnd      # Gross primary productivity
    ```
    
    **Usage**: Land surface modeling, vegetation dynamics

    ---

    ### Soil Variables  
    **Pattern**: `[variable]_[time]-sl-hxy-lnd`
    
    ```yaml
    # Multi-layer soil variables
    mrsol_tavg-sl-hxy-lnd   # Soil moisture (all soil levels)
    tsl_tavg-sl-hxy-lnd     # Soil temperature (all soil levels)
    cSoil_tavg-sl-hxy-lnd   # Soil carbon (all soil levels)
    ```
    
    **Usage**: Soil dynamics, root zone studies, permafrost

    ---

    ### Vegetation Carbon
    **Pattern**: `[carbon-var]_[time]-u-hxy-lnd`
    
    ```yaml
    # Carbon cycle variables
    cVeg_tavg-u-hxy-lnd     # Vegetation carbon
    cLitter_tavg-u-hxy-lnd  # Litter carbon
    cSoil_tavg-u-hxy-lnd    # Soil carbon
    nbp_tavg-u-hxy-lnd      # Net biome productivity
    npp_tavg-u-hxy-lnd      # Net primary productivity
    ```
    
    **Usage**: Carbon cycle studies, ecosystem modeling

=== "Precipitation Variables"

    ### Precipitation Types
    **Pattern**: `[precip-type]_[time]-u-hxy-u`
    
    ```yaml
    # Different precipitation forms
    pr_tavg-u-hxy-u         # Total precipitation
    prc_tavg-u-hxy-u        # Convective precipitation
    prsn_tavg-u-hxy-u       # Snowfall
    prra_tavg-u-hxy-u       # Rainfall
    ```
    
    **Usage**: Hydrology, weather pattern analysis

    ---

    ### Precipitation Extremes
    **Pattern**: `pr_t[extreme]-[area]-hxy-u`
    
    ```yaml
    # Extreme precipitation events
    pr_tmax-u-hxy-u         # Maximum precipitation (global)
    pr_tmax-lnd-hxy-u       # Maximum precipitation (land only)
    pr_tmin-u-hxy-u         # Minimum precipitation
    ```
    
    **Usage**: Flood risk, drought analysis, extreme events

=== "Radiation Variables"

    ### Surface Radiation
    **Pattern**: `[radiation]_[time]-u-hxy-u`
    
    ```yaml
    # Surface radiation components
    rsds_tavg-u-hxy-u       # Downward shortwave at surface
    rsus_tavg-u-hxy-u       # Upward shortwave at surface
    rlds_tavg-u-hxy-u       # Downward longwave at surface
    rlus_tavg-u-hxy-u       # Upward longwave at surface
    rns_tavg-u-hxy-u        # Net shortwave at surface
    ```
    
    **Usage**: Energy balance, solar applications

    ---

    ### Top-of-Atmosphere Radiation
    **Pattern**: `[toa-radiation]_[time]-u-hxy-u`
    
    ```yaml
    # TOA radiation budget
    rsdt_tavg-u-hxy-u       # Incoming solar at TOA
    rsut_tavg-u-hxy-u       # Outgoing shortwave at TOA
    rlut_tavg-u-hxy-u       # Outgoing longwave at TOA
    rtmt_tavg-u-hxy-u       # Net TOA radiation
    ```
    
    **Usage**: Earth's energy budget, climate sensitivity

=== "Ice Variables"

    ### Sea Ice
    **Pattern**: `si[property]_[time]-u-hxy-[ice-level]`
    
    ```yaml
    # Sea ice properties
    siconc_tavg-u-hxy-u     # Sea ice concentration
    sithick_tavg-u-hxy-si   # Sea ice thickness
    siage_tavg-u-hxy-si     # Sea ice age
    siu_tavg-u-hxy-si       # Sea ice eastward velocity
    siv_tavg-u-hxy-si       # Sea ice northward velocity
    ```
    
    **Usage**: Arctic/Antarctic studies, sea ice modeling

    ---

    ### Land Ice
    **Pattern**: `[ice-var]_[time]-u-hxy-is`
    
    ```yaml
    # Ice sheet variables
    lithk_tavg-u-hxy-is     # Land ice thickness
    litemptop_tavg-u-hxy-is # Ice temperature at surface
    xvelsurf_tavg-u-hxy-is  # Ice surface velocity (x)
    yvelsurf_tavg-u-hxy-is  # Ice surface velocity (y)
    ```
    
    **Usage**: Ice sheet modeling, sea level projections

## Temporal Pattern Conventions

=== "Time Aggregation Patterns"

    ### Climate Timescales
    ```yaml
    # Long-term climate variables (monthly/annual means)
    [variable]_tavg-[area]-[horizontal]-[vertical]
    
    Examples:
    tas_tavg-h2m-hxy-u      # Monthly mean temperature
    pr_tavg-u-hxy-u         # Monthly mean precipitation
    tos_tavg-u-hxy-sea      # Monthly mean SST
    ```

    ### Weather Timescales
    ```yaml
    # Daily or sub-daily variables
    [variable]_tpt-[area]-[horizontal]-[vertical]   # Instantaneous
    [variable]_tmax-[area]-[horizontal]-[vertical]  # Daily maximum
    [variable]_tmin-[area]-[horizontal]-[vertical]  # Daily minimum
    
    Examples:
    tas_tmax-h2m-hxy-u      # Daily maximum temperature
    pr_tpt-u-hxy-u          # Instantaneous precipitation
    ps_tpt-u-hxy-u          # Instantaneous pressure
    ```

=== "Frequency Patterns"

    ### High-Frequency Output
    ```yaml
    # Sub-daily to daily variables
    Pattern: [variable]_tpt-[area]-hxy-[vertical]
    
    tas_tpt-h2m-hxy-u       # Hourly/3-hourly temperature
    pr_tpt-u-hxy-u          # Hourly precipitation
    ps_tpt-u-hxy-u          # Pressure tendency
    ```

    ### Climate Monitoring
    ```yaml
    # Monthly to annual means
    Pattern: [variable]_tavg-[area]-hxy-[vertical]
    
    tas_tavg-h2m-hxy-u      # Climate normal temperature
    pr_tavg-u-hxy-u         # Climate normal precipitation
    ```

## Spatial Pattern Conventions

=== "Global Coverage"

    ### Global Gridded Data
    ```yaml
    Pattern: [variable]_[time]-u-hxy-[vertical]
    
    # Most common for global climate studies
    tas_tavg-u-hxy-u        # Global temperature (no height specified)
    pr_tavg-u-hxy-u         # Global precipitation
    ps_tavg-u-hxy-u         # Global pressure
    ```

=== "Domain-Specific Coverage"

    ### Land-Only Analysis
    ```yaml
    Pattern: [variable]_[time]-lnd-hxy-[vertical]
    
    lai_tavg-lnd-hxy-u      # Vegetation over land only
    mrsos_tavg-lnd-hxy-u    # Soil moisture over land
    ts_tavg-lnd-hxy-u       # Surface temp over land
    ```

    ### Ocean-Only Analysis  
    ```yaml
    Pattern: [variable]_[time]-u-hxy-sea
    
    tos_tavg-u-hxy-sea      # Sea surface temperature
    sos_tavg-u-hxy-sea      # Sea surface salinity
    ```

## Vertical Pattern Conventions

=== "Surface Variables"

    ### 2D Surface Fields
    ```yaml
    Pattern: [variable]_[time]-[area]-hxy-u
    
    # Most surface variables use 'u' for vertical
    pr_tavg-u-hxy-u         # Precipitation (no vertical dim)
    ps_tavg-u-hxy-u         # Surface pressure
    ts_tavg-u-hxy-u         # Surface temperature
    ```

=== "3D Atmospheric Variables"

    ### Full Atmospheric Column
    ```yaml
    Pattern: [variable]_[time]-al-hxy-air
    
    ta_tavg-al-hxy-air      # Temperature (all atmos levels)
    ua_tavg-al-hxy-air      # Wind (all atmos levels)
    ```

=== "3D Ocean Variables"

    ### Full Ocean Column
    ```yaml
    Pattern: [variable]_[time]-ol-hxy-sea
    
    thetao_tavg-ol-hxy-sea  # Temperature (all ocean levels)
    so_tavg-ol-hxy-sea      # Salinity (all ocean levels)
    ```

## Pattern Validation Rules

### ✅ **Consistent Patterns**
```yaml
# Atmospheric surface variables
tas_tavg-h2m-hxy-u      ✓ Temperature at 2m height
hurs_tavg-h2m-hxy-u     ✓ Humidity at 2m height  
uas_tavg-h10m-hxy-u     ✓ Wind at 10m height

# Ocean surface variables  
tos_tavg-u-hxy-sea      ✓ Sea surface temperature
sos_tavg-u-hxy-sea      ✓ Sea surface salinity

# Land surface variables
lai_tavg-u-hxy-lnd      ✓ Leaf area over land
mrsos_tavg-u-hxy-lnd    ✓ Surface soil moisture
```

### ❌ **Inconsistent Patterns**
```yaml
# Mixing incompatible domains
tos_tavg-al-hxy-air     ✗ Sea temp with atmospheric levels
lai_tavg-u-hxy-sea      ✗ Leaf area over ocean
siconc_tavg-lnd-hxy-u   ✗ Sea ice over land

# Inappropriate vertical levels
pr_tavg-ol-hxy-u        ✗ Precipitation at ocean levels
ps_tavg-al-hxy-air      ✗ Surface pressure with 3D levels
```

## Quick Pattern Reference

| Domain | Common Pattern | Example |
|--------|----------------|---------|
| **Atmosphere (Surface)** | `var_time-h[X]m-hxy-u` | `tas_tavg-h2m-hxy-u` |
| **Atmosphere (3D)** | `var_time-al-hxy-air` | `ta_tavg-al-hxy-air` |
| **Ocean (Surface)** | `var_time-u-hxy-sea` | `tos_tavg-u-hxy-sea` |
| **Ocean (3D)** | `var_time-ol-hxy-sea` | `thetao_tavg-ol-hxy-sea` |
| **Land (Surface)** | `var_time-u-hxy-lnd` | `lai_tavg-u-hxy-lnd` |
| **Land (Soil)** | `var_time-sl-hxy-lnd` | `tsl_tavg-sl-hxy-lnd` |
| **Precipitation** | `pr_time-u-hxy-u` | `pr_tavg-u-hxy-u` |
| **Sea Ice** | `si[var]_time-u-hxy-si` | `siconc_tavg-u-hxy-u` |
| **Radiation** | `r[var]_time-u-hxy-u` | `rsds_tavg-u-hxy-u` |

## Pattern Selection Guide

### 1. **Identify the Domain**
- Atmosphere → Use `air`, `al`, or height levels
- Ocean → Use `sea`, `ol`, or specific depths  
- Land → Use `lnd`, `sl` (soil levels)
- Ice → Use `si` (sea ice) or `is` (ice sheet)

### 2. **Choose Appropriate Temporal Sampling**
- Climate studies → `tavg` (time average)
- Extreme events → `tmax`, `tmin`
- Weather/forecasting → `tpt` (time point)

### 3. **Match Spatial Coverage**
- Global studies → `u` (unmasked)
- Domain-specific → `lnd`, `sea`, `ice`
- Height-specific → `h2m`, `h10m`, etc.

### 4. **Validate Physical Consistency**
- Check domain compatibility
- Ensure vertical level makes sense
- Verify temporal sampling is appropriate

## Navigation

- **[← Construction Examples](examples.md)**
- **[Rules & Validation →](rules-and-validation.md)**
- **[Construction Overview →](index.md)**
- **[Component Reference →](../03-component-reference.md)**

---

*These patterns represent best practices developed by the climate modeling community. Following them ensures consistency and interoperability across different modeling centers and projects.*