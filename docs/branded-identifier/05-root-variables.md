# Construction Examples

Step-by-step examples of constructing branded identifiers across different climate domains.

## Pattern Reminder

```
[root-variable]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
```

---

## Atmospheric Examples

### Daily Maximum Temperature
**Goal**: Daily maximum near-surface air temperature globally

```yaml
Step 1: tas        # near-surface air temperature
Step 2: tmax       # daily maximum  
Step 3: h2m        # 2-meter height
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: tas_tmax-h2m-hxy-u
```
**Use case**: Heat wave analysis, extreme temperature studies

### 3D Wind Field  
**Goal**: Monthly average eastward wind at all atmospheric levels

```yaml
Step 1: ua         # eastward wind
Step 2: tavg       # time average
Step 3: al         # all atmospheric levels
Step 4: hxy        # gridded horizontal
Step 5: air        # atmospheric region

Result: ua_tavg-al-hxy-air
```
**Use case**: Atmospheric circulation studies, jet stream analysis

### Surface Pressure
**Goal**: Instantaneous surface pressure globally

```yaml
Step 1: ps         # surface air pressure
Step 2: tpt        # time point (instantaneous)
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: ps_tpt-u-hxy-u
```
**Use case**: Weather forecasting, pressure system tracking

---

## Ocean Examples

### Sea Surface Temperature
**Goal**: Monthly average sea surface temperature

```yaml
Step 1: tos        # sea surface temperature
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: sea        # over ocean areas

Result: tos_tavg-u-hxy-sea
```
**Use case**: Climate change studies, coral bleaching analysis

### Ocean Heat Flux
**Goal**: Downward heat flux at sea surface

```yaml
Step 1: hfds       # downward heat flux at sea surface
Step 2: tavg       # time average
Step 3: u          # surface level
Step 4: hxy        # gridded horizontal
Step 5: sea        # over sea areas

Result: hfds_tavg-u-hxy-sea
```
**Use case**: Ocean energy balance, heat content studies

### Ocean Velocity
**Goal**: Monthly average eastward ocean velocity at all depths

```yaml
Step 1: uo         # eastward ocean velocity
Step 2: tavg       # time average
Step 3: ol         # all ocean levels
Step 4: hxy        # gridded horizontal
Step 5: sea        # ocean domain

Result: uo_tavg-ol-hxy-sea
```
**Use case**: Ocean circulation modeling, current analysis

---

## Precipitation Examples

### Monthly Precipitation
**Goal**: Monthly average precipitation rate globally

```yaml
Step 1: pr         # precipitation rate
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: pr_tavg-u-hxy-u
```
**Use case**: Climate monitoring, drought assessment

### Daily Maximum Rainfall
**Goal**: Daily maximum precipitation over land areas

```yaml
Step 1: pr         # precipitation rate
Step 2: tmax       # daily maximum
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: lnd        # over land areas

Result: pr_tmax-u-hxy-lnd
```
**Use case**: Flood risk assessment, extreme precipitation analysis

### Snowfall
**Goal**: Monthly snowfall rate globally

```yaml
Step 1: prsn       # snowfall rate
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: prsn_tavg-u-hxy-u
```
**Use case**: Snow water equivalent studies, winter precipitation

---

## Land Examples

### Soil Moisture
**Goal**: Monthly average soil moisture in all soil layers

```yaml
Step 1: mrsol      # soil moisture content
Step 2: tavg       # time average
Step 3: sl         # all soil levels
Step 4: hxy        # gridded horizontal
Step 5: lnd        # over land areas

Result: mrsol_tavg-sl-hxy-lnd
```
**Use case**: Drought monitoring, agricultural planning

### Vegetation Carbon
**Goal**: Annual average vegetation carbon content

```yaml
Step 1: cVeg       # vegetation carbon
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: lnd        # over land areas

Result: cVeg_tavg-u-hxy-lnd
```
**Use case**: Carbon cycle studies, forest monitoring

### Leaf Area Index
**Goal**: Monthly average leaf area index

```yaml
Step 1: lai        # leaf area index
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: lnd        # over land areas

Result: lai_tavg-u-hxy-lnd
```
**Use case**: Vegetation phenology, ecosystem modeling

---

## Sea Ice Examples

### Sea Ice Concentration
**Goal**: Monthly average sea ice concentration

```yaml
Step 1: siconc     # sea ice area fraction
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: siconc_tavg-u-hxy-u
```
**Use case**: Arctic/Antarctic ice studies, climate monitoring

### Sea Ice Thickness
**Goal**: Monthly average sea ice thickness

```yaml
Step 1: sithick    # sea ice thickness
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: si         # over sea ice

Result: sithick_tavg-u-hxy-si
```
**Use case**: Ice volume studies, navigation planning

---

## Radiation Examples

### Surface Solar Radiation
**Goal**: Daily average downward solar radiation at surface

```yaml
Step 1: rsds       # surface downwelling shortwave
Step 2: tavg       # time average
Step 3: u          # surface/unspecified
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: rsds_tavg-u-hxy-u
```
**Use case**: Solar energy studies, radiation balance

### Outgoing Longwave Radiation
**Goal**: Monthly average thermal radiation to space

```yaml
Step 1: rlut       # TOA outgoing longwave
Step 2: tavg       # time average
Step 3: u          # top of atmosphere
Step 4: hxy        # gridded horizontal
Step 5: u          # global/unmasked

Result: rlut_tavg-u-hxy-u
```
**Use case**: Earth's energy budget, greenhouse effect studies

---

## Complete Variable List

All 620+ root variables are available in the registry:

### Browse by Letter
- **A**: `abs550aer`, `acabf`, `agesno`, `airmass`, `albc`, `aoanh`, `arag`, `areacell`
- **B**: `bacc`, `baresoilFrac`, `basin`, `bigthetao`, `bldep`, `bry`, `bs550aer`
- **C**: `c13Land`, `cLand`, `cVeg`, `calc`, `ccb`, `chl`, `ci`, `cl`, `clt`, `co2`, `conccn`
- **And many more...**

### Find Variables
- **Full list**: [src-data/variable-root/](../../src-data/variable-root/)
- **Interactive search**: [Variable Registry Explorer](../web/branded-variable-builder.html)
- **By domain**: Use the category tabs above

## Common Patterns

| Variable Type | Typical Pattern |
|---------------|----------------|
| **Surface meteorology** | `{var}_tavg-h2m-hxy-u` |
| **3D atmosphere** | `{var}_tavg-al-hxy-air` |
| **Ocean surface** | `{var}_tavg-u-hxy-sea` |
| **Ocean 3D** | `{var}_tavg-ol-hxy-sea` |
| **Land surface** | `{var}_tavg-u-hxy-lnd` |
| **Soil layers** | `{var}_tavg-sl-hxy-lnd` |

## Next Steps

- **[Construction guide →](02_How%20to%20Construct/01_general_structure.md)**
- **[Component reference →](08_components/)**
- **[Interactive explorer →](../web/branded-variable-builder.html)**

---

*Pattern: root_temporal-vertical-horizontal-area*
