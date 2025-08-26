# Component Examples

## Role in CMIP Variable Construction

Component examples demonstrate how the five elements of branded identifiers work together to create unambiguous, physically consistent variable definitions for CMIP. These examples serve as:

- **Construction templates** for new variable development
- **Validation references** for checking component compatibility  
- **Best practice demonstrations** from operational CMIP usage
- **Quality assurance tools** for scientific consistency

Understanding component interactions ensures robust variable construction that works across all CMIP modeling centers.

## Complete Variable Breakdown

### Example: `abs550aer_tavg-u-hxy-u`

Let's examine how each component contributes to this aerosol absorption variable:

```
abs550aer_tavg-u-hxy-u
├── abs550aer        (variable-root)
├── tavg             (temporal-label)  
├── u                (vertical-label)
├── hxy              (horizontal-label)
└── u                (area-label)
```

=== "Variable Root: abs550aer"

    **Definition**: Aerosol absorption optical thickness at 550nm wavelength
    
    **Physical Meaning**: Atmospheric aerosol absorption coefficient
    
    **CMIP Applications**: 
    - Aerosol radiative forcing studies
    - Air quality assessments  
    - Climate model validation against satellite data
    
    **Units**: Dimensionless (optical depth)
    
    **Registry**: [abs550aer.json](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root)

=== "Temporal Label: tavg"

    **Definition**: Time-averaged data over sampling period
    
    **Physical Meaning**: Mean value computed from high-frequency data
    
    **CMIP Applications**:
    - Monthly climatologies for model comparison
    - Seasonal cycle analysis
    - Long-term trend detection
    
    **Processing**: Raw model output → temporal averaging → monthly/daily means
    
    **Registry**: [tavg.json](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/temporal-label)

=== "Vertical Label: u"

    **Definition**: Unspecified vertical coordinate (typically column-integrated)
    
    **Physical Meaning**: Total atmospheric column for aerosol absorption
    
    **CMIP Applications**:
    - Satellite comparison (column measurements)
    - Radiative forcing calculations
    - Global aerosol burden assessment
    
    **Alternative Options**: `al` (3D profiles), `h2m` (near-surface)
    
    **Registry**: [u.json](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/vertical-label)

=== "Horizontal Label: hxy"

    **Definition**: Regular latitude-longitude grid representation
    
    **Physical Meaning**: Spatially distributed data on model's native grid
    
    **CMIP Applications**:
    - Regional pattern analysis
    - Spatial model validation
    - Impact assessment studies
    
    **Grid Structure**: 2D arrays with lat/lon coordinates
    
    **Registry**: [hxy.json](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/horizontal-label)

=== "Area Label: u"

    **Definition**: Unmasked/global coverage (no spatial domain restriction)
    
    **Physical Meaning**: Aerosol absorption exists globally in atmosphere
    
    **CMIP Applications**:
    - Global aerosol studies
    - Earth system model validation
    - Climate forcing assessments
    
    **Coverage**: All grid points where atmosphere exists
    
    **Registry**: [u.json](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/area-label)

## Multi-Domain Variable Examples

=== "Atmospheric Variables"

    ### Surface Meteorology
    ```yaml
    tas_tpt-h2m-hxy-u:
      Description: Instantaneous 2m air temperature
      Usage: Weather prediction, model initialization
      Components:
        - tas: Near-surface air temperature
        - tpt: Time point (instantaneous)
        - h2m: 2-meter height above surface
        - hxy: Gridded spatial representation  
        - u: Global coverage
    ```

    ### 3D Atmospheric Fields  
    ```yaml
    ua_tavg-al-hxy-air:
      Description: Monthly mean eastward wind profiles
      Usage: Atmospheric circulation, jet stream analysis
      Components:
        - ua: Eastward wind component
        - tavg: Time averaged monthly means
        - al: All atmospheric model levels
        - hxy: Gridded horizontal structure
        - air: Atmospheric domain only
    ```

=== "Ocean Variables"

    ### Sea Surface Properties
    ```yaml
    tos_tavg-u-hxy-sea:
      Description: Monthly mean sea surface temperature
      Usage: Climate indices (El Niño), marine ecosystems
      Components:
        - tos: Sea surface temperature
        - tavg: Monthly time averages  
        - u: Surface level (unspecified depth)
        - hxy: Regular lat-lon ocean grid
        - sea: Ocean areas only
    ```

    ### Ocean Interior
    ```yaml
    thetao_tavg-ol-hxy-sea:
      Description: Ocean potential temperature profiles  
      Usage: Ocean heat content, circulation studies
      Components:
        - thetao: Ocean potential temperature
        - tavg: Monthly averages for climate analysis
        - ol: All ocean depth levels
        - hxy: 3D ocean grid structure
        - sea: Marine environment only
    ```

