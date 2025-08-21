# Construction Examples

This section provides comprehensive, step-by-step examples of constructing branded identifiers across different climate domains.

## How to Use These Examples

Each example follows the same structure:
1. **Goal**: What variable we're trying to create
2. **Step-by-step breakdown**: Following the 5-step construction process
3. **Result**: The final branded identifier
4. **Use case**: When you'd use this variable

---

## Construction Examples by Domain

=== "Atmospheric Examples"

    ### Daily Maximum Temperature
    **Goal**: Daily maximum near-surface air temperature on a global grid

    ```yaml
    Step 1: tas        # near-surface air temperature
    Step 2: tmax       # daily maximum  
    Step 3: h2m        # 2-meter height
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface level

    Result: tas_tmax-h2m-hxy-u
    ```
    **Use case**: Heat wave analysis, extreme temperature studies

    ---

    ### 3D Wind Field  
    **Goal**: Monthly average eastward wind at all atmospheric levels

    ```yaml
    Step 1: ua         # eastward wind
    Step 2: tavg       # time average
    Step 3: al         # all atmospheric levels
    Step 4: hxy        # gridded horizontal
    Step 5: air        # atmospheric levels

    Result: ua_tavg-al-hxy-air
    ```
    **Use case**: Atmospheric circulation studies, jet stream analysis

    ---

    ### Surface Pressure
    **Goal**: Instantaneous surface pressure globally

    ```yaml
    Step 1: ps         # surface air pressure
    Step 2: tpt        # time point (instantaneous)
    Step 3: u          # unmasked/global
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: ps_tpt-u-hxy-u
    ```
    **Use case**: Weather forecasting, pressure system tracking

    ---

    ### Relative Humidity
    **Goal**: Monthly average relative humidity at 2m height

    ```yaml
    Step 1: hurs       # near-surface relative humidity
    Step 2: tavg       # time average
    Step 3: h2m        # 2-meter height
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface level

    Result: hurs_tavg-h2m-hxy-u
    ```
    **Use case**: Drought studies, comfort indices

=== "Ocean Examples"

    ### Sea Surface Temperature
    **Goal**: Monthly average sea surface temperature

    ```yaml
    Step 1: tos        # sea surface temperature
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: sea        # sea surface

    Result: tos_tavg-u-hxy-sea
    ```
    **Use case**: Climate change studies, coral bleaching analysis

    ---

    ### Ocean Temperature Profile
    **Goal**: Monthly average ocean temperature at all depths

    ```yaml
    Step 1: thetao     # sea water potential temperature
    Step 2: tavg       # time average
    Step 3: ol         # all ocean levels
    Step 4: hxy        # gridded horizontal
    Step 5: sea        # ocean levels

    Result: thetao_tavg-ol-hxy-sea
    ```
    **Use case**: Ocean heat content, thermocline studies

    ---

    ### Ocean Current Velocity
    **Goal**: Instantaneous eastward ocean velocity at all levels

    ```yaml
    Step 1: uo         # sea water x velocity
    Step 2: tpt        # time point
    Step 3: ol         # all ocean levels
    Step 4: hxy        # gridded horizontal
    Step 5: sea        # ocean levels

    Result: uo_tpt-ol-hxy-sea
    ```
    **Use case**: Ocean circulation modeling, current analysis

    ---

    ### Sea Level Height
    **Goal**: Monthly average sea surface height

    ```yaml
    Step 1: zos        # sea surface height
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: sea        # sea surface

    Result: zos_tavg-u-hxy-sea
    ```
    **Use case**: Sea level rise studies, tide analysis

=== "Precipitation Examples"

    ### Monthly Average Precipitation
    **Goal**: Monthly average precipitation rate globally

    ```yaml
    Step 1: pr         # precipitation rate
    Step 2: tavg       # time average
    Step 3: u          # unmasked/global
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: pr_tavg-u-hxy-u
    ```
    **Use case**: Climate monitoring, drought assessment

    ---

    ### Daily Maximum Rainfall
    **Goal**: Daily maximum precipitation over land areas

    ```yaml
    Step 1: pr         # precipitation rate
    Step 2: tmax       # daily maximum
    Step 3: lnd        # land areas only
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: pr_tmax-lnd-hxy-u
    ```
    **Use case**: Flood risk assessment, extreme precipitation analysis

    ---

    ### Snow Precipitation
    **Goal**: Monthly snowfall rate globally

    ```yaml
    Step 1: prsn       # snowfall rate
    Step 2: tavg       # time average
    Step 3: u          # unmasked/global
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: prsn_tavg-u-hxy-u
    ```
    **Use case**: Snow water equivalent studies, avalanche forecasting

    ---

    ### Convective Precipitation
    **Goal**: Daily average convective precipitation

    ```yaml
    Step 1: prc        # convective precipitation
    Step 2: tavg       # time average
    Step 3: u          # unmasked/global
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: prc_tavg-u-hxy-u
    ```
    **Use case**: Thunderstorm climatology, convection studies

