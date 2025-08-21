# Root Variables Registry

This comprehensive registry contains all available root variables organized by domain and functionality. Root variables represent the fundamental physical parameters that can be combined with other components to create complete branded identifiers.

---

## Root Variable Categories

=== "Temperature Variables"

    ### Atmospheric Temperature

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `ta` | Air Temperature | air-temperature | Air temperature in 3D atmosphere | Atmosphere | `ta_tavg-al-hxy-air` |
    | `tas` | Near-Surface Air Temperature | air-temperature | Air temperature near surface (2m) | Atmosphere | `tas_tavg-h2m-hxy-u` |
    | `tatp` | Air Temperature at Tropopause | air-temperature | Temperature at tropopause level | Atmosphere | `tatp_tavg-u-hxy-u` |

    ### Ocean Temperature

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `tos` | Sea Surface Temperature | sea-surface-temperature | Temperature at ocean surface | Ocean Surface | `tos_tavg-u-hxy-sea` |
    | `thetao` | Sea Water Potential Temperature | sea-water-potential-temperature | Potential temperature in ocean | Ocean 3D | `thetao_tavg-ol-hxy-sea` |
    | `thetaot` | Ocean Temperature Tendency | sea-water-potential-temperature-tendency | Rate of change of ocean temperature | Ocean 3D | `thetaot_tavg-ol-hxy-sea` |

    ### Land Temperature

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `ts` | Surface Temperature | surface-temperature | Temperature at land/sea surface | Surface | `ts_tavg-u-hxy-u` |
    | `tsl` | Soil Temperature | soil-temperature | Temperature in soil layers | Land/Soil | `tsl_tavg-sl-hxy-lnd` |
    | `tslsi` | Snow/Ice Surface Temperature | surface-temperature | Temperature of snow/ice surface | Ice/Snow | `tslsi_tavg-u-hxy-u` |

    ### Ice Temperature

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `litemptop` | Land Ice Surface Temperature | temperature-at-top-of-ice-sheet-model | Surface temperature of ice sheet | Land Ice | `litemptop_tavg-u-hxy-is` |
    | `litempbot` | Land Ice Base Temperature | temperature-at-base-of-ice-sheet-model | Base temperature of ice sheet | Land Ice | `litempbot_tavg-u-hxy-is` |
    | `sitempbot` | Sea Ice Bottom Temperature | sea-ice-temperature-at-interface | Temperature at sea ice bottom | Sea Ice | `sitempbot_tavg-u-hxy-si` |
    | `sitemptop` | Sea Ice Surface Temperature | surface-temperature | Temperature at sea ice surface | Sea Ice | `sitemptop_tavg-u-hxy-si` |

=== "Precipitation Variables"

    ### Precipitation Types

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `pr` | Precipitation | precipitation-flux | Total precipitation rate | Atmosphere | `pr_tavg-u-hxy-u` |
    | `prc` | Convective Precipitation | convective-precipitation-flux | Convective precipitation only | Atmosphere | `prc_tavg-u-hxy-u` |
    | `prsn` | Snowfall | snowfall-flux | Snowfall rate | Atmosphere | `prsn_tavg-u-hxy-u` |
    | `prra` | Rainfall | rainfall-flux | Liquid precipitation rate | Atmosphere | `prra_tavg-u-hxy-u` |
    | `prrsn` | Solid Precipitation | solid-precipitation-flux | All solid precipitation | Atmosphere | `prrsn_tavg-u-hxy-u` |

    ### Isotopic Precipitation

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `pr17o` | Precipitation H₂¹⁷O | precipitation-flux-17o | Precipitation with O-17 isotope | Atmosphere | `pr17o_tavg-u-hxy-u` |
    | `pr18o` | Precipitation H₂¹⁸O | precipitation-flux-18o | Precipitation with O-18 isotope | Atmosphere | `pr18o_tavg-u-hxy-u` |
    | `pr2h` | Precipitation HDO | precipitation-flux-2h | Precipitation with deuterium | Atmosphere | `pr2h_tavg-u-hxy-u` |
    | `prsn18o` | Snowfall H₂¹⁸O | snowfall-flux-18o | Snowfall with O-18 isotope | Atmosphere | `prsn18o_tavg-u-hxy-u` |
    | `prsn2h` | Snowfall HDO | snowfall-flux-2h | Snowfall with deuterium | Atmosphere | `prsn2h_tavg-u-hxy-u` |

    ### Specialized Precipitation

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `prveg` | Precipitation on Vegetation | precipitation-flux-onto-canopy | Precip intercepted by vegetation | Land | `prveg_tavg-u-hxy-lnd` |
    | `prsnc` | Snow Precipitation (Convective) | convective-snowfall-flux | Convective snowfall only | Atmosphere | `prsnc_tavg-u-hxy-u` |
    | `prsnsn` | Snow on Snow | snowfall-flux | Snowfall onto existing snow | Land/Snow | `prsnsn_tavg-u-hxy-lnd` |