=== "Land Variables"

    ### Surface Land Processes
    ```yaml
    lai_tavg-u-hxy-lnd:
      Description: Monthly leaf area index
      Usage: Vegetation phenology, carbon cycle
      Components:
        - lai: Leaf area index
        - tavg: Monthly growing season averages
        - u: Surface canopy level
        - hxy: Terrestrial grid representation
        - lnd: Land areas only
    ```

    ### Subsurface Processes  
    ```yaml
    mrsol_tavg-sl-hxy-lnd:
      Description: Soil moisture content profiles
      Usage: Drought monitoring, agricultural impacts  
      Components:
        - mrsol: Soil moisture content
        - tavg: Monthly hydrological averages
        - sl: All soil model layers
        - hxy: Land surface grid
        - lnd: Terrestrial domain only
    ```

=== "Ice Variables"

    ### Sea Ice Properties
    ```yaml
    siconc_tavg-u-hxy-u:
      Description: Monthly sea ice concentration
      Usage: Arctic/Antarctic monitoring, shipping routes
      Components:
        - siconc: Sea ice area percentage  
        - tavg: Monthly averages for climate analysis
        - u: Sea surface level
        - hxy: Polar region grids
        - u: Global coverage (ice can occur anywhere)
    ```

    ### Ice-Specific Processes
    ```yaml  
    sithick_tavg-u-hxy-si:
      Description: Sea ice thickness  
      Usage: Ice volume calculations, climate trends
      Components:
        - sithick: Sea ice thickness
        - tavg: Monthly thickness averages
        - u: Ice surface level
        - hxy: Sea ice grid representation
        - si: Sea ice regions only
    ```

## Physical Consistency Rules

### Valid Component Interactions

**Domain-appropriate combinations**:
```yaml
Ocean variables:
  ✓ tos_tavg-u-hxy-sea      # Ocean temperature over sea
  ✓ uo_tavg-ol-hxy-sea      # Ocean currents in water column
  ✓ hfds_tavg-u-hxy-sea     # Heat flux into ocean

Land variables:
  ✓ mrsol_tavg-sl-hxy-lnd   # Soil moisture in ground  
  ✓ gpp_tavg-u-hxy-lnd      # Plant productivity over land
  ✓ mrro_tavg-u-hxy-lnd     # Surface runoff from land

Atmospheric variables:
  ✓ tas_tavg-h2m-hxy-u      # Air temperature in atmosphere
  ✓ pr_tavg-u-hxy-u         # Precipitation (global process)
  ✓ ua_tavg-al-hxy-air      # Wind in atmospheric column
```

### Invalid Component Combinations

**Domain mismatches**:
```yaml
❌ tos_tavg-al-hxy-air      # Sea temperature with air levels
❌ tas_tavg-ol-hxy-sea      # Air temperature with ocean levels  
❌ mrsol_tavg-u-hxy-sea     # Soil moisture over ocean
❌ siconc_tavg-sl-hxy-lnd   # Sea ice with soil coordinates
```

**Physically meaningless**:
```yaml
❌ ps_tsum-u-hxy-u          # Pressure "sum" (undefined)
❌ tas_tavg-ol-hxy-air      # Air temp with ocean coordinates  
❌ pr_tavg-sl-hxy-u         # Precipitation in soil layers
```

## Component Validation Workflow

### Interactive Validation

Use the [Variable Registry Explorer](../../web/branded-variable-builder.html) for:

1. **Real-time validation** of component combinations
2. **Autocomplete suggestions** from registry data  
3. **Physical consistency checking** 
4. **Variable definition lookup** with complete metadata

**Test these examples**:
- [abs550aer_tavg-u-hxy-u](../../web/branded-variable-builder.html?branding=abs550aer_tavg-u-hxy-u)
- [tas_tavg-h2m-hxy-u](../../web/branded-variable-builder.html?branding=tas_tavg-h2m-hxy-u)  
- [tos_tavg-u-hxy-sea](../../web/branded-variable-builder.html?branding=tos_tavg-u-hxy-sea)

### Registry Integration

Each validated component combination includes:

```json
{
  "id": "hfds_tavg-u-hxy-sea",
  "variable-root": "hfds",
  "temporal-label": "tavg", 
  "vertical-label": "u",
  "horizontal-label": "hxy",
  "area-label": "sea",
  "ui-label": "Downward Heat Flux at Sea Water Surface",
  "description": "Net flux of heat entering ocean...",
  "standard-name": "surface_downward_heat_flux_in_sea_water",
  "units": "W m-2"
}
```

## Quality Assurance Checklist

### Before Using Component Combinations

- **All components exist** in Variable Registry
- **Physical consistency** validated by domain experts
- **CMIP precedent** established in operational use
- **Standard format** follows exact separator pattern  
- **Documentation complete** with scientific descriptions

### Community Standards

- **CF Convention compliance** for all metadata
- **Version control** for component updates
- **Peer review** through CMIP working groups
- **Automated validation** in CMIP processing systems

## Next Steps

- **[Construction guide →](../02_How%20to%20Construct/01_general_structure.md)** - Build identifiers step-by-step
- **[Common patterns →](../02_How%20to%20Construct/patterns.md)** - Learn established patterns
- **[Interactive explorer →](../../web/branded-variable-builder.html)** - Try building variables

---

*Component examples demonstrate physically consistent variable construction for CMIP.*