=== "Land Examples"

    ### Soil Moisture
    **Goal**: Monthly average soil moisture in all soil layers over land

    ```yaml
    Step 1: mrsol      # soil moisture content
    Step 2: tavg       # time average
    Step 3: sl         # all soil levels
    Step 4: hxy        # gridded horizontal
    Step 5: lnd        # land areas

    Result: mrsol_tavg-sl-hxy-lnd
    ```
    **Use case**: Drought monitoring, agricultural planning

    ---

    ### Vegetation Carbon
    **Goal**: Annual average vegetation carbon content over land

    ```yaml
    Step 1: cVeg       # vegetation carbon
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: lnd        # land areas

    Result: cVeg_tavg-u-hxy-lnd
    ```
    **Use case**: Carbon cycle studies, forest monitoring

    ---

    ### Leaf Area Index
    **Goal**: Monthly average leaf area index over land

    ```yaml
    Step 1: lai        # leaf area index
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: lnd        # land areas

    Result: lai_tavg-u-hxy-lnd
    ```
    **Use case**: Vegetation phenology, photosynthesis studies

    ---

    ### Soil Temperature
    **Goal**: Daily average soil temperature at all soil levels

    ```yaml
    Step 1: tsl        # soil temperature
    Step 2: tavg       # time average
    Step 3: sl         # all soil levels
    Step 4: hxy        # gridded horizontal
    Step 5: lnd        # land areas

    Result: tsl_tavg-sl-hxy-lnd
    ```
    **Use case**: Permafrost studies, soil thermal dynamics

=== "Ice Examples"

    ### Sea Ice Concentration
    **Goal**: Monthly average sea ice concentration

    ```yaml
    Step 1: siconc     # sea ice area percentage
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: siconc_tavg-u-hxy-u
    ```
    **Use case**: Arctic/Antarctic ice studies, climate monitoring

    ---

    ### Sea Ice Thickness
    **Goal**: Monthly average sea ice thickness

    ```yaml
    Step 1: sithick    # sea ice thickness
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: si         # sea ice

    Result: sithick_tavg-u-hxy-si
    ```
    **Use case**: Ice volume studies, shipping route planning

    ---

    ### Land Ice Thickness
    **Goal**: Annual average land ice thickness

    ```yaml
    Step 1: lithk      # land ice thickness
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: is         # ice sheet

    Result: lithk_tavg-u-hxy-is
    ```
    **Use case**: Ice sheet modeling, sea level projections

=== "Radiation Examples"

    ### Shortwave Radiation
    **Goal**: Daily average downward shortwave radiation at surface

    ```yaml
    Step 1: rsds       # surface downwelling shortwave
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: rsds_tavg-u-hxy-u
    ```
    **Use case**: Solar energy studies, radiation balance

    ---

    ### Longwave Radiation
    **Goal**: Monthly average upward longwave radiation at top of atmosphere

    ```yaml
    Step 1: rlut       # TOA upwelling longwave
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: u          # top of atmosphere

    Result: rlut_tavg-u-hxy-u
    ```
    **Use case**: Earth's energy budget, greenhouse effect studies

    ---

    ### Net Radiation
    **Goal**: Daily average net radiation at surface

    ```yaml
    Step 1: rns        # surface net radiation
    Step 2: tavg       # time average
    Step 3: u          # unmasked
    Step 4: hxy        # gridded horizontal
    Step 5: u          # surface

    Result: rns_tavg-u-hxy-u
    ```
    **Use case**: Energy balance studies, ecosystem modeling


## Common Construction Mistakes

=== ###  **Physically Inconsistent Combinations**
```
Wrong: tos_tavg-al-hxy-air   # Sea surface temp with atmospheric levels
Right: tos_tavg-u-hxy-sea    # Sea surface temp with sea surface level
```

=== ###  **Inappropriate Spatial Domain**
```
Wrong: lai_tavg-sea-hxy-u    # Leaf area over ocean
Right: lai_tavg-u-hxy-lnd    # Leaf area over land
```

=== ###  **Mismatched Components**
```
Wrong: pr_tavg-ol-hxy-u      # Precipitation at ocean levels
Right: pr_tavg-u-hxy-u       # Precipitation at surface
```

## Navigation

- **[← Back to Construction Overview](index.md)**
- **[Common Patterns →](patterns.md)**
- **[Rules & Validation →](rules-and-validation.md)**
- **[Component Reference →](../03-component-reference.md)**

---

*These examples cover the most common variable types in climate modeling. Use them as templates for constructing similar variables in your domain.*