=== "Wind Variables"

    ### Horizontal Wind Components

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `ua` | Eastward Wind | eastward-wind | Eastward component of wind | Atmosphere | `ua_tavg-al-hxy-air` |
    | `va` | Northward Wind | northward-wind | Northward component of wind | Atmosphere | `va_tavg-al-hxy-air` |
    | `uas` | Surface Eastward Wind | eastward-wind | Near-surface eastward wind | Atmosphere | `uas_tavg-h10m-hxy-u` |
    | `vas` | Surface Northward Wind | northward-wind | Near-surface northward wind | Atmosphere | `vas_tavg-h10m-hxy-u` |

    ### Wind Speed and Derived Quantities

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `sfcWind` | Near-Surface Wind Speed | wind-speed | Wind speed near surface | Atmosphere | `sfcWind_tavg-h10m-hxy-u` |
    | `wap` | Vertical Velocity | lagrangian-tendency-of-air-pressure | Vertical motion (omega) | Atmosphere | `wap_tavg-al-hxy-air` |
    | `wa` | Upward Air Velocity | upward-air-velocity | Vertical velocity in m/s | Atmosphere | `wa_tavg-al-hxy-air` |
    | `wsg` | Wind Gust Speed | wind-speed-of-gust | Maximum wind gust speed | Atmosphere | `wsg_tmax-h10m-hxy-u` |

    ### Wind Stress

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `tauu` | Surface Wind Stress (Eastward) | surface-downward-eastward-stress | Eastward surface stress | Surface | `tauu_tavg-u-hxy-u` |
    | `tauv` | Surface Wind Stress (Northward) | surface-downward-northward-stress | Northward surface stress | Surface | `tauv_tavg-u-hxy-u` |
    | `tauuo` | Ocean Surface Stress (Eastward) | surface-downward-x-stress | Ocean eastward stress | Ocean | `tauuo_tavg-u-hxy-sea` |
    | `tauvo` | Ocean Surface Stress (Northward) | surface-downward-y-stress | Ocean northward stress | Ocean | `tauvo_tavg-u-hxy-sea` |

