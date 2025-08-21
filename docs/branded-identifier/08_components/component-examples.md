# Component Examples

This document provides detailed examples of how components work together in the Branded Identifier System.

## Complete Variable Example

Let's examine the variable `abs550aer_tavg-u-hxy-u` and break down each component:

### Variable Structure
```
abs550aer_tavg-u-hxy-u
└── abs550aer        (variable-root)
└── tavg             (temporal-label)
└── u                (area-label)
└── hxy              (horizontal-label)
└── u                (vertical-label)
```

### Component Breakdown

#### Variable Root: `abs550aer`
**File**: `src-data/variable-root/abs550aer.json`
> - **Purpose**: Aerosol absorption optical thickness at 550nm wavelength
> - **Physical Parameter**: Atmospheric aerosol absorption coefficient
> - **Base Units**: Dimensionless (1)

#### Temporal Label: `tavg`
**File**: `src-data/temporal-label/tavg.json`
> - **Purpose**: Time-averaged data
> - **Description**: Data averaged over the temporal sampling period
> - **Usage**: Monthly, daily, or other regular time averages

#### Area Label: `u`
**File**: `src-data/area-label/u.json`
> - **Purpose**: Unmasked area
> - **Description**: No spatial masking applied - global coverage
> - **Alternative Options**:
>     - `lnd` - Land areas only
>     - `sea` - Ocean/sea areas only
>     - `ice` - Ice-covered areas only

#### Horizontal Label: `hxy`
**File**: `src-data/horizontal-label/hxy.json`
> - **Purpose**: Gridded horizontal representation
> - **Description**: Regular latitude-longitude grid
> - **Alternative Options**:
>     - `hys` - Meridional section (latitude-depth)
>     - `ht` - Transect along specific path

#### Vertical Label: `u`
**File**: `src-data/vertical-label/u.json`
> - **Purpose**: Unspecified vertical coordinate
> - **Description**: Typically indicates surface or column-integrated values
> - **Alternative Options**:
>     - `al` - All atmospheric levels
>     - `ol` - All ocean levels
>     - `plev` - Pressure levels

## More Variable Examples

=== "Temperature Variables"

    #### Surface Air Temperature: `tas_tpt-h2m-hxy-u`
    ```yaml
    variable-root: tas (Near-surface air temperature)
    temporal-label: tpt (Time point - instantaneous)
    area-label: h2m (2-meter height)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Unspecified/surface)
    ```

    #### Maximum Daily Temperature: `tas_tmax-h2m-hxy-u`
    ```yaml
    variable-root: tas (Near-surface air temperature)
    temporal-label: tmax (Daily maximum)
    area-label: h2m (2-meter height)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Unspecified/surface)
    ```

    #### 3D Temperature: `ta_tavg-al-hxy-air`
    ```yaml
    variable-root: ta (Air temperature)
    temporal-label: tavg (Time average)
    area-label: al (All atmospheric levels)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: air (Atmospheric levels)
    ```

=== "Precipitation Variables"

    #### Monthly Precipitation: `pr_tavg-u-hxy-u`
    ```yaml
    variable-root: pr (Precipitation rate)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked - global)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Surface)
    ```

    #### Snow Precipitation: `prsn_tavg-u-hxy-u`
    ```yaml
    variable-root: prsn (Snowfall rate)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked - global)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Surface)
    ```

    #### Maximum Daily Precipitation: `pr_tmax-u-hxy-u`
    ```yaml
    variable-root: pr (Precipitation rate)
    temporal-label: tmax (Daily maximum)
    area-label: u (Unmasked - global)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Surface)
    ```

=== "Ocean Variables"

    #### Sea Surface Temperature: `tos_tavg-u-hxy-sea`
    ```yaml
    variable-root: tos (Sea surface temperature)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: sea (Sea surface)
    ```

    #### Ocean Temperature Profile: `thetao_tavg-ol-hxy-sea`
    ```yaml
    variable-root: thetao (Sea water potential temperature)
    temporal-label: tavg (Time average)
    area-label: ol (All ocean levels)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: sea (Ocean levels)
    ```

    #### Ocean Salinity: `so_tavg-ol-hxy-sea`
    ```yaml
    variable-root: so (Sea water salinity)
    temporal-label: tavg (Time average)
    area-label: ol (All ocean levels)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: sea (Ocean levels)
    ```

=== "Atmospheric Variables"

    #### Wind Speed: `sfcWind_tavg-h10m-hxy-u`
    ```yaml
    variable-root: sfcWind (Near-surface wind speed)
    temporal-label: tavg (Time average)
    area-label: h10m (10-meter height)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Unspecified/surface)
    ```

    #### Zonal Wind: `ua_tavg-al-hxy-air`
    ```yaml
    variable-root: ua (Eastward wind)
    temporal-label: tavg (Time average)
    area-label: al (All atmospheric levels)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: air (Atmospheric levels)
    ```

    #### Surface Pressure: `ps_tavg-u-hxy-u`
    ```yaml
    variable-root: ps (Surface air pressure)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Surface)
    ```

