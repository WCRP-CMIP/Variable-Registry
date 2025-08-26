# Component Examples

This document provides detailed examples of how components work together in the Branded Identifier System.

## Complete Variable Example

Let's examine the variable `abs550aer_tavg-u-hxy-u` and break down each component:

### Variable Structure
```
abs550aer_tavg-u-hxy-u
└── abs550aer        (variable-root)
└── tavg             (temporal-label)
└── u                (vertical-label)
└── hxy              (horizontal-label)
└── u                (area-label)
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

#### Vertical Label: `u`
**File**: `src-data/vertical-label/u.json`
> - **Purpose**: Unspecified vertical coordinate
> - **Description**: Typically indicates surface or column-integrated values
> - **Alternative Options**:
>     - `al` - All atmospheric levels
>     - `ol` - All ocean levels
>     - `h2m` - 2-meter height

#### Horizontal Label: `hxy`
**File**: `src-data/horizontal-label/hxy.json`
> - **Purpose**: Gridded horizontal representation
> - **Description**: Regular latitude-longitude grid
> - **Alternative Options**:
>     - `hm` - Global mean
>     - `hy` - Zonal mean

#### Area Label: `u`
**File**: `src-data/area-label/u.json`
> - **Purpose**: Unmasked area
> - **Description**: No spatial masking applied - global coverage
> - **Alternative Options**:
>     - `lnd` - Land areas only
>     - `sea` - Ocean/sea areas only
>     - `air` - Atmospheric region

## More Variable Examples

=== "Temperature Variables"

    #### Surface Air Temperature: `tas_tpt-h2m-hxy-u`
    ```yaml
    variable-root: tas (Near-surface air temperature)
    temporal-label: tpt (Time point - instantaneous)
    vertical-label: h2m (2-meter height)
    horizontal-label: hxy (Gridded horizontal)
    area-label: u (Global/unmasked)
    ```

    #### Ocean Heat Flux: `hfds_tavg-u-hxy-sea`
    ```yaml
    variable-root: hfds (Downward heat flux at sea surface)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface level)
    horizontal-label: hxy (Gridded horizontal)
    area-label: sea (Over sea areas)
    ```

=== "Precipitation Variables"

    #### Monthly Precipitation: `pr_tavg-u-hxy-u`
    ```yaml
    variable-root: pr (Precipitation rate)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface/unspecified)
    horizontal-label: hxy (Gridded horizontal)
    area-label: u (Global/unmasked)
    ```

    #### Snow Precipitation: `prsn_tavg-u-hxy-u`
    ```yaml
    variable-root: prsn (Snowfall rate)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface/unspecified)
    horizontal-label: hxy (Gridded horizontal)
    area-label: u (Global/unmasked)
    ```

=== "Ocean Variables"

    #### Sea Surface Temperature: `tos_tavg-u-hxy-sea`
    ```yaml
    variable-root: tos (Sea surface temperature)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface/unspecified)
    horizontal-label: hxy (Gridded horizontal)
    area-label: sea (Over ocean areas)
    ```

    #### Ocean Velocity: `uo_tavg-ol-hxy-sea`
    ```yaml
    variable-root: uo (Eastward ocean velocity)
    temporal-label: tavg (Time average)
    vertical-label: ol (All ocean levels)
    horizontal-label: hxy (Gridded horizontal)
    area-label: sea (Ocean domain)
    ```

=== "Land Variables"

    #### Soil Moisture: `mrsol_tavg-sl-hxy-lnd`
    ```yaml
    variable-root: mrsol (Soil moisture content)
    temporal-label: tavg (Time average)
    vertical-label: sl (All soil levels)
    horizontal-label: hxy (Gridded horizontal)
    area-label: lnd (Over land areas)
    ```

    #### Vegetation Carbon: `cVeg_tavg-u-hxy-lnd`
    ```yaml
    variable-root: cVeg (Vegetation carbon)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface/unspecified)
    horizontal-label: hxy (Gridded horizontal)
    area-label: lnd (Over land areas)
    ```

=== "Ice Variables"

    #### Sea Ice Concentration: `siconc_tavg-u-hxy-u`
    ```yaml
    variable-root: siconc (Sea ice area fraction)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface/unspecified)
    horizontal-label: hxy (Gridded horizontal)
    area-label: u (Global/unmasked)
    ```

    #### Sea Ice Thickness: `sithick_tavg-u-hxy-si`
    ```yaml
    variable-root: sithick (Sea ice thickness)
    temporal-label: tavg (Time average)
    vertical-label: u (Surface/unspecified)
    horizontal-label: hxy (Gridded horizontal)
    area-label: si (Over sea ice)
    ```

## Component Combination Rules

### Pattern
```
[variable-root]_[temporal-label]-[vertical-label]-[horizontal-label]-[area-label]
```

### Physical Consistency Rules
- Ocean variables must use ocean-compatible area labels (`sea`)
- Land variables must use land-compatible area labels (`lnd`)
- Surface variables typically use `u` for vertical label
- 3D variables use level-specific vertical labels (`al`, `ol`)

### Valid Combinations
```
✓ hfds_tavg-u-hxy-sea        (Heat flux at sea surface)
✓ tas_tmax-h2m-hxy-u         (Maximum temperature at 2m)
✓ uo_tavg-ol-hxy-sea         (Ocean velocity at all levels)
✓ mrsol_tavg-sl-hxy-lnd      (Soil moisture in all layers)
```

### Invalid Combinations
```
✗ tos_tavg-al-hxy-air        (Sea temperature with atmospheric levels)
✗ ua_tavg-ol-hxy-sea         (Atmospheric wind with ocean levels)
✗ siconc_tavg-sl-hxy-lnd     (Sea ice with soil levels)
```

## Interactive Explorer

Use the [Variable Registry Explorer](../web/branded-variable-builder.html) to:
- Build identifiers interactively
- Validate component combinations
- Explore all available components
- See real variable examples

Try these examples:
- [hfds_tavg-u-hxy-sea](../web/branded-variable-builder.html?branding=hfds_tavg-u-hxy-sea)
- [tas_tmax-h2m-hxy-u](../web/branded-variable-builder.html?branding=tas_tmax-h2m-hxy-u)
- [abs550aer_tavg-u-hxy-u](../web/branded-variable-builder.html?branding=abs550aer_tavg-u-hxy-u)

## Supporting Variable Data

Each complete variable includes:

```json
{
    "id": "hfds_tavg-u-hxy-sea",
    "validation-key": "hfds_tavg-u-hxy-sea",
    "variable-root": "hfds",
    "temporal-label": "tavg",
    "vertical-label": "u",
    "horizontal-label": "hxy",
    "area-label": "sea",
    "ui-label": "Downward Heat Flux at Sea Water Surface",
    "description": "Net flux of heat entering the liquid water column...",
    "standard-name": "surface_downward_heat_flux_in_sea_water",
    "units": "W m-2"
}
```

## Next Steps

- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)**
- **[Component reference →](../08_components/)**
- **[Root variables →](../05-root-variables.md)**

---

*Pattern: root_temporal-vertical-horizontal-area*