=== "Ocean Variables"

    ### Ocean Circulation

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `uo` | Eastward Ocean Velocity | sea-water-x-velocity | Eastward ocean current | Ocean 3D | `uo_tavg-ol-hxy-sea` |
    | `vo` | Northward Ocean Velocity | sea-water-y-velocity | Northward ocean current | Ocean 3D | `vo_tavg-ol-hxy-sea` |
    | `wo` | Upward Ocean Velocity | upward-sea-water-velocity | Vertical ocean velocity | Ocean 3D | `wo_tavg-ol-hxy-sea` |
    | `uos` | Surface Eastward Ocean Velocity | surface-eastward-sea-water-velocity | Surface eastward current | Ocean Surface | `uos_tavg-u-hxy-sea` |
    | `vos` | Surface Northward Ocean Velocity | surface-northward-sea-water-velocity | Surface northward current | Ocean Surface | `vos_tavg-u-hxy-sea` |

    ### Ocean Properties

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `so` | Sea Water Salinity | sea-water-salinity | Ocean salinity | Ocean 3D | `so_tavg-ol-hxy-sea` |
    | `sos` | Sea Surface Salinity | sea-surface-salinity | Surface ocean salinity | Ocean Surface | `sos_tavg-u-hxy-sea` |
    | `zos` | Sea Surface Height | sea-surface-height-above-geoid | Dynamic sea surface height | Ocean Surface | `zos_tavg-u-hxy-sea` |
    | `zostoga` | Global Mean Sea Level | global-average-sea-level-change | Global mean sea level | Ocean | `zostoga_tavg-u-hm-sea` |

    ### Ocean Biogeochemistry

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `o2` | Dissolved Oxygen | mole-concentration-of-dissolved-molecular-oxygen-in-sea-water | Ocean oxygen content | Ocean 3D | `o2_tavg-ol-hxy-sea` |
    | `no3` | Nitrate | mole-concentration-of-nitrate-in-sea-water | Ocean nitrate concentration | Ocean 3D | `no3_tavg-ol-hxy-sea` |
    | `po4` | Phosphate | mole-concentration-of-phosphate-in-sea-water | Ocean phosphate concentration | Ocean 3D | `po4_tavg-ol-hxy-sea` |
    | `si` | Silicate | mole-concentration-of-silicate-in-sea-water | Ocean silicate concentration | Ocean 3D | `si_tavg-ol-hxy-sea` |
    | `nh4` | Ammonium | mole-concentration-of-ammonium-in-sea-water | Ocean ammonium concentration | Ocean 3D | `nh4_tavg-ol-hxy-sea` |

    ### Marine Ecosystem

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `chl` | Chlorophyll | mass-concentration-of-chlorophyll-in-sea-water | Chlorophyll concentration | Ocean 3D | `chl_tavg-ol-hxy-sea` |
    | `phyc` | Phytoplankton Carbon | mole-concentration-of-phytoplankton-expressed-as-carbon-in-sea-water | Phytoplankton carbon | Ocean 3D | `phyc_tavg-ol-hxy-sea` |
    | `zooc` | Zooplankton Carbon | mole-concentration-of-zooplankton-expressed-as-carbon-in-sea-water | Zooplankton carbon | Ocean 3D | `zooc_tavg-ol-hxy-sea` |
    | `pp` | Primary Production | net-primary-mole-productivity-of-carbon-by-phytoplankton | Ocean primary productivity | Ocean 3D | `pp_tavg-ol-hxy-sea` |

=== "Humidity Variables"

    ### Water Vapor Content

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `hus` | Specific Humidity | specific-humidity | Water vapor mixing ratio | Atmosphere | `hus_tavg-al-hxy-air` |
    | `huss` | Surface Specific Humidity | specific-humidity | Near-surface specific humidity | Atmosphere | `huss_tavg-h2m-hxy-u` |
    | `hur` | Relative Humidity | relative-humidity | Relative humidity | Atmosphere | `hur_tavg-al-hxy-air` |
    | `hurs` | Surface Relative Humidity | relative-humidity | Near-surface relative humidity | Atmosphere | `hurs_tavg-h2m-hxy-u` |

    ### Integrated Water Vapor

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `prw` | Precipitable Water | atmosphere-water-vapor-content | Total column water vapor | Atmosphere | `prw_tavg-u-hxy-u` |
    | `clwvi` | Cloud Liquid Water Path | atmosphere-cloud-liquid-water-content | Integrated cloud liquid water | Atmosphere | `clwvi_tavg-u-hxy-u` |
    | `clivi` | Cloud Ice Water Path | atmosphere-cloud-ice-content | Integrated cloud ice water | Atmosphere | `clivi_tavg-u-hxy-u` |

=== "Pressure Variables"

    ### Atmospheric Pressure

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `ps` | Surface Air Pressure | surface-air-pressure | Pressure at surface | Atmosphere | `ps_tavg-u-hxy-u` |
    | `psl` | Sea Level Pressure | air-pressure-at-mean-sea-level | Pressure reduced to sea level | Atmosphere | `psl_tavg-u-hxy-u` |
    | `pfull` | Pressure at Model Levels | air-pressure | Pressure at model levels | Atmosphere | `pfull_tavg-al-hxy-u` |
    | `phalf` | Pressure at Half Levels | air-pressure-at-half-levels | Pressure at layer interfaces | Atmosphere | `phalf_tavg-alh-hxy-u` |