=== "Land Variables"

    #### Soil Temperature: `tsl_tavg-sl-hxy-lnd`
    ```yaml
    variable-root: tsl (Soil temperature)
    temporal-label: tavg (Time average)
    area-label: sl (All soil levels)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: lnd (Land areas)
    ```

    #### Soil Moisture: `mrsol_tavg-sl-hxy-lnd`
    ```yaml
    variable-root: mrsol (Soil moisture content)
    temporal-label: tavg (Time average)
    area-label: sl (All soil levels)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: lnd (Land areas)
    ```

    #### Vegetation Carbon: `cVeg_tavg-u-hxy-lnd`
    ```yaml
    variable-root: cVeg (Vegetation carbon content)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: lnd (Land areas)
    ```

=== "Ice Variables"

    #### Sea Ice Concentration: `siconc_tavg-u-hxy-u`
    ```yaml
    variable-root: siconc (Sea ice area percentage)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: u (Surface)
    ```

    #### Sea Ice Thickness: `sithick_tavg-u-hxy-si`
    ```yaml
    variable-root: sithick (Sea ice thickness)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: si (Sea ice)
    ```

    #### Land Ice Thickness: `lithk_tavg-u-hxy-is`
    ```yaml
    variable-root: lithk (Land ice thickness)
    temporal-label: tavg (Time average)
    area-label: u (Unmasked)
    horizontal-label: hxy (Gridded horizontal)
    vertical-label: is (Ice sheet)
    ```

## Component Combination Rules

### Naming Convention
Variables follow the pattern:
```
[variable-root]_[temporal-label]-[area-label]-[horizontal-label]-[vertical-label]
```

### Required Components
Every variable must specify:
1. **Variable Root**: The base physical parameter
2. **Temporal Label**: Time sampling method
3. **Area Label**: Spatial masking (can be 'u' for unmasked)
4. **Horizontal Label**: Horizontal representation
5. **Vertical Label**: Vertical coordinate system

### Optional Components
Additional metadata is provided through:
> - **Cell Methods**: Aggregation operations
> - **Coordinates**: Coordinate system details
> - **Dimensions**: Dimensional specifications

### Physical Consistency
Component combinations must be physically meaningful:
> - Ocean variables (`sea`, `ol`) cannot use atmospheric vertical labels (`al`, `air`)
> - Surface variables typically use `u` for vertical label
> - Height-specific variables use appropriate area labels (`h2m`, `h10m`)

## Validation Examples

### Valid Combinations
```
✓ tas_tavg-h2m-hxy-u          (Surface temperature, time-averaged)
✓ pr_tmax-u-hxy-u             (Maximum precipitation rate)
✓ thetao_tavg-ol-hxy-sea      (Ocean temperature at all levels)
✓ ua_tpt-al-hxy-air           (Instantaneous wind at all atmospheric levels)
```

### Invalid Combinations
```
✗ tas_tavg-ol-hxy-u           (Temperature with ocean levels - inconsistent)
✗ tos_tavg-al-hxy-air         (Sea temperature with atmospheric levels)
✗ pr_tavg-h100km-hxy-u        (Precipitation at 100km height - unrealistic)
```

## Supporting Component Examples

### Cell Methods
> - `amn-twm`: Area mean, time mean
> - `amx-twm`: Area mean, time maximum  
> - `asm-twm`: Area sum, time mean

### CMIP6 Tables
> - `AERmon`: Aerosol monthly output
> - `Amon`: Atmospheric monthly output
> - `Omon`: Ocean monthly output
> - `LImon`: Land ice monthly output

### Coordinates
> - `longitude`: East-west spatial coordinate
> - `latitude`: North-south spatial coordinate
> - `time`: Temporal coordinate
> - `plev`: Pressure level coordinate
> - `height`: Height coordinate

## Usage in Variable Files

Each complete variable file includes references to all relevant components:

```json
{
    "id": "abs550aer_tavg-u-hxy-u",
    "validation-key": "abs550aer_tavg-u-hxy-u",
    "variable-root": "abs550aer",
    "temporal-label": "tavg",
    "area-label": "u",
    "horizontal-label": "hxy",
    "vertical-label": "u",
    "cell-methods": "amn-twm",
    "dimensions": ["longitude", "latitude", "time", "lambda550nm"],
    "standard-name": "atmosphere_absorption_optical_thickness_due_to_ambient_aerosol_particles",
    "units": "1",
    "description": "Optical thickness of atmospheric aerosols at wavelength 550 nanometers."
}
```

## Navigation

> - [Main Documentation](index.md) - Complete system overview
> - [Tutorial Series](tutorial-index.md) - University-style learning
> - [Components Table](components-table.md) - Component reference table
> - [../../src-data/](../../src-data/) - Source component definitions

> ---

*These examples demonstrate how the Branded Identifier System combines standardized components to create unique, meaningful variable identifiers while maintaining physical consistency and registry standards.*