=== "Land Variables"

    ### Vegetation Properties

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `lai` | Leaf Area Index | leaf-area-index | One-sided leaf area per unit area | Land | `lai_tavg-u-hxy-lnd` |
    | `vegHeight` | Vegetation Height | vegetation-height | Height of vegetation canopy | Land | `vegHeight_tavg-u-hxy-lnd` |
    | `vegFrac` | Vegetation Fraction | vegetation-area-fraction | Fraction covered by vegetation | Land | `vegFrac_tavg-u-hxy-u` |
    | `treeFrac` | Tree Fraction | tree-area-fraction | Fraction covered by trees | Land | `treeFrac_tavg-u-hxy-u` |
    | `shrubFrac` | Shrub Fraction | shrub-area-fraction | Fraction covered by shrubs | Land | `shrubFrac_tavg-u-hxy-u` |
    | `grassFrac` | Grass Fraction | grass-area-fraction | Fraction covered by grass | Land | `grassFrac_tavg-u-hxy-u` |
    | `cropFrac` | Crop Fraction | crop-area-fraction | Fraction covered by crops | Land | `cropFrac_tavg-u-hxy-u` |

    ### Soil Properties

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `mrsol` | Soil Moisture | moisture-content-of-soil-layer | Soil moisture in layers | Land/Soil | `mrsol_tavg-sl-hxy-lnd` |
    | `mrso` | Total Soil Moisture | soil-moisture-content | Total column soil moisture | Land | `mrso_tavg-u-hxy-lnd` |
    | `mrsos` | Surface Soil Moisture | moisture-content-of-soil-layer | Near-surface soil moisture | Land | `mrsos_tavg-u-hxy-lnd` |
    | `mrfso` | Frozen Soil Moisture | frozen-water-content-of-soil-layer | Frozen moisture in soil | Land/Soil | `mrfso_tavg-u-hxy-lnd` |

    ### Carbon Cycle

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `gpp` | Gross Primary Productivity | gross-primary-productivity-of-carbon | Plant carbon uptake | Land | `gpp_tavg-u-hxy-lnd` |
    | `npp` | Net Primary Productivity | net-primary-productivity-of-carbon | Plant net carbon production | Land | `npp_tavg-u-hxy-lnd` |
    | `ra` | Autotrophic Respiration | plant-respiration-carbon-flux | Plant respiration | Land | `ra_tavg-u-hxy-lnd` |
    | `rh` | Heterotrophic Respiration | heterotrophic-respiration-carbon-flux | Soil/litter respiration | Land | `rh_tavg-u-hxy-lnd` |
    | `nbp` | Net Biome Productivity | surface-net-downward-mass-flux-of-carbon-dioxide-expressed-as-carbon-due-to-all-land-processes | Net carbon exchange | Land | `nbp_tavg-u-hxy-lnd` |

    ### Carbon Pools

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `cVeg` | Vegetation Carbon | vegetation-carbon-content | Carbon in vegetation | Land | `cVeg_tavg-u-hxy-lnd` |
    | `cLitter` | Litter Carbon | litter-carbon-content | Carbon in litter | Land | `cLitter_tavg-u-hxy-lnd` |
    | `cSoil` | Soil Carbon | soil-carbon-content | Carbon in soil | Land/Soil | `cSoil_tavg-sl-hxy-lnd` |
    | `cLeaf` | Leaf Carbon | leaf-carbon-content | Carbon in leaves | Land | `cLeaf_tavg-u-hxy-lnd` |
    | `cRoot` | Root Carbon | root-carbon-content | Carbon in roots | Land | `cRoot_tavg-u-hxy-lnd` |
    | `cStem` | Stem Carbon | wood-carbon-content | Carbon in wood/stems | Land | `cStem_tavg-u-hxy-lnd` |

=== "Sea Ice Variables"

    ### Sea Ice Properties

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `siconc` | Sea Ice Concentration | sea-ice-area-fraction | Fraction of area covered by ice | Sea Ice | `siconc_tavg-u-hxy-u` |
    | `sithick` | Sea Ice Thickness | sea-ice-thickness | Thickness of sea ice | Sea Ice | `sithick_tavg-u-hxy-si` |
    | `siage` | Sea Ice Age | age-of-sea-ice | Age of sea ice | Sea Ice | `siage_tavg-u-hxy-si` |
    | `simass` | Sea Ice Mass | sea-ice-mass | Mass of sea ice | Sea Ice | `simass_tavg-u-hxy-sea` |
    | `sivol` | Sea Ice Volume | sea-ice-volume | Volume of sea ice | Sea Ice | `sivol_tavg-u-hm-u` |

    ### Sea Ice Dynamics

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `siu` | Sea Ice Velocity (Eastward) | sea-ice-x-velocity | Eastward ice velocity | Sea Ice | `siu_tavg-u-hxy-si` |
    | `siv` | Sea Ice Velocity (Northward) | sea-ice-y-velocity | Northward ice velocity | Sea Ice | `siv_tavg-u-hxy-si` |
    | `sispeed` | Sea Ice Speed | sea-ice-speed | Magnitude of ice velocity | Sea Ice | `sispeed_tavg-u-hxy-si` |
    | `sistrxdtop` | Ice Stress (X) | surface-downward-x-stress | Eastward ice stress at top | Sea Ice | `sistrxdtop_tavg-u-hxy-si` |
    | `sistrydtop` | Ice Stress (Y) | surface-downward-y-stress | Northward ice stress at top | Sea Ice | `sistrydtop_tavg-u-hxy-si` |

=== "Land Ice Variables"

    ### Ice Sheet Properties

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `lithk` | Land Ice Thickness | land-ice-thickness | Thickness of ice sheet | Land Ice | `lithk_tavg-u-hxy-is` |
    | `litemptop` | Ice Surface Temperature | temperature-at-top-of-ice-sheet-model | Surface temperature of ice | Land Ice | `litemptop_tavg-u-hxy-is` |
    | `litempbot` | Ice Base Temperature | temperature-at-base-of-ice-sheet-model | Base temperature of ice | Land Ice | `litempbot_tavg-u-hxy-is` |

    ### Ice Sheet Dynamics

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `xvelsurf` | Ice Surface Velocity (X) | land-ice-surface-x-velocity | Surface eastward velocity | Land Ice | `xvelsurf_tavg-u-hxy-is` |
    | `yvelsurf` | Ice Surface Velocity (Y) | land-ice-surface-y-velocity | Surface northward velocity | Land Ice | `yvelsurf_tavg-u-hxy-is` |
    | `xvelbase` | Ice Base Velocity (X) | land-ice-basal-x-velocity | Base eastward velocity | Land Ice | `xvelbase_tavg-u-hxy-is` |
    | `yvelbase` | Ice Base Velocity (Y) | land-ice-basal-y-velocity | Base northward velocity | Land Ice | `yvelbase_tavg-u-hxy-is` |
    | `zvelsurf` | Ice Surface Velocity (Z) | land-ice-surface-upward-velocity | Surface upward velocity | Land Ice | `zvelsurf_tavg-u-hxy-is` |

=== "Radiation Variables"

    ### Shortwave Radiation

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `rsdt` | TOA Incident Solar Radiation | toa-incoming-shortwave-flux | Solar radiation at top of atmosphere | TOA | `rsdt_tavg-u-hxy-u` |
    | `rsut` | TOA Outgoing Shortwave | toa-outgoing-shortwave-flux | Reflected solar at TOA | TOA | `rsut_tavg-u-hxy-u` |
    | `rsds` | Surface Downwelling Shortwave | surface-downwelling-shortwave-flux | Solar reaching surface | Surface | `rsds_tavg-u-hxy-u` |
    | `rsus` | Surface Upwelling Shortwave | surface-upwelling-shortwave-flux | Solar reflected by surface | Surface | `rsus_tavg-u-hxy-u` |
    | `rss` | Net Surface Shortwave | surface-net-downward-shortwave-flux | Net solar at surface | Surface | `rss_tavg-u-hxy-u` |

    ### Longwave Radiation

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `rlut` | TOA Outgoing Longwave | toa-outgoing-longwave-flux | Thermal radiation to space | TOA | `rlut_tavg-u-hxy-u` |
    | `rlds` | Surface Downwelling Longwave | surface-downwelling-longwave-flux | Atmospheric thermal radiation | Surface | `rlds_tavg-u-hxy-u` |
    | `rlus` | Surface Upwelling Longwave | surface-upwelling-longwave-flux | Thermal radiation from surface | Surface | `rlus_tavg-u-hxy-u` |
    | `rls` | Net Surface Longwave | surface-net-upward-longwave-flux | Net thermal at surface | Surface | `rls_tavg-u-hxy-u` |

    ### Net Radiation

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `rtmt` | Net TOA Radiation | toa-net-downward-radiative-flux | Net radiation at TOA | TOA | `rtmt_tavg-u-hxy-u` |
    | `rns` | Net Surface Shortwave | surface-net-downward-shortwave-flux | Net shortwave at surface | Surface | `rns_tavg-u-hxy-u` |

=== "Cloud Variables"

    ### Cloud Fraction

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `clt` | Total Cloud Fraction | cloud-area-fraction | Total column cloud cover | Atmosphere | `clt_tavg-u-hxy-u` |
    | `cl` | Cloud Area Fraction | cloud-area-fraction-in-atmosphere-layer | Cloud fraction by level | Atmosphere | `cl_tavg-al-hxy-u` |
    | `clc` | Convective Cloud Fraction | convective-cloud-area-fraction-in-atmosphere-layer | Convective cloud fraction | Atmosphere | `clc_tavg-al-hxy-u` |

    ### Cloud Water Content

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `clw` | Cloud Liquid Water | mass-fraction-of-cloud-liquid-water-in-air | Liquid water in clouds | Atmosphere | `clw_tavg-al-hxy-u` |
    | `cli` | Cloud Ice | mass-fraction-of-cloud-ice-in-air | Ice water in clouds | Atmosphere | `cli_tavg-al-hxy-u` |
    | `clwvi` | Liquid Water Path | atmosphere-cloud-liquid-water-content | Integrated liquid water | Atmosphere | `clwvi_tavg-u-hxy-u` |
    | `clivi` | Ice Water Path | atmosphere-cloud-ice-content | Integrated ice water | Atmosphere | `clivi_tavg-u-hxy-u` |

=== "Atmospheric Chemistry"

    ### Greenhouse Gases

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `co2` | Carbon Dioxide | mole-fraction-of-carbon-dioxide-in-air | CO₂ concentration | Atmosphere | `co2_tavg-al-hxy-u` |
    | `ch4` | Methane | mole-fraction-of-methane-in-air | CH₄ concentration | Atmosphere | `ch4_tavg-al-hxy-u` |
    | `n2o` | Nitrous Oxide | mole-fraction-of-nitrous-oxide-in-air | N₂O concentration | Atmosphere | `n2o_tavg-al-hxy-u` |
    | `o3` | Ozone | mole-fraction-of-ozone-in-air | O₃ concentration | Atmosphere | `o3_tavg-al-hxy-u` |
    | `h2o` | Water Vapor | mole-fraction-of-water-vapor-in-air | H₂O concentration | Atmosphere | `h2o_tavg-al-hxy-u` |

    ### Reactive Gases

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `no` | Nitric Oxide | mole-fraction-of-nitrogen-monoxide-in-air | NO concentration | Atmosphere | `no_tavg-al-hxy-u` |
    | `no2` | Nitrogen Dioxide | mole-fraction-of-nitrogen-dioxide-in-air | NO₂ concentration | Atmosphere | `no2_tavg-al-hxy-u` |
    | `hno3` | Nitric Acid | mole-fraction-of-nitric-acid-in-air | HNO₃ concentration | Atmosphere | `hno3_tavg-al-hxy-u` |
    | `co` | Carbon Monoxide | mole-fraction-of-carbon-monoxide-in-air | CO concentration | Atmosphere | `co_tavg-al-hxy-u` |
    | `so2` | Sulfur Dioxide | mole-fraction-of-sulfur-dioxide-in-air | SO₂ concentration | Atmosphere | `so2_tavg-al-hxy-u` |

=== "Aerosol Variables"

    ### Aerosol Optical Properties

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `od550aer` | Aerosol Optical Depth at 550nm | atmosphere-optical-thickness-due-to-ambient-aerosol-particles | Total aerosol optical depth | Atmosphere | `od550aer_tavg-u-hxy-u` |
    | `abs550aer` | Aerosol Absorption at 550nm | atmosphere-absorption-optical-thickness-due-to-ambient-aerosol-particles | Aerosol absorption | Atmosphere | `abs550aer_tavg-u-hxy-u` |
    | `ec550aer` | Aerosol Extinction at 550nm | atmosphere-extinction-optical-thickness-due-to-ambient-aerosol-particles | Aerosol extinction | Atmosphere | `ec550aer_tavg-al-hxy-u` |

    ### Aerosol Mass Mixing Ratios

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `mmrbc` | Black Carbon Mass Mixing Ratio | mass-fraction-of-black-carbon-dry-aerosol-particles-in-air | Black carbon concentration | Atmosphere | `mmrbc_tavg-al-hxy-u` |
    | `mmrso4` | Sulfate Mass Mixing Ratio | mass-fraction-of-sulfate-dry-aerosol-particles-in-air | Sulfate concentration | Atmosphere | `mmrso4_tavg-al-hxy-u` |
    | `mmrdust` | Dust Mass Mixing Ratio | mass-fraction-of-dust-dry-aerosol-particles-in-air | Dust concentration | Atmosphere | `mmrdust_tavg-al-hxy-u` |
    | `mmroa` | Organic Aerosol Mass Mixing Ratio | mass-fraction-of-particulate-organic-matter-dry-aerosol-particles-in-air | Organic aerosol concentration | Atmosphere | `mmroa_tavg-al-hxy-u` |
    | `mmrss` | Sea Salt Mass Mixing Ratio | mass-fraction-of-sea-salt-dry-aerosol-particles-in-air | Sea salt concentration | Atmosphere | `mmrss_tavg-al-hxy-u` |

=== "Heat Flux Variables"

    ### Surface Heat Fluxes

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `hfls` | Surface Upward Latent Heat | surface-upward-latent-heat-flux | Latent heat from surface | Surface | `hfls_tavg-u-hxy-u` |
    | `hfss` | Surface Upward Sensible Heat | surface-upward-sensible-heat-flux | Sensible heat from surface | Surface | `hfss_tavg-u-hxy-u` |
    | `hfds` | Surface Downward Heat Flux | surface-net-downward-heat-flux | Net heat into surface | Surface | `hfds_tavg-u-hxy-sea` |

    ### Subsurface Heat Fluxes

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `hfdsl` | Downward Heat Flux in Soil | downward-heat-flux-at-ground-level-in-soil | Heat into soil | Land | `hfdsl_tavg-u-hxy-lnd` |
    | `hfgeou` | Geothermal Heat Flux | upward-geothermal-heat-flux-at-sea-floor | Geothermal heating | Ocean | `hfgeou_tavg-u-hxy-sea` |

=== "Water Fluxes"

    ### Evaporation and Transpiration

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `evspsbl` | Evaporation | water-evapotranspiration-flux | Total evapotranspiration | Surface | `evspsbl_tavg-u-hxy-u` |
    | `evspsblveg` | Transpiration | water-evapotranspiration-flux-from-canopy | Plant transpiration | Land | `evspsblveg_tavg-u-hxy-lnd` |
    | `evspsblsoi` | Soil Evaporation | water-evaporation-flux-from-soil | Evaporation from soil | Land | `evspsblsoi_tavg-u-hxy-lnd` |
    | `evspsblpot` | Potential Evapotranspiration | water-potential-evapotranspiration-flux | Potential ET | Land | `evspsblpot_tavg-u-hxy-lnd` |

    ### Runoff and Drainage

    | Root Variable | Full Name | Standard Name | Description | Typical Domain | Example Usage |
    |---------------|-----------|---------------|-------------|----------------|---------------|
    | `mrro` | Total Runoff | runoff-flux | Total runoff from land | Land | `mrro_tavg-u-hxy-lnd` |
    | `mrros` | Surface Runoff | surface-runoff-flux | Surface runoff only | Land | `mrros_tavg-u-hxy-lnd` |
    | `mrrob` | Subsurface Runoff | subsurface-runoff-flux | Baseflow/drainage | Land | `mrrob_tavg-u-hxy-lnd` |

## Root Variable Statistics

### Count by Domain

| Domain | Count | Percentage | Most Common Type |
|--------|-------|------------|------------------|
| **Atmospheric** | 198 | 32% | Temperature, wind, chemistry |
| **Ocean** | 124 | 20% | Circulation, biogeochemistry |
| **Land** | 142 | 23% | Vegetation, carbon, soil |
| **Sea Ice** | 47 | 8% | Ice properties, dynamics |
| **Land Ice** | 15 | 2% | Ice sheet properties |
| **Radiation** | 38 | 6% | Shortwave, longwave, net |
| **Chemistry** | 56 | 9% | Gases, aerosols |
| **Total** | **620** | **100%** | All domains |

### Most Common Root Variables

| Rank | Root Variable | Count in Registry | Primary Domain | Most Common Usage |
|------|---------------|-------------------|----------------|-------------------|
| 1 | `ta` | 15 | Atmosphere | 3D atmospheric temperature |
| 2 | `uo` | 12 | Ocean | Eastward ocean velocity |
| 3 | `pr` | 11 | Atmosphere | Precipitation variations |
| 4 | `cl` | 10 | Atmosphere | Cloud properties |
| 5 | `si*` | 45 | Sea Ice | Sea ice variables (all types) |
| 6 | `c*` | 38 | Land | Carbon cycle variables |
| 7 | `hf*` | 22 | Energy | Heat flux variables |
| 8 | `rs*` | 20 | Radiation | Shortwave radiation |
| 9 | `rl*` | 18 | Radiation | Longwave radiation |
| 10 | `mmr*` | 15 | Chemistry | Mass mixing ratios |

## Search and Filter Tools

### Quick Search by Domain

| Domain | Search Pattern | Example Variables |
|--------|----------------|-------------------|
| **Temperature** | `*temp*, ta*, ts*, tos*` | `tas`, `tos`, `thetao`, `tsl` |
| **Precipitation** | `pr*, *precip*, *rain*, *snow*` | `pr`, `prsn`, `prc`, `prra` |
| **Wind** | `*wind*, ua*, va*, u*s, v*s` | `ua`, `vas`, `sfcWind`, `wap` |
| **Ocean** | `*o, *ocean*, so*, uo*, vo*` | `tos`, `so`, `uo`, `thetao` |
| **Land** | `*veg*, lai*, *soil*, c*` | `lai`, `cVeg`, `mrsol`, `gpp` |
| **Ice** | `si*, li*` | `siconc`, `lithk`, `sithick` |
| **Radiation** | `r*s*, r*l*, r*t*` | `rsds`, `rlut`, `rtmt` |
| **Chemistry** | `*o3*, co2*, ch4*, no*` | `o3`, `co2`, `no2`, `hno3` |
| **Aerosols** | `*aer*, mmr*, od*` | `od550aer`, `mmrbc`, `abs550aer` |

### Component Compatibility Quick Reference

| Root Variable Type | Compatible Area Labels | Compatible Vertical Labels | Compatible Temporal Labels |
|-------------------|------------------------|----------------------------|---------------------------|
| **Surface Met** | `h2m`, `h10m`, `u` | `u` | `tavg`, `tmax`, `tmin`, `tpt` |
| **3D Atmosphere** | `al`, `plev`, `p19` | `air` | `tavg`, `tpt` |
| **Ocean Surface** | `u` | `sea`, `u` | `tavg` |
| **Ocean 3D** | `ol` | `sea` | `tavg`, `tpt` |
| **Land Surface** | `u` | `lnd`, `u` | `tavg` |
| **Soil** | `sl` | `lnd` | `tavg` |
| **Sea Ice** | `u` | `si`, `u` | `tavg` |
| **Land Ice** | `u` | `is` | `tavg` |
| **Radiation** | `u` | `u` | `tavg` |

## Navigation

- **[← Component Examples](../component-examples.md)**
- **[Construction Guide →](../construction/index.md)**
- **[Variable Registry →](../../index.md)**

---

*This comprehensive registry contains all 620+ root variables available in the Variable Registry, organized by domain for easy discovery and selection.*