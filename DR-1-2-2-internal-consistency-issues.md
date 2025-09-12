**clwvi_tavg-u-hxy-u**

- description
    - E3hr.clwvi: 'Liquid water path'
    - CFday.clwvi: 'calculate mass of condensed (liquid + ice) water in the column divided by the area of the column (not just the area of the cloudy portion of the column). This includes precipitating hydrometeors ONLY if the precipitating hydrometeors affect the calculation of radiative transfer in model.'
    - Amon.clwvi: 'mass of condensed (liquid + ice) water in the column divided by the area of the column (not just the area of the cloudy portion of the column). Includes precipitating hydrometeors ONLY if the precipitating hydrometeor affects the calculation of radiative transfer in model.'


**drynh3_tavg-u-hxy-u**

- ui-label
    - AERmon.drynh3: 'Dry Deposition Rate of NH3'
    - AERday.drynh3: 'Daily Dry Deposition Rate of NH3'

- description
    - AERmon.drynh3: 'Monthly Dry Deposition Rate of NH3 at surface'
    - AERday.drynh3: 'Daily Dry Deposition Rate of NH3 at surface. Vertically integrated throughout the column to the surface.'


**drynh4_tavg-u-hxy-u**

- ui-label
    - AERmon.drynh4: 'Dry Deposition Rate of NH4'
    - AERday.drynh4: 'Daily Dry Deposition Rate of NH4'

- description
    - AERmon.drynh4: 'Dry Deposition Rate of NH4'
    - AERday.drynh4: 'Daily Dry Deposition Rate of NH4 at surface. Vertically integrated throughout the column to the surface.'


**drynoy_tavg-u-hxy-u**

- ui-label
    - AERday.drynoy: 'Daily Dry Deposition Rate of NOy'
    - AERmon.drynoy: 'Dry Deposition Rate of NOy'

- description
    - AERday.drynoy: 'Daily Dry Deposition Rate of NOy at surface. Vertically integrated throughout the column to the surface.'
    - AERmon.drynoy: 'Dry Deposition Rate of NOy'


**rls_tavg-u-hxy-u**

- description
    - Emon.rls: 'Net longwave surface radiation'
    - day.rls: 'Net longwave radiation'


**rlut_tavg-u-hxy-u**

- description
    - day.rlut: 'at the top of the atmosphere.'
    - Amon.rlutSouth30: 'at the top of the atmosphere (to be compared with satellite measurements)'
    - E3hr.rlut: 'TOA outgoing longwave radiation'
    - Amon.rlut: 'at the top of the atmosphere (to be compared with satellite measurements)'


**rlus_tavg-u-hxy-u**

- description
    - Amon.rlus: 'The surface called "surface" means the lower boundary of the atmosphere. "longwave" means longwave radiation. Upwelling radiation is radiation from below. It does not mean "net upward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'
    - 3hr.rlus: 'This is the 3-hour mean flux.'
    - E1hr.rlus: 'Hourly surface upwelling shortwave radiation'
    - day.rlus: 'The surface called "surface" means the lower boundary of the atmosphere. "longwave" means longwave radiation. Upwelling radiation is radiation from below. It does not mean "net upward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'

- ui-label
    - E1hr.rlus: 'Surface upwelling shortwave radiation'
    - day.rlus: 'Surface Upwelling Longwave Radiation'


**rlus_tavg-u-hxy-is**

- dimensions
    - ImonGre.rlus: ['xgre', 'ygre', 'time']
    - ImonAnt.rlus: ['xant', 'yant', 'time']
    - LImon.rlusIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.rlusIs: 'Ice Sheet Surface Upwelling Longwave Radiation'
    - ImonGre.rlus: 'Surface Upwelling Longwave Radiation'

- description
    - LImon.rlusIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.rlus: 'The surface called "surface" means the lower boundary of the atmosphere. "longwave" means longwave radiation. Upwelling radiation is radiation from below. It does not mean "net upward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'

- cell-measures
    - LImon.rlusIs: 'area: areacella'
    - ImonGre.rlus: 'area: areacellg'

- model-realm
    - LImon.rlusIs: 'landIce'
    - ImonGre.rlus: 'atmos'

- physical-parameter-name
    - LImon.rlusIs: 'rlusIs'
    - ImonGre.rlus: 'rlus'

- variable-root
    - LImon.rlusIs: 'rlusis'
    - ImonGre.rlus: 'rlus'


**rsds_tavg-u-hxy-u**

- description
    - Amon.rsdsSouth30: 'Surface solar irradiance for UV calculations.'
    - 3hr.rsds: 'This is the 3-hour mean flux.'
    - 6hrPlev.rsds: 'Surface downwelling shortwave radiation'
    - Amon.rsds: 'Surface solar irradiance for UV calculations.'
    - E1hr.rsds: 'Hourly downward solar radiation flux at the surface'
    - day.rsds: 'Surface solar irradiance for UV calculations.'

- ui-label
    - E1hr.rsds: 'Hourly downward solar radiation flux at the surface'
    - day.rsds: 'Surface Downwelling Shortwave Radiation'


**rsds_tavg-u-hxy-is**

- dimensions
    - ImonGre.rsds: ['xgre', 'ygre', 'time']
    - ImonAnt.rsds: ['xant', 'yant', 'time']
    - LImon.rsdsIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.rsdsIs: 'Ice Sheet Surface Downwelling Shortwave Radiation'
    - ImonGre.rsds: 'Surface Downwelling Shortwave Radiation'

- description
    - LImon.rsdsIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.rsds: 'Surface solar irradiance for UV calculations.'

- cell-measures
    - LImon.rsdsIs: 'area: areacella'
    - ImonGre.rsds: 'area: areacellg'

- model-realm
    - LImon.rsdsIs: 'landIce'
    - ImonGre.rsds: 'atmos'

- physical-parameter-name
    - LImon.rsdsIs: 'rsdsIs'
    - ImonGre.rsds: 'rsds'

- variable-root
    - LImon.rsdsIs: 'rsdsis'
    - ImonGre.rsds: 'rsds'


**rlutcs_tavg-u-hxy-u**

- description
    - E3hr.rlutcs: 'TOA outgoing clear sky longwave'
    - CFday.rlutcs: 'Upwelling clear-sky longwave radiation at top of atmosphere'


**rsdsdiff_tavg-u-hxy-u**

- ui-label
    - Eday.rsdsdiff: 'Surface Diffuse Downwelling Shortwave Radiation'
    - E1hr.rsdsdiff: 'Surface Diffuse Downwelling Shortwave Radiation\n'

- description
    - Eday.rsdsdiff: 'Surface downwelling solar irradiance from diffuse radiation for UV calculations.'
    - E1hr.rsdsdiff: 'Surface Diffuse Downwelling Shortwave Radiation'


**rsus_tavg-u-hxy-u**

- description
    - 3hr.rsus: 'This is the 3-hour mean flux.'
    - Amon.rsusSouth30: 'The surface called "surface" means the lower boundary of the atmosphere. "shortwave" means shortwave radiation. Upwelling radiation is radiation from below. It does not mean "net upward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'
    - day.rsus: 'The surface called "surface" means the lower boundary of the atmosphere. "shortwave" means shortwave radiation. Upwelling radiation is radiation from below. It does not mean "net upward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'
    - E1hr.rsus: 'Surface upwelling shortwave radiation'

- ui-label
    - E1hr.rsus: 'Surface upwelling shortwave radiation'
    - day.rsus: 'Surface Upwelling Shortwave Radiation'


**rsdt_tavg-u-hxy-u**

- description
    - CFday.rsdt: 'Shortwave radiation incident at the top of the atmosphere'
    - Amon.rsdtSouth30: 'at the top of the atmosphere'


**rss_tavg-u-hxy-u**

- description
    - Emon.rss: 'Net downward shortwave radiation at the surface'
    - day.rss: 'Net shortwave radiation'


**rsus_tavg-u-hxy-is**

- dimensions
    - ImonGre.rsus: ['xgre', 'ygre', 'time']
    - ImonAnt.rsus: ['xant', 'yant', 'time']
    - LImon.rsusIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.rsusIs: 'Ice Sheet Surface Upwelling Shortwave Radiation'
    - ImonGre.rsus: 'Surface Upwelling Shortwave Radiation'

- description
    - LImon.rsusIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.rsus: 'The surface called "surface" means the lower boundary of the atmosphere. "shortwave" means shortwave radiation. Upwelling radiation is radiation from below. It does not mean "net upward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'

- cell-measures
    - LImon.rsusIs: 'area: areacella'
    - ImonGre.rsus: 'area: areacellg'

- model-realm
    - LImon.rsusIs: 'landIce'
    - ImonGre.rsus: 'atmos'

- physical-parameter-name
    - LImon.rsusIs: 'rsusIs'
    - ImonGre.rsus: 'rsus'

- variable-root
    - LImon.rsusIs: 'rsusis'
    - ImonGre.rsus: 'rsus'


**rsut_tavg-u-hxy-u**

- description
    - CFday.rsut: 'at the top of the atmosphere'
    - E3hr.rsut: 'TOA outgoing shortwave radiation'


**sfcWind_tavg-h10m-hxy-u**

- ui-label
    - E1hr.sfcWind: 'Hourly surface wind speed'
    - day.sfcWind: 'Daily-Mean Near-Surface Wind Speed'
    - E3hr.sfcWind: 'Near-Surface Wind Speed'
    - E1hr.sfcWindSouth30: 'Hourly surface wind speed'

- description
    - E1hr.sfcWind: 'Hourly near-surface wind speed at 10m above the ground'
    - day.sfcWind: 'near-surface (usually, 10 meters) wind speed.'
    - E3hr.sfcWind: 'Near surface wind speed'
    - E1hr.sfcWindSouth30: 'Hourly near-surface wind speed at 10m above the ground'
    - 6hrPlev.sfcWind: 'near-surface (usually, 10 meters) wind speed.'
    - Amon.sfcWind: 'This is the mean of the speed, not the speed computed from the mean u and v components of wind'


**sfcWind_tmax-h10m-hxy-u**

- cell-methods
    - Emon.sfcWindmax: 'area: mean time: maximum within days time: mean over days'
    - day.sfcWindmax: 'area: mean time: maximum'

- dimensions
    - Emon.sfcWindmax: ['longitude', 'latitude', 'time4', 'height10m']
    - day.sfcWindmax: ['longitude', 'latitude', 'time', 'height10m']


**scldncl_tavg-u-hxy-scl**

- description
    - Emon.scldncl: 'Cloud Droplet Number Concentration of Stratiform Cloud Tops'
    - Eday.scldncl: 'Droplets are liquid only.  Report concentration "as seen from space" over stratiform liquid cloudy portion of grid cell.  This is the value from uppermost model layer with liquid cloud or, if available, it is better to sum over all liquid cloud tops, no matter where they occur, as long as they are seen from the top of the atmosphere. Weight by total liquid cloud top fraction of  (as seen from TOA) each time sample when computing monthly mean.'


**rsutcs_tavg-u-hxy-u**

- description
    - E3hr.rsutcs: 'TOA outgoing clear sky shortwave'
    - CFday.rsutcs: 'Calculated in the absence of clouds.'


**sbl_tavg-u-hxy-u**

- description
    - Eday.sbl: 'surface upward flux of water vapor due to sublimation of surface snow and ice'
    - Amon.sbl: 'The snow and ice sublimation flux is the loss of snow and ice mass from the surface resulting from their conversion to water vapor that enters the atmosphere.'


**sbl_tavg-u-hxy-is**

- dimensions
    - ImonGre.sbl: ['xgre', 'ygre', 'time']
    - ImonAnt.sbl: ['xant', 'yant', 'time']
    - LImon.sblIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.sblIs: 'Ice Sheet Surface Snow and Ice Sublimation Flux'
    - ImonGre.sbl: 'Surface Snow and Ice Sublimation Flux'

- description
    - LImon.sblIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.sbl: 'The snow and ice sublimation flux is the loss of snow and ice mass per unit area from the surface resulting from their direct conversion to water vapor that enters the atmosphere.'

- cell-measures
    - LImon.sblIs: 'area: areacella'
    - ImonGre.sbl: 'area: areacellg'

- physical-parameter-name
    - LImon.sblIs: 'sblIs'
    - ImonGre.sbl: 'sbl'

- variable-root
    - LImon.sblIs: 'sblis'
    - ImonGre.sbl: 'sbl'


**shrubFrac_tavg-u-hxy-u**

- description
    - Eyr.shrubFrac: 'Percentage of entire grid cell  that is covered by shrub.'
    - Lmon.shrubFrac: 'fraction of entire grid cell  that is covered by shrub.'


**sfdsi_tavg-u-hxy-sea**

- description
    - Omon.sfdsi: 'This field is physical, and it arises since sea ice has a nonzero salt content, so it exchanges salt with the liquid ocean upon melting and freezing.'
    - 3hr.sfdsi: 'Basal salt flux into ocean from sea ice. This field is physical, and it arises since sea ice has a nonzero salt content, so it exchanges salt with the liquid ocean upon melting and freezing.'


**sftgif_tavg-u-hxy-u**

- description
    - LImon.sftgif: 'Percentage of grid cell covered by land ice (ice sheet, ice shelf, ice cap, glacier)'
    - IyrGre.sftgif: 'This is needed in case the ice sheet area changes in time'
    - IyrAnt.sftgif: 'This is needed in case the ice sheet area changes in time'

- cell-measures
    - LImon.sftgif: 'area: areacella'
    - IyrGre.sftgif: 'area: areacellg'
    - IyrAnt.sftgif: 'area: areacellg'

- dimensions
    - LImon.sftgif: ['longitude', 'latitude', 'time']
    - IyrGre.sftgif: ['xgre', 'ygre', 'time']
    - IyrAnt.sftgif: ['xant', 'yant', 'time']


**sftgrf_tavg-u-hxy-u**

- dimensions
    - IyrGre.sftgrf: ['xgre', 'ygre', 'time']
    - IyrAnt.sftgrf: ['xant', 'yant', 'time']
    - LImon.sftgrf: ['longitude', 'latitude', 'time']

- description
    - LImon.sftgrf: 'Percentage of grid cell covered by grounded ice sheet'
    - IyrGre.sftgrf: 'This is needed in case the grounded ice sheet area changes in time (NO floating ice shelf)'

- cell-measures
    - LImon.sftgrf: 'area: areacella'
    - IyrGre.sftgrf: 'area: areacellg'


**sfpm1_tavg-h2m-hxy-u**

- ui-label
    - AERhr.sfpm1: 'Hourly Surface PM1.0 Mixing Ratio'
    - AERday.sfpm1: 'Surface daily mean PM1.0'

- description
    - AERhr.sfpm1: 'Hourly PM1.0 Mass Mixing Ratio in Lowest Model Layer'
    - AERday.sfpm1: 'Daily mean PM1.0 mass mixing ratio in lowest model layer'


**sfpm10_tavg-h2m-hxy-u**

- ui-label
    - AERhr.sfpm10: 'Hourly Surface PM10 Mixing Ratio'
    - AERday.sfpm10: 'Daily mean surface PM10'

- description
    - AERhr.sfpm10: 'Hourly PM10 Mass Mixing Ratio in Lowest Model Layer'
    - AERday.sfpm10: 'Daily mean PM10 mass mixing ratio in lowest model layer'


**sfpm25_tavg-h2m-hxy-u**

- ui-label
    - AERhr.sfpm25: 'PM2.5 Mass Mixing Ratio in Lowest Model Layer'
    - AERday.sfpm25: 'Daily mean surface PM2.5 '

- description
    - AERhr.sfpm25: 'Mass fraction of atmospheric particulate compounds with an aerodynamic diameter of less than or equal to 2.5 micrometers. To specify the relative humidity and temperature at which the particle size applies, provide scalar coordinate variables with the standard names of "relative\\_humidity" and "air\\_temperature".'
    - AERday.sfpm25: 'Daily mean PM2.5 mass mixing ratio in lowest model layer'


**sftflf_tavg-u-hxy-u**

- dimensions
    - IyrGre.sftflf: ['xgre', 'ygre', 'time']
    - IyrAnt.sftflf: ['xant', 'yant', 'time']
    - LImon.sftflf: ['longitude', 'latitude', 'time']

- description
    - LImon.sftflf: 'Percentage of grid cell covered by floating ice shelf, the component of the ice sheet that is flowing over sea water'
    - IyrGre.sftflf: 'This is needed in case the floating ice sheet area changes in time (NO grounded ice sheet)'

- cell-measures
    - LImon.sftflf: 'area: areacella'
    - IyrGre.sftflf: 'area: areacellg'


**hfgeoubed_tavg-u-hxy-gis**

- dimensions
    - IyrGre.hfgeoubed: ['xgre', 'ygre', 'time']
    - IyrAnt.hfgeoubed: ['xant', 'yant', 'time']


**hfss_tavg-u-hxy-u**

- description
    - Amon.hfss: 'The surface sensible heat flux, also called turbulent heat flux, is the exchange of heat between the surface and the air by motion of air.'
    - 3hr.hfss: 'This is the 3-hour mean flux.'
    - E1hr.hfss: 'Hourly surface upward sensible heat flux'
    - day.hfss: 'The surface sensible heat flux, also called turbulent heat flux, is the exchange of heat between the surface and the air by motion of air.'

- ui-label
    - E1hr.hfss: 'Surface upward sensible heat flux'
    - day.hfss: 'Surface Upward Sensible Heat Flux'


**hfss_tavg-u-hxy-is**

- ui-label
    - ImonAnt.hfss: 'Surface Upward Sensible Heat Flux'
    - LImon.hfssIs: 'Ice Sheet Surface Upward Sensible Heat Flux'

- description
    - ImonAnt.hfss: 'The surface sensible heat flux, also called turbulent heat flux, is the exchange of heat between the surface and the air by motion of air.'
    - LImon.hfssIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'

- cell-measures
    - ImonAnt.hfss: 'area: areacellg'
    - LImon.hfssIs: 'area: areacella'

- dimensions
    - ImonAnt.hfss: ['xant', 'yant', 'time']
    - LImon.hfssIs: ['longitude', 'latitude', 'time']
    - ImonGre.hfss: ['xgre', 'ygre', 'time']

- model-realm
    - ImonAnt.hfss: 'atmos'
    - LImon.hfssIs: 'landIce'

- physical-parameter-name
    - ImonAnt.hfss: 'hfss'
    - LImon.hfssIs: 'hfssIs'

- variable-root
    - ImonAnt.hfss: 'hfss'
    - LImon.hfssIs: 'hfssis'


**hfls_tavg-u-hxy-u**

- description
    - Amon.hflsSouth30: 'includes both evaporation and sublimation'
    - 3hr.hfls: 'This is the 3-hour mean flux.'
    - E1hr.hfls: 'Hourly surface upward latent heat flux'
    - Amon.hfls: 'includes both evaporation and sublimation'
    - day.hfls: 'The surface called "surface" means the lower boundary of the atmosphere. "Upward" indicates a vector component which is positive when directed upward (negative downward). The surface latent heat flux is the exchange of heat between the surface and the air on account of evaporation (including sublimation). In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'

- ui-label
    - E1hr.hfls: 'Surface upward latent heat flux'
    - Amon.hfls: 'Surface Upward Latent Heat Flux'
    - day.hfls: 'Surface Upward Latent Heat Flux'


**hfls_tavg-u-hxy-is**

- dimensions
    - ImonAnt.hfls: ['xant', 'yant', 'time']
    - ImonGre.hfls: ['xgre', 'ygre', 'time']
    - LImon.hflsIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.hflsIs: 'Ice Sheet Surface Upward Latent Heat Flux'
    - ImonAnt.hfls: 'Surface Upward Latent Heat Flux'

- description
    - LImon.hflsIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonAnt.hfls: 'The surface called "surface" means the lower boundary of the atmosphere. "Upward" indicates a vector component which is positive when directed upward (negative downward). The surface latent heat flux is the exchange of heat between the surface and the air on account of evaporation (including sublimation). In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'

- cell-measures
    - LImon.hflsIs: 'area: areacella'
    - ImonAnt.hfls: 'area: areacellg'

- model-realm
    - LImon.hflsIs: 'landIce'
    - ImonAnt.hfls: 'atmos'

- physical-parameter-name
    - LImon.hflsIs: 'hflsIs'
    - ImonAnt.hfls: 'hfls'

- variable-root
    - LImon.hflsIs: 'hflsis'
    - ImonAnt.hfls: 'hfls'


**hurs_tavg-h2m-hxy-u**

- ui-label
    - 6hrPlev.hurs: 'Near-Surface Relative Humidity'
    - E1hr.hursSouth30: 'Hourly relative humidity at the surface'
    - E1hr.hurs: 'Hourly relative humidity at the surface'
    - day.hurs: 'Near-Surface Relative Humidity'

- description
    - 6hrPlev.hurs: 'The relative humidity with respect to liquid water for T> 0 C, and with respect to ice for T<0 C.'
    - E1hr.hursSouth30: 'Relative humidity at 2m above the surface'
    - Amon.hurs: 'This is the relative humidity with respect to liquid water for T> 0 C, and with respect to ice for T<0 C.'
    - E1hr.hurs: 'Relative humidity at 2m above the surface'
    - day.hurs: 'This is the relative humidity with respect to liquid water for T> 0 C, and with respect to ice for T<0 C.'


**hur_tavg-al-hxy-u**

- description
    - CFmon.hur: 'The relative humidity with respect to liquid water for T> 0 C, and with respect to ice for T<0 C.'
    - CFday.hur: 'This is the relative humidity with respect to liquid water for T> 0 C, and with respect to ice for T<0 C.'


**iareagr_tavg-u-hm-gis**

- description
    - IyrGre.iareagr: 'Greenland'
    - IyrAnt.iareagr: 'Antarctica'


**icem_tavg-u-hxy-is**

- dimensions
    - ImonAnt.icem: ['xant', 'yant', 'time']
    - ImonGre.icem: ['xgre', 'ygre', 'time']
    - LImon.icemIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.icemIs: 'Ice Sheet Surface Ice Melt Flux'
    - ImonAnt.icem: 'Surface Ice Melt Flux'

- description
    - LImon.icemIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonAnt.icem: 'Loss of ice mass resulting from surface melting. Computed as the total surface melt water on the land ice portion of the grid cell divided by land ice area in the grid cell.'

- cell-measures
    - LImon.icemIs: 'area: areacella'
    - ImonAnt.icem: 'area: areacellg'

- physical-parameter-name
    - LImon.icemIs: 'icemIs'
    - ImonAnt.icem: 'icem'

- variable-root
    - LImon.icemIs: 'icemis'
    - ImonAnt.icem: 'icem'


**hus_tpt-al-hxy-u**

- description
    - E3hrPt.hus: 'Specific Humidity'
    - 6hrLev.hus: 'Specific humidity is the mass fraction of water vapor in (moist) air.'


**huss_tpt-h2m-hxy-u**

- description
    - E1hr.huss: 'Specific humidity at 2m.'
    - 3hr.huss: 'This is sampled synoptically.'


**iareafl_tavg-u-hm-fis**

- description
    - IyrGre.iareafl: 'Greenland'
    - IyrAnt.iareafl: 'Antarctica'


**intvaw_tavg-u-hxy-u**

- description
    - Emon.intvaw: 'Vertically integrated Northward moisture transport (Mass\\_weighted\\_vertical integral of the product of northward wind by total water mass per unit mass)'
    - Eday.intvaw: 'Vertically integrated northward moisture transport (Mass\\_weighted\\_vertical integral of the product of northward wind by total water mass per unit mass)'


**intpp_tavg-u-hxy-sea**

- description
    - Omon.intpp: 'Vertically integrated total primary (organic carbon) production by phytoplankton.  This should equal the sum of intpdiat+intpphymisc, but those individual components may be unavailable in some models.'
    - Oday.intpp: 'Vertically integrated total primary (organic carbon) production by phytoplankton. This should equal the sum of intpdiat+intpphymisc, but those individual components may be unavailable in some models.'


**intuaw_tavg-u-hxy-u**

- description
    - Emon.intuaw: 'Vertically integrated Eastward moisture transport (Mass weighted vertical integral of the product of eastward wind by total water mass per unit mass)'
    - Eday.intuaw: 'Vertically integrated eastward moisture transport (Mass weighted vertical integral of the product of eastward wind by total water mass per unit mass)'


**libmassbf_tavg-u-hxy-gis**

- dimensions
    - IyrGre.libmassbfgr: ['xgre', 'ygre', 'time']
    - IyrAnt.libmassbfgr: ['xant', 'yant', 'time']
    - ImonAnt.libmassbfgr: ['xant', 'yant', 'time']
    - ImonGre.libmassbfgr: ['xgre', 'ygre', 'time']

- description
    - ImonAnt.libmassbfgr: 'quantity averaged over grounded ice sheet'
    - IyrGre.libmassbfgr: 'quantity averaged over grounded land ice'


**licalvf_tavg-u-hxy-is**

- dimensions
    - ImonAnt.licalvf: ['xant', 'yant', 'time']
    - ImonGre.licalvf: ['xgre', 'ygre', 'time']
    - IyrGre.licalvf: ['xgre', 'ygre', 'time']
    - IyrAnt.licalvf: ['xant', 'yant', 'time']


**jpdftaureicemodis_tavg-u-hxy-u**

- description
    - Eday.jpdftaureicemodis: 'MODIS Optical Thickness-Particle Size joint  distribution, ice'
    - Emon.jpdftaureicemodis: 'MODIS Optical Thickness-Particle Size joint distribution, ice'


**jpdftaureliqmodis_tavg-u-hxy-u**

- description
    - Emon.jpdftaureliqmodis: 'MODIS Optical Thickness-Particle Size joint distribution, liquid'
    - Eday.jpdftaureliqmodis: 'MODIS Optical Thickness-Particle Size joint  distribution, liquid'


**libmassbf_tavg-u-hxy-fis**

- dimensions
    - IyrGre.libmassbffl: ['xgre', 'ygre', 'time']
    - IyrAnt.libmassbffl: ['xant', 'yant', 'time']
    - ImonAnt.libmassbffl: ['xant', 'yant', 'time']
    - ImonGre.libmassbffl: ['xgre', 'ygre', 'time']

- description
    - ImonAnt.libmassbffl: 'quantity averaged over floating ice shelf'
    - IyrGre.libmassbffl: 'quantity averaged over floating land ice'


**lifmassbf_tavg-u-hxy-is**

- dimensions
    - ImonGre.lifmassbf: ['xgre', 'ygre', 'time']
    - IyrAnt.lifmassbf: ['xant', 'yant', 'time']


**litemptop_tavg-u-hxy-is**

- ui-label
    - LImon.litemptopIs: 'Ice Sheet Temperature at Top of Ice Sheet Model'
    - IyrGre.litemptop: 'Temperature at Top of Ice Sheet Model'
    - ImonAnt.litemptop: 'Temperature at Top of Ice Sheet Model'

- description
    - LImon.litemptopIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - IyrGre.litemptop: 'quantity averaged over ice sheet only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonAnt.litemptop: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods'
    - IyrAnt.litemptop: 'quantity averaged over ice sheet only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.litemptop: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods'

- cell-measures
    - LImon.litemptopIs: 'area: areacella'
    - IyrGre.litemptop: 'area: areacellg'
    - ImonAnt.litemptop: 'area: areacellg'

- dimensions
    - LImon.litemptopIs: ['longitude', 'latitude', 'time']
    - IyrGre.litemptop: ['xgre', 'ygre', 'time']
    - ImonAnt.litemptop: ['xant', 'yant', 'time']
    - ImonGre.litemptop: ['xgre', 'ygre', 'time']
    - IyrAnt.litemptop: ['xant', 'yant', 'time']

- physical-parameter-name
    - LImon.litemptopIs: 'litemptopIs'
    - IyrGre.litemptop: 'litemptop'
    - ImonAnt.litemptop: 'litemptop'

- variable-root
    - LImon.litemptopIs: 'litemptopis'
    - IyrGre.litemptop: 'litemptop'
    - ImonAnt.litemptop: 'litemptop'


**lithk_ti-u-hxy-is**

- dimensions
    - IfxGre.lithk: ['xgre', 'ygre']
    - IfxAnt.lithk: ['xant', 'yant']


**lithk_tavg-u-hxy-is**

- dimensions
    - IyrGre.lithk: ['xgre', 'ygre', 'time']
    - IyrAnt.lithk: ['xant', 'yant', 'time']


**limnsw_tavg-u-hm-is**

- description
    - IyrGre.limnsw: 'Greenland'
    - IyrAnt.limnsw: 'Antarctica'


**lim_tavg-u-hm-is**

- description
    - IyrGre.lim: 'Greenland'
    - IyrAnt.lim: 'Antarctica'


**litempbot_tavg-u-hxy-fis**

- description
    - IyrAnt.litempbotfl: 'quantity averaged over floating land ice'
    - ImonGre.litempbotfl: 'quantity averaged over floating ice shelf'
    - ImonAnt.litempbotfl: 'quantity averaged over floating ice shelf'
    - IyrGre.litempbotfl: 'quantity averaged over floating land ice'

- dimensions
    - IyrAnt.litempbotfl: ['xant', 'yant', 'time']
    - ImonGre.litempbotfl: ['xgre', 'ygre', 'time']
    - IyrGre.litempbotfl: ['xgre', 'ygre', 'time']
    - ImonAnt.litempbotfl: ['xant', 'yant', 'time']


**litempbot_tavg-u-hxy-gis**

- dimensions
    - ImonGre.litempbotgr: ['xgre', 'ygre', 'time']
    - ImonAnt.litempbotgr: ['xant', 'yant', 'time']
    - IyrAnt.litempbotgr: ['xant', 'yant', 'time']
    - IyrGre.litempbotgr: ['xgre', 'ygre', 'time']

- description
    - IyrAnt.litempbotgr: 'quantity averaged over grounded land ice'
    - ImonGre.litempbotgr: 'quantity averaged over grounded ice sheet'


**mc_tavg-alh-hxy-u**

- description
    - CFday.mc: 'The net mass flux should represent the difference between the updraft and downdraft components.  This is calculated as the convective mass flux divided by the area of the whole grid cell (not just the area of the cloud).'
    - Amon.mc: 'The net mass flux should represent the difference between the updraft and downdraft components.  The flux is computed as the mass divided by the area of the grid cell.'


**lwsnl_tavg-u-hxy-lnd**

- description
    - LImon.lwsnl: 'where land over land: this is computed as the total mass of liquid water contained interstitially within the snow layer of the land portion of a grid cell divided by the area of the land portion of the cell.'
    - Eday.lwsnl: 'liquid\\_water\\_content\\_of\\_snow\\_layer'


**areacell_tavg-u-hxy-u**

- dimensions
    - IyrAnt.modelCellAreai: ['xant', 'yant', 'time']
    - IyrGre.modelCellAreai: ['xgre', 'ygre', 'time']


**mrro_tavg-u-hxy-lnd**

- description
    - 3hr.mrro: 'the total runoff (including "drainage" through the base of the soil model) leaving the land portion of the grid cell divided by the land area in the grid cell, averaged over the 3-hour interval.'
    - day.mrro: 'computed as the total runoff (including "drainage" through the base of the soil model) leaving the land portion of the grid cell divided by the land area in the grid cell.'
    - Lmon.mrro: 'the total runoff (including "drainage" through the base of the soil model) leaving the land portion of the grid cell.'


**mrtws_tavg-u-hxy-lnd**

- description
    - Emon.mrtws: 'requested for C4MIP, OCMIP/OMIP, LUMIP, ScenarioMIP, DECK, DAMIP, GeoMIP, LS3MIP, ??'
    - Eday.mrtws: 'canopy\\_and\\_surface\\_and\\_subsurface\\_water\\_amount'


**mrroLi_tavg-u-hxy-is**

- dimensions
    - ImonGre.mrroLi: ['xgre', 'ygre', 'time']
    - ImonAnt.mrroLi: ['xant', 'yant', 'time']


**mrros_tavg-u-hxy-lnd**

- description
    - Lmon.mrros: 'the total surface runoff leaving the land portion of the grid cell.'
    - Eday.mrros: 'surface\\_runoff\\_flux'


**o2_tavg-d0m-hxy-sea**

- description
    - Omon.o2os: '\'Mole concentration\' means number of moles per unit volume, also called "molarity", and is used in the construction mole\\_concentration\\_of\\_X\\_in\\_Y, where X is a material constituent of Y.  A chemical or biological species denoted by X may be described by a single term such as \'nitrogen\' or a phrase such as \'nox\\_expressed\\_as\\_nitrogen\'.'
    - Oday.o2os: 'Near surface \'Mole concentration\' means number of moles per unit volume, also called "molarity", and is used in the construction mole\\_concentration\\_of\\_X\\_in\\_Y, where X is a material constituent of Y. A chemical or biological species denoted by X may be described by a single term such as \'nitrogen\' or a phrase such as \'nox\\_expressed\\_as\\_nitrogen\'. The chemical formula for molecular oxygen is O2.'


**od550aer_tavg-u-hxy-u**

- description
    - AERmon.od550aer: 'AOD from ambient aerosols (i.e., includes aerosol water).  Does not include AOD from stratospheric aerosols if these are prescribed but includes other possible background aerosol types. Needs a comment attribute "wavelength: 550 nm"'
    - AERday.od550aer: 'AOD from the ambient aerosls (i.e., includes aerosol water).  Does not include AOD from stratospheric aerosols if these are prescribed but includes other possible background aerosol types. Needs a comment attribute "wavelength: 550 nm"'


**pctisccp_tavg-u-hxy-cl**

- description
    - CFmon.pctisccp: 'time-means weighted by the ISCCP Total Cloud Fraction - see <https://www.cfmip.org/tools-and-data/cosp>'
    - CFday.pctisccp: 'time-means are weighted by the ISCCP Total Cloud Fraction - see  <https://www.cfmip.org/tools-and-data/cosp>'


**pflw_tavg-u-hxy-lnd**

- description
    - Eday.pflw: 'liquid\\_water\\_content\\_of\\_permafrost\\_layer'
    - LImon.pflw: '"where land over land", i.e., this is the total mass of liquid water contained within the permafrost layer within the land portion of a grid cell divided by the area of the land portion of the cell.'


**pfull_tavg-al-hxy-u**

- description
    - CFday.pfull: 'Air pressure on model levels'
    - AERmon.pfull: 'The atmospheric pressure at the model layer midpoints for all times and levels in the associated output variables'


**orog_tavg-u-hxy-is**

- dimensions
    - ImonGre.orog: ['xgre', 'ygre', 'time']
    - ImonAnt.orog: ['xant', 'yant', 'time']
    - IyrAnt.orog: ['xant', 'yant', 'time']
    - IyrGre.orog: ['xgre', 'ygre', 'time']
    - LImon.orogIs: ['longitude', 'latitude', 'time']

- description
    - IyrAnt.orog: 'This is needed in case the ice sheet elevation changes in time'
    - ImonGre.orog: 'The surface called "surface" means the lower boundary of the atmosphere. Altitude is the (geometric) height above the geoid, which is the reference geopotential surface. The geoid is similar to mean sea level.'
    - LImon.orogIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - IyrGre.orog: 'This is needed in case the ice sheet elevation changes in time'

- ui-label
    - LImon.orogIs: 'Ice Sheet Surface Altitude'
    - IyrGre.orog: 'Surface Altitude'

- cell-measures
    - LImon.orogIs: 'area: areacella'
    - IyrGre.orog: 'area: areacellg'

- model-realm
    - LImon.orogIs: 'landIce'
    - IyrGre.orog: 'land'

- physical-parameter-name
    - LImon.orogIs: 'orogIs'
    - IyrGre.orog: 'orog'

- variable-root
    - LImon.orogIs: 'orogis'
    - IyrGre.orog: 'orog'


**phalf_tavg-alh-hxy-u**

- description
    - CFday.phalf: 'Air pressure on model half-levels'
    - AERmon.phalf: 'The atmospheric pressure at the model layer interfaces for all times and levels in the associated output variables'


**phymisc_tavg-d0m-hxy-sea**

- ui-label
    - Oday.phymiscos: 'Surface concentration of miscellaneous phytoplankton'
    - Omon.phymiscos: 'Surface Mole Concentration of Miscellaneous Phytoplankton Expressed as Carbon in Sea Water'

- description
    - Oday.phymiscos: 'Mole Concentration of Miscellaneous Phytoplankton Expressed as Carbon in Sea Water'
    - Omon.phymiscos: 'carbon concentration from additional phytoplankton component alone'

- cell-measures
    - Oday.phymiscos: 'area: areacello volume: volcello'
    - Omon.phymiscos: 'area: areacello'


**phypico_tavg-d0m-hxy-sea**

- ui-label
    - Omon.phypicoos: 'Surface Mole Concentration of Picophytoplankton Expressed as Carbon in Sea Water'
    - Oday.phypico: 'Carbon concentration of picophytoplankton'

- description
    - Omon.phypicoos: 'carbon concentration from the picophytoplankton (<2 um) component alone'
    - Oday.phypico: 'Mole Concentration of Picophytoplankton Expressed as Carbon in Sea Water'

- cell-measures
    - Omon.phypicoos: 'area: areacello'
    - Oday.phypico: 'area: areacello volume: volcello'

- physical-parameter-name
    - Omon.phypicoos: 'phypicoos'
    - Oday.phypico: 'phypico'

- variable-root
    - Omon.phypicoos: 'phypicoos'
    - Oday.phypico: 'phypico'


**pr_tavg-u-hxy-u**

- description
    - 6hrPlev.pr: 'includes both liquid and solid phases'
    - 3hr.pr: 'at surface; includes both liquid and solid phases.  This is the 3-hour mean precipitation flux.'
    - Amon.pr: 'at surface; includes both liquid and solid phases from all types of clouds (both large-scale and convective)'
    - E1hr.pr: 'Total precipitation flux'
    - day.pr: 'at surface; includes both liquid and solid phases from all types of clouds (both large-scale and convective)'


**ph_tavg-d0m-hxy-sea**

- description
    - Omon.phos: 'negative log10 of hydrogen ion concentration with the concentration expressed as mol H kg-1.'
    - Oday.phos: 'Near surface negative log10 of hydrogen ion concentration with the concentration expressed as mol H kg-1.'


**phycalc_tavg-ol-hxy-sea**

- description
    - Omon.phycalc: 'carbon concentration from calcareous (calcite-producing) phytoplankton component alone'
    - Oday.phycalc: 'Mole Concentration of Calcareous Phytoplankton Expressed as Carbon in Sea Water'


**phyc_tavg-d0m-hxy-sea**

- description
    - Omon.phycos: 'sum of phytoplankton carbon component concentrations.  In most (all?) cases this is the sum of phycdiat and phycmisc (i.e., "Diatom Carbon Concentration" and "Non-Diatom Phytoplankton Carbon Concentration"'
    - Oday.phycos: 'sum of phytoplankton organic carbon component concentrations at the sea surface'


**pr_tmax-u-hxy-u**

- description
    - Eday.prhmax: 'Daily Maximum Hourly Precipitation Rate'
    - 6hrPlev.prhmax: 'In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'
    - Emon.prhmax: 'In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'


**prra_tavg-u-hxy-u**

- description
    - Amon.prra: 'Rainfall rate at surface: Includes precipitation of all forms of water in the liquid phase'
    - 6hrPlev.prra: 'Precipitation rate at surface: Includes precipitation of all forms of water in the liquid phase'


**pr_tpt-u-hxy-u**

- ui-label
    - CF3hr.pr: 'Precipitation'
    - 6hrPlevPt.pr: 'surface precipitation'

- description
    - CF3hr.pr: 'at surface; includes both liquid and solid phases from all types of clouds (both large-scale and convective)'
    - 6hrPlevPt.pr: 'Total precipitation rate at the surface'


**prw_tavg-u-hxy-u**

- description
    - E3hr.prw: 'Column-integrated water vapour'
    - Amon.prwSouth30: 'vertically integrated through the atmospheric column'
    - Eday.prw: 'vertically integrated through the atmospheric column'


**prra_tavg-u-hxy-is**

- dimensions
    - ImonGre.prra: ['xgre', 'ygre', 'time']
    - ImonAnt.prra: ['xant', 'yant', 'time']
    - LImon.prraIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.prraIs: 'Ice Sheet Rainfall Rate'
    - ImonGre.prra: 'Rainfall Flux over Land Ice'

- description
    - LImon.prraIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.prra: 'over Land Ice//quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods'

- cell-measures
    - LImon.prraIs: 'area: areacella'
    - ImonGre.prra: 'area: areacellg'

- model-realm
    - LImon.prraIs: 'landIce'
    - ImonGre.prra: 'atmos'

- physical-parameter-name
    - LImon.prraIs: 'prraIs'
    - ImonGre.prra: 'prra'

- variable-root
    - LImon.prraIs: 'prrais'
    - ImonGre.prra: 'prra'


**prw_tpt-u-hxy-u**

- ui-label
    - 6hrPlevPt.prw: '6 hourly instantaneous vertically integrated water vapor'
    - CF3hr.prw: 'Water Vapor Path'

- description
    - 6hrPlevPt.prw: 'Vertically integrated mass of water vapour'
    - CF3hr.prw: 'vertically integrated through the atmospheric column'

- cell-methods
    - 6hrPlevPt.prw: 'time: point'
    - CF3hr.prw: 'area: mean time: point'


**prsn_tavg-u-hxy-u**

- ui-label
    - 6hrPlev.prsn: 'Snowfall Rate'
    - 3hr.prsn: 'Snowfall Flux'
    - Amon.prsnSouth30: 'Snowfall Flux'

- description
    - 6hrPlev.prsn: 'Precipitation rate at surface: Includes precipitation of all forms of water in the solid phase.'
    - 3hr.prsn: 'at surface.  Includes precipitation of all forms water in the solid phase.  This is the 3-hour mean snowfall flux.'
    - Amon.prsnSouth30: 'at surface; includes precipitation of all forms of water in the solid phase'


**prsn_tavg-u-hxy-is**

- ui-label
    - ImonAnt.prsn: 'Snowfall Flux'
    - LImon.prsnIs: 'Ice Sheet Snowfall Flux'

- description
    - ImonAnt.prsn: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods'
    - LImon.prsnIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'

- cell-measures
    - ImonAnt.prsn: 'area: areacellg'
    - LImon.prsnIs: 'area: areacella'

- dimensions
    - ImonAnt.prsn: ['xant', 'yant', 'time']
    - LImon.prsnIs: ['longitude', 'latitude', 'time']
    - ImonGre.prsn: ['xgre', 'ygre', 'time']

- model-realm
    - ImonAnt.prsn: 'atmos'
    - LImon.prsnIs: 'landIce'

- physical-parameter-name
    - ImonAnt.prsn: 'prsn'
    - LImon.prsnIs: 'prsnIs'

- variable-root
    - ImonAnt.prsn: 'prsn'
    - LImon.prsnIs: 'prsnis'


**ps_tpt-u-hxy-u**

- description
    - 6hrLev.ps: 'surface pressure, not mean sea level pressure'
    - 3hr.ps: 'sampled synoptically to diagnose atmospheric tides, this is better than mean sea level pressure.'
    - E1hr.ps: 'Surface pressure.'


**ps_tavg-u-hxy-u**

- description
    - CFday.ps: 'surface pressure (not mean sea-level pressure), 2-D field to calculate the 3-D pressure field from hybrid coordinates'
    - 6hrPlev.ps: 'Surface pressure, not mean sea level pressure'
    - Amon.ps: 'not, in general, the same as mean sea-level pressure'
    - AERhr.ps: 'surface pressure (not mean sea-level pressure), 2-D field to calculate the 3-D pressure field from hybrid coordinates'


**psl_tavg-u-hxy-u**

- description
    - Amon.psl: 'not, in general, the same as surface pressure'
    - 6hrPlev.psl: 'Sea Level Pressure'
    - day.psl: 'Sea Level Pressure'
    - Amon.pslSouth30: 'not, in general, the same as surface pressure'


**psl_tpt-u-hxy-u**

- description
    - E1hr.psl: 'Sea level pressure'
    - 6hrPlevPt.psl: 'Sea Level Pressure'


**reffsclwtop_tavg-u-hxy-scl**

- description
    - Emon.reffsclwtop: 'Cloud-Top Effective Droplet Radius in Stratiform Cloud'
    - Eday.reffsclwtop: 'Droplets are liquid only.  This is the effective radius "as seen from space" over liquid stratiform cloudy portion of grid cell.  This is the value from uppermost model layer with liquid cloud or, if available, or for some models it is the sum over all liquid cloud tops, no matter where they occur, as long as they are seen from the top of the atmosphere. Reported values are weighted by total liquid cloud top fraction of  (as seen from TOA) each time sample when computing monthly mean.daily data, separated to large-scale clouds, convective clouds. If any of the cloud is from more than one process (i.e. shallow convection), please provide them separately.'


**reffcclwtop_tavg-u-hxy-ccl**

- description
    - Emon.reffcclwtop: 'Cloud-Top Effective Droplet Radius in Convective Cloud'
    - Eday.reffcclwtop: 'Droplets are liquid only.  This is the effective radius "as seen from space" over convective liquid cloudy portion of grid cell.  This is the value from uppermost model layer with liquid cloud or, if available, or for some models it is the sum over all liquid cloud tops, no matter where they occur, as long as they are seen from the top of the atmosphere. Reported values are weighted by total liquid cloud top fraction of  (as seen from TOA) each time sample when computing monthly mean.daily data, separated to large-scale clouds, convective clouds. If any of the cloud is from more than one process (i.e. shallow convection), please provide them separately.'


**residualFrac_tavg-u-hxy-u**

- description
    - Lmon.residualFrac: 'fraction of entire grid cell  that is land and is covered by "non-vegetation" and "non-bare-soil" (e.g., urban, ice, lakes, etc.)'
    - Eyr.residualFrac: 'Percentage of entire grid cell  that is land and is covered by  neither vegetation nor bare-soil (e.g., urban, ice, lakes, etc.)'


**rlds_tavg-u-hxy-u**

- description
    - E1hr.rlds: 'Surface Downwelling Longwave Radiation'
    - day.rlds: 'The surface called "surface" means the lower boundary of the atmosphere. "longwave" means longwave radiation. Downwelling radiation is radiation from above. It does not mean "net downward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'
    - 3hr.rlds: 'This is the 3-hour mean flux.'
    - E1hr.rldsSouth30: 'Surface Downwelling Longwave Radiation'
    - 6hrPlev.rlds: 'Surface downwelling longwave radiation'
    - Amon.rlds: 'The surface called "surface" means the lower boundary of the atmosphere. "longwave" means longwave radiation. Downwelling radiation is radiation from above. It does not mean "net downward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'


**rlds_tavg-u-hxy-is**

- dimensions
    - ImonGre.rlds: ['xgre', 'ygre', 'time']
    - ImonAnt.rlds: ['xant', 'yant', 'time']
    - LImon.rldsIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.rldsIs: 'Ice Sheet Surface Downwelling Longwave Radiation'
    - ImonGre.rlds: 'Surface Downwelling Longwave Radiation'

- description
    - LImon.rldsIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.rlds: 'The surface called "surface" means the lower boundary of the atmosphere. "longwave" means longwave radiation. Downwelling radiation is radiation from above. It does not mean "net downward". When thought of as being incident on a surface, a radiative flux is sometimes called "irradiance". In addition, it is identical with the quantity measured by a cosine-collector light-meter and sometimes called "vector irradiance". In accordance with common usage in geophysical disciplines, "flux" implies per unit area, called "flux density" in physics.'

- cell-measures
    - LImon.rldsIs: 'area: areacella'
    - ImonGre.rlds: 'area: areacellg'

- model-realm
    - LImon.rldsIs: 'landIce'
    - ImonGre.rlds: 'atmos'

- physical-parameter-name
    - LImon.rldsIs: 'rldsIs'
    - ImonGre.rlds: 'rlds'

- variable-root
    - LImon.rldsIs: 'rldsis'
    - ImonGre.rlds: 'rlds'


**areacell_ti-u-hxy-u**

- ui-label
    - IfxAnt.areacellg: 'Grid-Cell Area for Ice Sheet Variables'
    - fx.areacella: 'Grid-Cell Area for Atmospheric Grid Variables'
    - Ofx.areacello: 'Grid-Cell Area for Ocean Variables'
    - IfxGre.areacellg: 'Grid-Cell Area for Ice Sheet Variables'
    - fx.areacellr: 'Grid-Cell Area for River Model Variables'

- description
    - IfxAnt.areacellg: 'Cell areas any grid used to report ice sheet variables. These cell areas should be defined to enable exact calculation of area integrals (e.g., of vertical fluxes of energy at the surface and top of the atmosphere)'
    - fx.areacella: 'Cell areas for any grid used to report atmospheric variables and any other variable using that grid (e.g., soil moisture content). These cell areas should be defined to enable exact calculation of global integrals (e.g., of vertical fluxes of energy at the surface and top of the atmosphere).'
    - Ofx.areacello: 'Cell areas for any grid used to report ocean variables and variables which are requested as used on the model ocean grid (e.g. hfsso, which is a downward heat flux from the atmosphere interpolated onto the ocean grid). These cell areas should be defined to enable exact calculation of global integrals (e.g., of vertical fluxes of energy at the surface and top of the atmosphere).'
    - IfxGre.areacellg: 'Cell areas any grid used to report ice sheet variables. These cell areas should be defined to enable exact calculation of area integrals (e.g., of vertical fluxes of energy at the surface and top of the atmosphere)'
    - fx.areacellr: 'Cell areas for any grid used to report river model variables (may be the same as for atmospheric variables). These cell areas should be defined to enable exact calculation of area integrals (e.g., of vertical fluxes of energy at the surface and top of the atmosphere).'

- model-realm
    - IfxAnt.areacellg: 'land'
    - fx.areacella: 'atmos'
    - Ofx.areacello: 'ocean'
    - IfxGre.areacellg: 'land'
    - fx.areacellr: 'land'

- physical-parameter-name
    - IfxAnt.areacellg: 'areacellg'
    - fx.areacella: 'areacella'
    - Ofx.areacello: 'areacello'
    - IfxGre.areacellg: 'areacellg'
    - fx.areacellr: 'areacellr'

- variable-root
    - IfxAnt.areacellg: 'areacellg'
    - fx.areacella: 'areacella'
    - Ofx.areacello: 'areacello'
    - IfxGre.areacellg: 'areacellg'
    - fx.areacellr: 'areacellr'


**albisccp_tavg-u-hxy-cl**

- description
    - CFmon.albisccp: 'time-means weighted by the ISCCP Total Cloud Fraction - see <https://www.cfmip.org/tools-and-data/cosp>'
    - CFday.albisccp: 'time-means are weighted by the ISCCP Total Cloud Fraction - see  <https://www.cfmip.org/tools-and-data/cosp>'


**acabf_tavg-u-hxy-is**

- dimensions
    - ImonGre.acabf: ['xgre', 'ygre', 'time']
    - ImonAnt.acabf: ['xant', 'yant', 'time']
    - IyrAnt.acabf: ['xant', 'yant', 'time']
    - LImon.acabfIs: ['longitude', 'latitude', 'time']
    - IyrGre.acabf: ['xgre', 'ygre', 'time']

- description
    - IyrAnt.acabf: 'quantity averaged over ice sheet only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.acabf: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods, and as forcing for ISM'
    - LImon.acabfIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - IyrGre.acabf: 'quantity averaged over ice sheet only, to avoid contamination from other surfaces (eg: permafrost)'

- ui-label
    - LImon.acabfIs: 'Ice Sheet Surface Mass Balance Flux'
    - IyrAnt.acabf: 'Surface Mass Balance Flux'
    - IyrGre.acabf: 'Surface Mass Balance Flux'

- cell-measures
    - LImon.acabfIs: 'area: areacella'
    - IyrAnt.acabf: 'area: areacellg'
    - IyrGre.acabf: 'area: areacellg'

- physical-parameter-name
    - LImon.acabfIs: 'acabfIs'
    - IyrAnt.acabf: 'acabf'
    - IyrGre.acabf: 'acabf'

- variable-root
    - LImon.acabfIs: 'acabfis'
    - IyrAnt.acabf: 'acabf'
    - IyrGre.acabf: 'acabf'


**bldep_tavg-u-hxy-u**

- ui-label
    - E1hr.bldep: 'Boundary layer depth'
    - AERmon.bldep: 'Boundary Layer Depth'

- description
    - E1hr.bldep: 'Boundary Layer depth'
    - AERmon.bldep: 'Boundary layer depth'


**ccldncl_tavg-u-hxy-ccl**

- description
    - Emon.ccldncl: 'Cloud Droplet Number Concentration of Convective Cloud Tops'
    - Eday.ccldncl: "Droplets are liquid only.  Report concentration 'as seen from space' over convective liquid cloudy portion of grid cell.  This is the value from uppermost model layer with liquid cloud or, if available, it is better to sum over all liquid cloud tops, no matter where they occur, as long as they are seen from the top of the atmosphere. Weight by total liquid cloud top fraction of  (as seen from TOA) each time sample when computing monthly mean."


**chl_tavg-d0m-hxy-sea**

- description
    - Omon.chlos: 'sum of chlorophyll from all phytoplankton group concentrations.  In most models this is equal to chldiat+chlmisc, that is the sum of "Diatom Chlorophyll Mass Concentration" plus "Other Phytoplankton Chlorophyll Mass Concentration"'
    - Oday.chlos: 'sum of chlorophyll from all phytoplankton group concentrations at the sea surface.  In most models this is equal to chldiat+chlmisc, that is the sum of "Diatom Chlorophyll Mass Concentration" plus "Other Phytoplankton Chlorophyll Mass Concentration"'

- dimensions
    - Omon.chlos: ['longitude', 'latitude', 'time']
    - Oday.chlos: ['longitude', 'latitude', 'time', 'depth0m']


**cl_tavg-al-hxy-u**

- description
    - CFday.cl: 'Percentage cloud cover, including both large-scale and convective cloud.'
    - Amon.clSouth30: 'Includes both large-scale and convective cloud.'


**cli_tavg-al-hxy-u**

- description
    - CFday.cli: 'Calculated as the mass of cloud ice  in the grid cell divided by the mass of air (including the water in all phases) in the grid cell.  This includes precipitating hydrometeors ONLY if the precipitating hydrometeors affect the calculation of radiative transfer in model.'
    - Amon.cliSouth30: 'Includes both large-scale and convective cloud.  This is calculated as the mass of cloud ice in the grid cell divided by the mass of air (including the water in all phases) in the grid cell. It includes precipitating hydrometeors ONLY if the precipitating hydrometeors affect the calculation of radiative transfer in model.'


**clivi_tavg-u-hxy-u**

- description
    - Amon.clivi: 'mass of ice water in the column divided by the area of the column (not just the area of the cloudy portion of the column). Includes precipitating frozen hydrometeors ONLY if the precipitating hydrometeor affects the calculation of radiative transfer in model.'
    - E3hr.clivi: 'Ice water path'
    - CFday.clivi: 'calculate mass of ice water in the column divided by the area of the column (not just the area of the cloudy portion of the column). This includes precipitating frozen hydrometeors ONLY if the precipitating hydrometeors affect the calculation of radiative transfer in model.'
    - Amon.cliviSouth30: 'mass of ice water in the column divided by the area of the column (not just the area of the cloudy portion of the column). Includes precipitating frozen hydrometeors ONLY if the precipitating hydrometeor affects the calculation of radiative transfer in model.'


**clt_tavg-u-hxy-u**

- description
    - Amon.clt: 'for the whole atmospheric column, as seen from the surface or the top of the atmosphere. Include both large-scale and convective cloud.'
    - 3hr.clt: 'for the whole atmospheric column, as seen from the surface or the top of the atmosphere. Include both large-scale and convective cloud.  This is a 3-hour mean.'
    - day.clt: 'for the whole atmospheric column, as seen from the surface or the top of the atmosphere. Includes both large-scale and convective cloud.'
    - Amon.cltSouth30: 'for the whole atmospheric column, as seen from the surface or the top of the atmosphere. Include both large-scale and convective cloud.'
    - E1hr.clt: 'Total cloud area fraction (reported as a percentage) for the whole atmospheric column, as seen from the surface or the top of the atmosphere. Includes both large-scale and convective cloud.'


**cltmodis_tavg-u-hxy-u**

- ui-label
    - Emon.cltmodis: 'MODIS Total Cloud Cover Percentage'
    - CFmon.cltmodisSouth30: 'MODIS Total Cloud Area Fraction'


**clw_tavg-al-hxy-u**

- description
    - Amon.clw: 'Includes both large-scale and convective cloud.  Calculate as the mass of cloud liquid water in the grid cell divided by the mass of air (including the water in all phases) in the grid cells. Precipitating hydrometeors are included ONLY if the precipitating hydrometeors affect the calculation of radiative transfer in model.'
    - CFday.clw: 'Calculated as the mass of  cloud liquid water in the grid cell divided by the mass of air (including the water in all phases) in the grid cell.  This includes precipitating hydrometeors ONLY if the precipitating hydrometeors affect the calculation of radiative transfer in model.'


**siage_tavg-u-hxy-si**

- ui-label
    - SImon.siage: 'Age of Sea Ice'
    - SIday.siage: 'Age of Sea Ice\n'


**siarea_tavg-u-hm-u**

- ui-label
    - SIday.siareas: 'Sea-Ice Area South'
    - SImon.siarean: 'Sea-Ice Area North'

- description
    - SIday.siareas: 'Total integrated area of sea ice in the Southern Hemisphere (where siconc > 0). Does not include grid cells partially covered by land.'
    - SImon.siarean: 'Total integrated area of sea ice in the Northern Hemisphere (where siconc > 0). Does not include grid cells partially covered by land.'

- physical-parameter-name
    - SIday.siareas: 'siareas'
    - SImon.siarean: 'siarean'

- variable-root
    - SIday.siareas: 'siareas'
    - SImon.siarean: 'siarean'


**siflsensbot_tavg-u-hxy-si**

- ui-label
    - SImon.siflsensbot: 'Net Upward Sensible Heat Flux under Sea Ice'
    - SIday.siflsensbot: 'Net Upward Sensible Heat Flux under Sea Ice\n'


**siflsenstop_tavg-u-hxy-si**

- ui-label
    - SIday.siflsenstop: 'Net Downward Sensible Heat Flux over Sea Ice\n'
    - SImon.siflsenstop: 'Net Downward Sensible Heat Flux over Sea Ice'

- cell-measures
    - SIday.siflsenstop: 'area: areacello'
    - SImon.siflsenstop: 'area: areacella'

- cell-methods
    - SIday.siflsenstop: 'area: time: mean where sea_ice (mask=siconc)'
    - SImon.siflsenstop: 'area: time: mean where sea_ice (mask=siconca)'


**siflcondbot_tavg-u-hxy-si**

- ui-label
    - SImon.siflcondbot: 'Net Conductive Heat Flux in Sea Ice at the Base'
    - SIday.siflcondbot: 'Net Conductive Heat Flux in Sea Ice at the Base\n'


**siflcondtop_tavg-u-hxy-si**

- ui-label
    - SImon.siflcondtop: 'Net Conductive Heat Flux in Sea Ice at the Surface'
    - SIday.siflcondtop: 'Net Conductive Heat Flux in Sea Ice at the Surface\n'


**sifllattop_tavg-u-hxy-si**

- ui-label
    - SImon.sifllattop: 'Net Latent Heat Flux over Sea Ice'
    - SIday.sifllattop: 'Net Latent Heat Flux over Sea Ice\n'

- cell-measures
    - SImon.sifllattop: 'area: areacella'
    - SIday.sifllattop: 'area: areacello'

- cell-methods
    - SImon.sifllattop: 'area: time: mean where sea_ice (mask=siconca)'
    - SIday.sifllattop: 'area: time: mean where sea_ice (mask=siconc)'


**rlds_tavg-u-hxy-si**

- cell-measures
    - SImon.sifllwdtop: 'area: areacella'
    - SIday.sifllwdtop: 'area: areacello'

- cell-methods
    - SImon.sifllwdtop: 'area: time: mean where sea_ice (mask=siconca)'
    - SIday.sifllwdtop: 'area: time: mean where sea_ice (mask=siconc)'


**rlus_tavg-u-hxy-si**

- ui-label
    - SIday.sifllwutop: 'Upwelling Longwave Flux over Sea Ice\n'
    - SImon.sifllwutop: 'Upwelling Longwave Flux over Sea Ice'

- cell-measures
    - SIday.sifllwutop: 'area: areacello'
    - SImon.sifllwutop: 'area: areacella'

- cell-methods
    - SIday.sifllwutop: 'area: time: mean where sea_ice (mask=siconc)'
    - SImon.sifllwutop: 'area: time: mean where sea_ice (mask=siconca)'


**siextent_tavg-u-hm-u**

- ui-label
    - SIday.siextents: 'Sea-Ice Extent South'
    - SImon.siextentn: 'Sea-Ice Extent North'

- description
    - SIday.siextents: 'Total integrated area of all Southern Hemisphere grid cells that are covered by at least 15% areal fraction of sea ice (siconc >= 0.15). Does not include grid cells partially covered by land.'
    - SImon.siextentn: 'Total integrated area of all Northern Hemisphere grid cells that are covered by at least 15% areal fraction of sea ice (siconc >= 0.15). Does not include grid cells partially covered by land.'

- physical-parameter-name
    - SIday.siextents: 'siextents'
    - SImon.siextentn: 'siextentn'

- variable-root
    - SIday.siextents: 'siextents'
    - SImon.siextentn: 'siextentn'


**sifb_tavg-u-hxy-si**

- ui-label
    - SIday.sifb: 'Sea-Ice Freeboard\n'
    - SImon.sifb: 'Sea-Ice Freeboard'


**simprefrozen_tavg-u-hxy-simp**

- ui-label
    - SImon.simprefrozen: 'Thickness of Refrozen Ice on Melt Pond'
    - SIday.simprefrozen: 'Thickness of Refrozen Ice on Melt Pond\n'


**rsds_tavg-u-hxy-si**

- ui-label
    - SIday.siflswdtop: 'Downwelling Shortwave Flux over Sea Ice\n'
    - Emon.rsdssi: 'Surface Downwelling Shortwave Radiation over Sea Ice'
    - SImon.siflswdtop: 'Downwelling Shortwave Flux over Sea Ice'

- description
    - SIday.siflswdtop: 'Downwelling shortwave flux from the atmosphere to the sea-ice surface (energy flow per sea ice area). Always positive or zero.'
    - Emon.rsdssi: 'Surface Downwelling Shortwave Radiation over the portion of an ocean grid cell covered by sea ice, including snow. Can be used for computation of surface albedo.'
    - SImon.siflswdtop: 'Downwelling shortwave flux from the atmosphere to the sea-ice surface\xa0(energy flow per sea ice area). Always positive or zero.'

- model-realm
    - SIday.siflswdtop: 'seaIce'
    - Emon.rsdssi: 'ocean'

- physical-parameter-name
    - SIday.siflswdtop: 'siflswdtop'
    - Emon.rsdssi: 'rsdssi'

- variable-root
    - SIday.siflswdtop: 'siflswdtop'
    - Emon.rsdssi: 'rsdssi'

- cell-measures
    - SImon.siflswdtop: 'area: areacella'
    - SIday.siflswdtop: 'area: areacello'

- cell-methods
    - SImon.siflswdtop: 'area: time: mean where sea_ice (mask=siconca)'
    - SIday.siflswdtop: 'area: time: mean where sea_ice (mask=siconc)'


**rsus_tavg-u-hxy-si**

- ui-label
    - SIday.siflswutop: 'Upwelling Shortwave Flux over Sea Ice'
    - Emon.rsussi: 'Surface Upwelling Shortwave Radiation over Sea Ice'

- description
    - SIday.siflswutop: 'Upward shortwave flux from the sea-ice surface to the atmosphere\xa0(energy flow per sea ice area). Always positive or zero.'
    - Emon.rsussi: 'Surface Upwelling Shortwave Radiation over the portion of an ocean grid cell covered by sea ice, including snow. Can be used for computation of surface albedo.'

- model-realm
    - SIday.siflswutop: 'seaIce'
    - Emon.rsussi: 'ocean'

- physical-parameter-name
    - SIday.siflswutop: 'siflswutop'
    - Emon.rsussi: 'rsussi'

- variable-root
    - SIday.siflswutop: 'siflswutop'
    - Emon.rsussi: 'rsussi'

- cell-measures
    - SImon.siflswutop: 'area: areacella'
    - SIday.siflswutop: 'area: areacello'

- cell-methods
    - SImon.siflswutop: 'area: time: mean where sea_ice (mask=siconca)'
    - SIday.siflswutop: 'area: time: mean where sea_ice (mask=siconc)'


**siitdthick_tavg-u-hxy-si**

- ui-label
    - SImon.siitdthick: 'Sea-Ice Thickness in Ice Thickness Categories'
    - SIday.siitdthick: 'Sea-Ice Thickness in Ice Thickness Categories\n'

- cell-methods
    - SImon.siitdthick: 'area: time: mean where sea_ice (mask=siitdconc)'
    - SIday.siitdthick: 'area: time: mean where sea_ice (mask=siconc)'


**simpconc_tavg-u-hxy-si**

- ui-label
    - SImon.simpconc: 'Fraction of Sea Ice Covered by Melt Pond'
    - SIday.simpconc: 'Fraction of Sea Ice Covered by Melt Pond\n'


**siitdconc_tavg-u-hxy-u**

- ui-label
    - SImon.siitdconc: 'Sea-Ice Area Fractions in Ice Thickness Categories'
    - SIday.siitdconc: 'Sea-Ice Area Fractions in Ice Thickness Categories\n'


**siitdsnthick_tavg-u-hxy-si**

- ui-label
    - SIday.siitdsnthick: 'Snow Thickness in Ice Thickness Categories\n'
    - SImon.siitdsnthick: 'Snow Thickness in Ice Thickness Categories'

- cell-methods
    - SIday.siitdsnthick: 'area: time: mean where sea_ice (mask=siconc)'
    - SImon.siitdsnthick: 'area: time: mean where sea_ice (mask=siitdconc)'


**siitdsnconc_tavg-u-hxy-si**

- ui-label
    - SImon.siitdsnconc: 'Snow Area Fractions in Ice Thickness Categories'
    - SIday.siitdsnconc: 'Snow Area Fractions in Ice Thickness Categories\n'

- cell-methods
    - SImon.siitdsnconc: 'area: time: mean where sea_ice (mask=siitdconc)'
    - SIday.siitdsnconc: 'area: time: mean where sea_ice (mask=siconc)'


**sisnmass_tavg-u-hm-u**

- ui-label
    - SIday.sisnmasss: 'Snow Mass on Sea Ice South'
    - SImon.sisnmassn: 'Snow Mass on Sea Ice North'
    - SIday.sisnmassn: 'Snow Mass on Sea Ice North'
    - SImon.sisnmasss: 'Snow Mass on Sea Ice South'

- description
    - SIday.sisnmasss: 'Total integrated mass of snow on sea ice in the Southern Hemisphere.'
    - SImon.sisnmassn: 'Total integrated mass of snow on sea ice in the Northern Hemisphere.'
    - SIday.sisnmassn: 'Total integrated mass of snow on sea ice in the Northern Hemisphere.'
    - SImon.sisnmasss: 'Total integrated mass of snow on sea ice in the Southern Hemisphere.'

- physical-parameter-name
    - SIday.sisnmasss: 'sisnmasss'
    - SImon.sisnmassn: 'sisnmassn'
    - SIday.sisnmassn: 'sisnmassn'
    - SImon.sisnmasss: 'sisnmasss'

- variable-root
    - SIday.sisnmasss: 'sisnmasss'
    - SImon.sisnmassn: 'sisnmassn'
    - SIday.sisnmassn: 'sisnmassn'
    - SImon.sisnmasss: 'sisnmasss'


**sirdgconc_tavg-u-hxy-si**

- ui-label
    - SImon.sirdgconc: 'Fraction of Ridged Sea Ice'
    - SIday.sirdgconc: 'Fraction of Ridged Sea Ice\n'

- dimensions
    - SImon.sirdgconc: ['longitude', 'latitude', 'time', 'typesirdg']
    - SIday.sirdgconc: ['longitude', 'latitude', 'time']


**sithick_tavg-u-hxy-sir**

- ui-label
    - SImon.sirdgthick: 'Ridged Ice Thickness'
    - SIday.sirdgthick: 'Ridged Ice Thickness\n'


**sisali_tavg-u-hxy-si**

- ui-label
    - SImon.sisali: 'Sea-Ice Salinity'
    - SIday.sisali: 'Sea-Ice Salinity\n'


**sisaltmass_tavg-u-hxy-sea**

- ui-label
    - SImon.sisaltmass: 'Mass of Salt in Sea Ice'
    - SIday.sisaltmass: 'Mass of Salt in Sea Ice\n'


**sitempbot_tavg-u-hxy-si**

- ui-label
    - SIday.sitempbot: 'Temperature at Ice-Ocean Interface\n'
    - SImon.sitempbot: 'Temperature at Ice-Ocean Interface'


**sivol_tavg-u-hm-u**

- ui-label
    - SIday.sivoln: 'Sea-Ice Volume North'
    - SImon.sivols: 'Sea-Ice Volume South'

- description
    - SIday.sivoln: 'Total integrated volume of sea ice in the Northern Hemisphere.'
    - SImon.sivols: 'Total integrated volume of sea ice in the Southern Hemisphere.'

- physical-parameter-name
    - SIday.sivoln: 'sivoln'
    - SImon.sivols: 'sivols'

- variable-root
    - SIday.sivoln: 'sivoln'
    - SImon.sivols: 'sivols'


**snc_tavg-u-hxy-is**

- dimensions
    - ImonGre.snc: ['xgre', 'ygre', 'time']
    - ImonAnt.snc: ['xant', 'yant', 'time']
    - IyrAnt.snc: ['xant', 'yant', 'time']
    - IyrGre.snc: ['xgre', 'ygre', 'time']
    - LImon.sncIs: ['longitude', 'latitude', 'time']

- description
    - IyrGre.snc: 'quantity averaged over ice sheet  only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.snc: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - LImon.sncIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - IyrAnt.snc: 'quantity averaged over ice sheet  only, to avoid contamination from other surfaces (eg: permafrost)'

- ui-label
    - LImon.sncIs: 'Ice Sheet Snow Cover Percentage'
    - IyrAnt.snc: 'Snow Area Percentage'

- cell-measures
    - LImon.sncIs: 'area: areacella'
    - IyrAnt.snc: 'area: areacellg'

- physical-parameter-name
    - LImon.sncIs: 'sncIs'
    - IyrAnt.snc: 'snc'

- variable-root
    - LImon.sncIs: 'sncis'
    - IyrAnt.snc: 'snc'


**sitempsnic_tavg-u-hxy-si**

- ui-label
    - SImon.sitempsnic: 'Temperature at Snow-Ice Interface'
    - SIday.sitempsnic: 'Temperature at Snow-Ice Interface\n'


**snw_tavg-u-hxy-lnd**

- description
    - LImon.snw: 'Computed as the mass of surface snow on the land portion of the grid cell divided by the land area in the grid cell; reported as missing where the land fraction is 0; excluded is snow on vegetation canopy or on sea ice.'
    - day.snw: 'the mass of surface snow on the land portion of the grid cell divided by the land area in the grid cell; reported as missing where the land fraction is 0; excludes snow on vegetation canopy or on sea ice.'


**snc_tavg-u-hxy-lnd**

- description
    - LImon.snc: 'Fraction of each grid cell that is occupied by snow that rests on land portion of cell.'
    - day.snc: 'Percentage of each grid cell that is occupied by snow that rests on land portion of cell.'

- cell-methods
    - LImon.snc: 'area: time: mean'
    - day.snc: 'area: mean where land time: mean'


**snm_tavg-u-hxy-lnd**

- description
    - LImon.snm: 'Computed as the total surface melt water on the land portion of the grid cell divided by the land area in the grid cell; report as 0.0 for snow-free land regions; report as missing where the land fraction is 0.'
    - Eday.snm: 'surface\\_snow\\_and\\_ice\\_melt\\_flux'


**snm_tavg-u-hxy-is**

- dimensions
    - ImonGre.snm: ['xgre', 'ygre', 'time']
    - ImonAnt.snm: ['xant', 'yant', 'time']
    - LImon.snmIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.snmIs: 'Ice Sheet Surface Snow Melt'
    - ImonGre.snm: 'Surface Snow Melt'

- description
    - LImon.snmIs: 'Loss of snow mass resulting from surface melting. Computed as the surface melt water from snow on the ice sheet portion of the grid cell divided by the ice\\_sheet area in the grid cell; report as 0.0 for snow-free land\\_ice regions; report as missing where the land fraction is 0.'
    - ImonGre.snm: 'The total surface snow melt rate on the land portion of the grid cell divided by the land area in the grid cell; report as zero for snow-free land regions and missing where there is no land.'

- cell-measures
    - LImon.snmIs: 'area: areacella'
    - ImonGre.snm: 'area: areacellg'

- physical-parameter-name
    - LImon.snmIs: 'snmIs'
    - ImonGre.snm: 'snm'

- variable-root
    - LImon.snmIs: 'snmis'
    - ImonGre.snm: 'snm'


**snd_tavg-u-hxy-lnd**

- description
    - LImon.snd: 'where land over land, this is computed as the mean thickness of snow in the land portion of the grid cell (averaging over the entire land portion, including the snow-free fraction).  Reported as missing where the land fraction is 0.'
    - Eday.snd: 'where land over land, this is computed as the mean thickness of snow in the land portion of the grid cell (averaging over the entire land portion, including the snow-free fraction).  Reported as 0.0 where the land fraction is 0.'


**snrefr_tavg-u-hxy-is**

- dimensions
    - ImonGre.snicefreez: ['xgre', 'ygre', 'time']
    - ImonAnt.snicefreez: ['xant', 'yant', 'time']
    - LImon.snicefreezIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.snicefreezIs: 'Ice Sheet Surface Snow and Ice Refreeze Flux'
    - ImonGre.snicefreez: 'Surface Snow and Ice Refreeze Flux'

- description
    - LImon.snicefreezIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.snicefreez: 'Mass flux of surface meltwater which refreezes within the snowpack. Computed as the total refreezing on the land ice portion of the grid cell divided by land ice area in the grid cell.'

- cell-measures
    - LImon.snicefreezIs: 'area: areacella'
    - ImonGre.snicefreez: 'area: areacellg'

- physical-parameter-name
    - LImon.snicefreezIs: 'snicefreezIs'
    - ImonGre.snicefreez: 'snicefreez'

- variable-root
    - LImon.snicefreezIs: 'snicefreezis'
    - ImonGre.snicefreez: 'snicefreez'


**snicem_tavg-u-hxy-is**

- ui-label
    - ImonAnt.snicem: 'Surface Snow and Ice Melt Flux'
    - LImon.snicemIs: 'Ice Sheet Surface Snow and Ice Melt Flux'

- description
    - ImonAnt.snicem: 'Loss of snow and ice mass resulting from surface melting. Computed as the total surface melt on the land ice portion of the grid cell divided by land ice area in the grid cell.'
    - LImon.snicemIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'

- cell-measures
    - ImonAnt.snicem: 'area: areacellg'
    - LImon.snicemIs: 'area: areacella'

- dimensions
    - ImonAnt.snicem: ['xant', 'yant', 'time']
    - LImon.snicemIs: ['longitude', 'latitude', 'time']
    - ImonGre.snicem: ['xgre', 'ygre', 'time']

- physical-parameter-name
    - ImonAnt.snicem: 'snicem'
    - LImon.snicemIs: 'snicemIs'

- variable-root
    - ImonAnt.snicem: 'snicem'
    - LImon.snicemIs: 'snicemis'


**so_tavg-ol-hxy-sea**

- ui-label
    - Odec.so: 'Sea Water Salinity'
    - Oday.so: 'Sea water salinity'

- description
    - Odec.so: "Sea water salinity is the salt content of sea water, often on the Practical Salinity Scale of 1978. However, the unqualified term 'salinity' is generic and does not necessarily imply any particular method of calculation. The units of salinity are dimensionless and the units attribute should normally be given as 1e-3 or 0.001 i.e. parts per thousand."
    - Oday.so: "Sea water salinity is the salt content of sea water, often on the Practical Salinity Scale of 1978. However, the unqualified term 'salinity' is generic and does not necessarily imply any particular method of calculation."


**strbasemag_tavg-u-hxy-is**

- dimensions
    - IyrAnt.strbasemag: ['xant', 'yant', 'time']
    - IyrGre.strbasemag: ['xgre', 'ygre', 'time']


**so2_tavg-h2m-hxy-u**

- ui-label
    - E3hrPt.so2: 'Surface SO2 volume mixing ratio at CF sites'
    - AERday.so2: 'Surface daily mean SO2'

- description
    - E3hrPt.so2: 'This variable represents the instantaneous surface so2 volume mixing ration at CF sites, sampled every 3 hours'
    - AERday.so2: 'Daily mean SO2 volume mixing ratio in lowest model layer'

- cell-measures
    - E3hrPt.so2: '::MODEL'
    - AERday.so2: 'area: areacella'

- cell-methods
    - E3hrPt.so2: 'area: point time: point'
    - AERday.so2: 'area: time: mean'

- dimensions
    - E3hrPt.so2: ['site', 'time1', 'lowerModelLayer']
    - AERday.so2: ['longitude', 'latitude', 'time', 'lowerModelLayer']


**tas_tmax-h2m-hxy-u**

- description
    - day.tasmax: 'maximum near-surface (usually, 2 meter) air temperature (add cell\\_method attribute "time: max")'
    - Amon.tasmaxSouth30: 'monthly mean of the daily-maximum near-surface air temperature.'
    - Amon.tasmax: 'monthly mean of the daily-maximum near-surface air temperature.'

- cell-methods
    - day.tasmax: 'area: mean time: maximum'
    - Amon.tasmaxSouth30: 'area: mean time: maximum within days time: mean over days'
    - Amon.tasmax: 'area: mean time: maximum within days time: mean over days'

- dimensions
    - day.tasmax: ['longitude', 'latitude', 'time', 'height2m']
    - Amon.tasmaxSouth30: ['longitude', 'latitude', 'time4', 'height2m']
    - Amon.tasmax: ['longitude', 'latitude', 'time4', 'height2m']


**t20d_tavg-u-hxy-sea**

- description
    - Emon.t20d: 'Monthly 20C isotherm depth'
    - Eday.t20d: 'Daily 20C isotherm depth'


**ta_tavg-p39-hy-air**

- ui-label
    - EdayZ.ta: 'Zonal mean air temperature'
    - AERmonZ.ta: 'Air Temperature'

- description
    - EdayZ.ta: 'Zonal mean temperature of air with the extended number of vertical levels.'
    - AERmonZ.ta: 'Air Temperature'

- cell-measures
    - EdayZ.ta: 'area: areacella'
    - AERmonZ.ta: None


**tas_tavg-h2m-hxy-u**

- description
    - AERhr.tas: 'Temperature at surface'
    - 6hrPlev.tas: 'near-surface (usually, 2 meter) air temperature'
    - Amon.tas: 'near-surface (usually, 2 meter) air temperature'


**tauvo_tavg-u-hxy-sea**

- description
    - Odec.tauvo: 'This is the stress on the liquid ocean from overlying atmosphere, sea ice, ice shelf, etc.'
    - 3hr.tauvo: 'The stress on the liquid ocean from interactions with overlying atmosphere, sea ice, ice shelf, etc.'

- cell-measures
    - Odec.tauvo: 'area: areacello'
    - 3hr.tauvo: '::OPT'
    - Omon.tauvo: '::OPT'


**tas_tmin-h2m-hxy-u**

- description
    - day.tasmin: 'minimum near-surface (usually, 2 meter) air temperature (add cell\\_method attribute "time: min")'
    - Amon.tasminSouth30: 'monthly mean of the daily-minimum near-surface air temperature.'

- cell-methods
    - day.tasmin: 'area: mean time: minimum'
    - Amon.tasminSouth30: 'area: mean time: minimum within days time: mean over days'

- dimensions
    - day.tasmin: ['longitude', 'latitude', 'time', 'height2m']
    - Amon.tasminSouth30: ['longitude', 'latitude', 'time4', 'height2m']


**tauv_tavg-u-hxy-u**

- description
    - Eday.tauv: 'surface, now requesting daily output.'
    - Amon.tauv: 'Downward northward wind stress at the surface'


**tauuo_tavg-u-hxy-sea**

- description
    - Odec.tauuo: 'This is the stress on the liquid ocean from overlying atmosphere, sea ice, ice shelf, etc.'
    - 3hr.tauuo: 'The stress on the liquid ocean from interactions with overlying atmosphere, sea ice, ice shelf, etc.'

- cell-measures
    - Odec.tauuo: 'area: areacello'
    - 3hr.tauuo: '::OPT'
    - Omon.tauuo: '::OPT'


**tendacabf_tavg-u-hm-is**

- description
    - IyrGre.tendacabf: 'Greenland'
    - IyrAnt.tendacabf: 'Antarctica'


**tendlibmassbf_tavg-u-hm-is**

- description
    - IyrGre.tendlibmassbf: 'Greenland'
    - IyrAnt.tendlibmassbf: 'Antarctica'


**tendlicalvf_tavg-u-hm-is**

- description
    - IyrGre.tendlicalvf: 'Greenland'
    - IyrAnt.tendlicalvf: 'Antarctica'


**tntmp_tavg-p39-hy-air**

- ui-label
    - EdayZ.tntmp: 'Zonal mean tendency of air temperature due to model physics'
    - EmonZ.tntmp: 'Tendency of Air Temperature Due to Model Physics'


**tntrl_tavg-p39-hy-air**

- ui-label
    - EmonZ.tntrl: 'Tendency of Air Temperature Due to Longwave Radiative Heating'
    - EdayZ.tntrl: 'Zonal mean tendency of air temperature due to longwave heating, all sky'

- description
    - EmonZ.tntrl: 'zonal mean; hence YZT'
    - EdayZ.tntrl: 'Zonal mean tendency of air temperature due to longwave heating, all sky, with the extended number of vertical levels.'


**topg_ti-u-hxy-gis**

- dimensions
    - IfxGre.topg: ['xgre', 'ygre']
    - IfxAnt.topg: ['xant', 'yant']


**tntrs_tavg-p39-hy-air**

- ui-label
    - EdayZ.tntrs: 'Zonal mean tendency of air temperature due to shortwave heating, all sky'
    - EmonZ.tntrs: 'Tendency of Air Temperature Due to Shortwave Radiative Heating'

- description
    - EdayZ.tntrs: 'Zonal mean tendency of air temperature due to shortwave heating, all sky, with the extended number of vertical levels.'
    - EmonZ.tntrs: 'zonal mean; hence YZT'


**ts_tpt-u-hxy-u**

- description
    - CF3hr.ts: 'Surface temperature (skin for open ocean)'
    - 6hrPlevPt.ts: 'Temperature of the lower boundary of the atmosphere'


**topg_tavg-u-hxy-gis**

- dimensions
    - IyrGre.topg: ['xgre', 'ygre', 'time']
    - IyrAnt.topg: ['xant', 'yant', 'time']


**ts_tavg-u-hxy-u**

- ui-label
    - 6hrPlev.ts: 'Surface temperature '
    - E1hr.ts: 'Surface Temperature'
    - Eday.ts: 'Surface Temperature'


**toz_tavg-u-hxy-u**

- description
    - AERmon.toz: 'total ozone column in DU'
    - AERday.toz: 'Total ozone column'


**tpf_tavg-u-hxy-lnd**

- description
    - LImon.tpf: 'where land over land: This is the mean thickness of the permafrost layer in the land portion of the grid cell.  Reported as missing in permafrost-free regions.'
    - Eday.tpf: 'permafrost\\_layer\\_thickness'


**treeFrac_tavg-u-hxy-u**

- description
    - Lmon.treeFrac: 'fraction of entire grid cell  that is covered by trees.'
    - Eyr.treeFrac: 'Percentage of entire grid cell  that is covered by trees.'


**ts_tavg-u-hxy-is**

- dimensions
    - ImonAnt.ts: ['xant', 'yant', 'time']
    - ImonGre.ts: ['xgre', 'ygre', 'time']
    - LImon.tsIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.tsIs: 'Ice Sheet Surface Temperature'
    - ImonAnt.ts: 'Surface Temperature'

- description
    - LImon.tsIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonAnt.ts: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods'

- cell-measures
    - LImon.tsIs: 'area: areacella'
    - ImonAnt.ts: 'area: areacellg'

- model-realm
    - LImon.tsIs: 'landIce'
    - ImonAnt.ts: 'atmos'

- physical-parameter-name
    - LImon.tsIs: 'tsIs'
    - ImonAnt.ts: 'ts'

- variable-root
    - LImon.tsIs: 'tsis'
    - ImonAnt.ts: 'ts'


**ua_tavg-p39-hy-air**

- description
    - EdayZ.ua: 'zonal mean; hence YZT'
    - AERmonZ.ua: 'Zonal wind (positive in a eastward direction).'


**tsn_tavg-u-hxy-is**

- dimensions
    - ImonGre.tsn: ['xgre', 'ygre', 'time']
    - ImonAnt.tsn: ['xant', 'yant', 'time']
    - LImon.tsnIs: ['longitude', 'latitude', 'time']

- ui-label
    - LImon.tsnIs: 'Ice Sheet Snow Internal Temperature'
    - ImonGre.tsn: 'Snow Internal Temperature on Land Ice'

- description
    - LImon.tsnIs: 'quantity averaged over ice\\_sheet (meaning grounded ice sheet and floating ice shelf) only, to avoid contamination from other surfaces (eg: permafrost)'
    - ImonGre.tsn: 'quantity averaged over ice sheet (grounded ice sheet and floating ice shelf) only. Needed to analyse the impact of downscaling methods'

- cell-measures
    - LImon.tsnIs: 'area: areacella'
    - ImonGre.tsn: 'area: areacellg'

- cell-methods
    - LImon.tsnIs: 'area: time: mean where ice_sheet'
    - ImonGre.tsn: 'depth: mean area: time: mean where ice_sheet'

- physical-parameter-name
    - LImon.tsnIs: 'tsnIs'
    - ImonGre.tsn: 'tsn'

- variable-root
    - LImon.tsnIs: 'tsnis'
    - ImonGre.tsn: 'tsn'


**tsn_tavg-u-hxy-lnd**

- cell-methods
    - LImon.tsn: 'area: mean where land time: mean (weighted by snow mass on land)'
    - Eday.tsn: 'depth: mean area: mean where land time: mean (weighted by snow mass on land)'


**uas_tpt-h10m-hxy-u**

- description
    - 6hrPlevPt.uas: 'Near surface eastward wind'
    - 3hrPt.uas: 'This is sampled synoptically.'
    - E1hr.uas: 'Zonal wind (positive in a eastward direction) at 10 meters above the surface.'

- ui-label
    - E1hr.uas: 'Surface wind speed Eastward Components'
    - 6hrPlevPt.uas: 'Eastward Near-Surface Wind'


**vas_tavg-h10m-hxy-u**

- description
    - 6hrPlev.vas: 'Near surface northward wind'
    - day.vas: 'Northward component of the near surface wind'


**vas_tpt-h10m-hxy-u**

- description
    - 6hrPlevPt.vas: 'Near surface northward wind'
    - 3hrPt.vas: 'This is sampled synoptically.'
    - E1hr.vas: 'Meridional wind (positive in a northward direction) at 10 meters above the surface.'

- ui-label
    - E1hr.vas: 'Surface wind speed Northward Component'
    - 6hrPlevPt.vas: 'Northward Near-Surface Wind'


**utendepfd_tavg-p39-hy-air**

- description
    - EmonZ.utendepfd: 'Tendency of the zonal mean zonal wind due to the divergence of the Eliassen-Palm flux.'
    - EdayZ.utendepfd: 'Called "acceldivf" in CCMI table; we suggest new name. zonal mean; hence YZT'


**utendnogw_tavg-p19-hxy-air**

- ui-label
    - Emon.utendnogw: 'Eastward Acceleration Due to Non-Orographic Gravity Wave Drag'
    - Eday.utendnogw: 'Tendency of eastward wind due to non-orographic gravity waves'


**utendogw_tavg-p19-hxy-air**

- ui-label
    - Emon.utendogw: 'Eastward Acceleration Due to Orographic Gravity Wave Drag'
    - Eday.utendogw: 'Tendency of eastward wind due to orographic gravity waves'


**vtem_tavg-p39-hy-air**

- description
    - EdayZ.vtem: 'zonal mean; hence YZT'
    - EmonZ.vtem: 'Transformed Eulerian Mean Diagnostics v\\*, meridional component of the residual meridional circulation (v\\*, w\\*) derived from 6 hr or higher frequency data fields (use instantaneous daily fields or 12 hr fields if the 6 hr data are not available).'


**vtendnogw_tavg-p19-hxy-air**

- ui-label
    - Emon.vtendnogw: 'Northward Acceleration Due to Non-Orographic Gravity Wave Drag'
    - Eday.vtendnogw: 'Tendency of northward wind due to non-orographic gravity waves'


**vtendogw_tavg-p19-hxy-air**

- ui-label
    - Emon.vtendogw: 'Northward Acceleration Due to Orographic Gravity Wave Drag'
    - Eday.vtendogw: 'Tendency of northward wind due to orographic gravity waves'


**wetnh3_tavg-u-hxy-u**

- ui-label
    - AERmon.wetnh3: 'Wet Deposition Rate of NH3'
    - AERday.wetnh3: 'Daily Wet Deposition Rate of NH3'

- description
    - AERmon.wetnh3: 'Surface deposition rate of ammonia (NH3) due to wet processes'
    - AERday.wetnh3: 'Daily Wet Deposition Rate of NH3 at surface. Vertically integrated throughout the column to the surface.'


**wetnh4_tavg-u-hxy-u**

- ui-label
    - AERmon.wetnh4: 'Wet Deposition Rate of NH4'
    - AERday.wetnh4: 'Daily Wet Deposition Rate of NH4'

- description
    - AERmon.wetnh4: 'Surface deposition rate of ammonium (NH4) due to wet processes'
    - AERday.wetnh4: 'Daily Wet Deposition Rate of NH4 at surface. Vertically integrated throughout the column to the surface.'


**wetnoy_tavg-u-hxy-u**

- ui-label
    - AERmon.wetnoy: 'Wet Deposition Rate of NOy Including Aerosol Nitrate'
    - AERday.wetnoy: 'Daily Wet Deposition Rate of NOy'

- description
    - AERmon.wetnoy: 'NOy is the sum of all simulated oxidized nitrogen species, out of NO, NO2, HNO3, HNO4, NO3aerosol, NO3(radical), N2O5, PAN, other organic nitrates.'
    - AERday.wetnoy: 'Daily Wet Deposition Rate of NOy at surface. Vertically integrated throughout the column to the surface.'


**yvelbase_tavg-u-hxy-is**

- dimensions
    - IyrGre.yvelbase: ['xgre', 'ygre', 'time']
    - IyrAnt.yvelbase: ['xant', 'yant', 'time']


**wpp_tavg-u-hxy-sea**

- ui-label
    - Omon.wpp: 'Total Wave Peak Period'
    - 6hr.wpp: ' Total Wave Peak Period'


**yvelmean_tavg-u-hxy-is**

- dimensions
    - IyrGre.yvelmean: ['xgre', 'ygre', 'time']
    - IyrAnt.yvelmean: ['xant', 'yant', 'time']


**yvelsurf_tavg-u-hxy-is**

- dimensions
    - IyrAnt.yvelsurf: ['xant', 'yant', 'time']
    - IyrGre.yvelsurf: ['xgre', 'ygre', 'time']


**wsg_tmax-h10m-hxy-u**

- ui-label
    - Emon.wsgmax10m: 'Maximum Wind Speed of Gust at 10m'
    - E1hr.wsgmax10m: 'Maximum Speed of Wind Gust at 10m'

- description
    - Emon.wsgmax10m: 'Maximum Wind Speed of Gust at 10m, monthly'
    - E1hr.wsgmax10m: 'Wind speed gust maximum at 10m above surface'


**wsg_tmax-h100m-hxy-u**

- description
    - Emon.wsgmax100m: 'Maximum Wind Speed of Gust at 100m, monthly'
    - E1hr.wsgmax100m: 'Wind speed gust maximum at 100m above surface'


**wtem_tavg-p39-hy-air**

- description
    - EmonZ.wtem: 'Transformed Eulerian Mean Diagnostics w\\*, upward component of the residual meridional circulation (v\\*, w\\*) derived from 6 hr or higher frequency data fields (use instantaneous daily fields or 12 hr fields if the 6 hr data are not available). Scale height: 6950 m'
    - EdayZ.wtem: 'zonal mean; hence YZT'


**xvelbase_tavg-u-hxy-is**

- dimensions
    - IyrGre.xvelbase: ['xgre', 'ygre', 'time']
    - IyrAnt.xvelbase: ['xant', 'yant', 'time']


**xvelmean_tavg-u-hxy-is**

- dimensions
    - IyrGre.xvelmean: ['xgre', 'ygre', 'time']
    - IyrAnt.xvelmean: ['xant', 'yant', 'time']


**xvelsurf_tavg-u-hxy-is**

- dimensions
    - IyrGre.xvelsurf: ['xgre', 'ygre', 'time']
    - IyrAnt.xvelsurf: ['xant', 'yant', 'time']


**zostoga_tavg-u-hm-sea**

- ui-label
    - Omon.zostoga: 'Global Average Thermosteric Sea Level Change'
    - Oday.zostoga: 'global_average_thermosteric_sea_level_change'

- description
    - Omon.zostoga: 'There is no CMIP6 request for zosga nor zossga.'
    - Oday.zostoga: 'Global Average Thermosteric Sea Level Change'


**zvelbase_tavg-u-hxy-is**

- dimensions
    - IyrGre.zvelbase: ['xgre', 'ygre', 'time']
    - IyrAnt.zvelbase: ['xant', 'yant', 'time']


**zg_tavg-p39-hy-air**

- description
    - EdayZ.zg: 'zonal mean; hence YZT'
    - AERmonZ.zg: 'Geopotential is the sum of the specific gravitational potential energy relative to the geoid and the specific centripetal potential energy. Geopotential height is the geopotential divided by the standard acceleration due to gravity. It is numerically similar to the altitude (or geometric height) and not to the quantity with standard name height, which is relative to the surface.'


**zos_tavg-u-hxy-sea**

- ui-label
    - Oday.zos: 'Sea Surface Height above Geoid'
    - Omon.zos: 'Sea Surface Height Above Geoid'
    - Omon.zosSouth30: 'Sea Surface Height Above Geoid'

- description
    - Oday.zos: 'This is the dynamic sea level, so should have zero global area mean. zos is the effective sea level as if sea ice (and snow) at a grid cell were converted to liquid seawater (Campin et al., 2008). For OMIP, do _not _record inverse barometer responses from sea-ice (and snow) loading in zos. See (Griffies et al, 2016, https://doi.org/10.5194/gmd-9-3231-2016).'
    - Omon.zos: 'This is the dynamic sea level, so should have zero global area mean. It should not include inverse barometer depressions from sea ice.'
    - Omon.zosSouth30: 'This is the dynamic sea level, so should have zero global area mean. It should not include inverse barometer depressions from sea ice.'


**zvelsurf_tavg-u-hxy-is**

- dimensions
    - IyrGre.zvelsurf: ['xgre', 'ygre', 'time']
    - IyrAnt.zvelsurf: ['xant', 'yant', 'time']


**zmeso_tavg-ol-hxy-sea**

- description
    - Oday.zmeso: 'carbon concentration from mesozooplankton (20-200 um) component alone'
    - Omon.zmeso: 'carbon  concentration from mesozooplankton (20-200 um) component alone'


**zmicro_tavg-ol-hxy-sea**

- ui-label
    - Omon.zmicro: 'Mole Concentration of Microzooplankton Expressed as Carbon in Sea Water'
    - Oday.zmicro: 'Mole Concentration of microzooplankton Expressed as Carbon in Sea Water\n'

- description
    - Omon.zmicro: 'carbon  concentration from the microzooplankton (<20 um) component alone'
    - Oday.zmicro: 'carbon\xa0concentration from the microzooplankton (<20 um) component alone'


**expcob_tavg-u-hxy-sea**

- description
    - Oday.expcob: 'Downward sinking flux of particulate organic carbon at seafloor. Reported at the sea floor depth for present day relative to z=0 geoid. Reported as missing for land grid cells.'
    - Omon.expcob: 'Downward sinking flux of particulate organic carbon at seafloor'


**epfy_tavg-p39-hy-air**

- description
    - EdayZ.epfy: 'zonal mean; hence YZT'
    - EmonZ.epfy: 'Transformed Eulerian Mean Diagnostics Meridional component Fy of Eliassen-Palm (EP) flux (Fy, Fz) derived from 6hr or higher frequency fields (use daily fields or 12 hr fields if the 6 hr are not available). Please use the definitions given by equation 3.5.3a of Andrews, Holton and Leovy text book, but scaled by density to have units m3 s-2.'


**evspsblveg_tavg-u-hxy-u**

- ui-label
    - Eday.evspsblveg: 'Daily water evaporation flux from canopy'
    - 3hr.evspsblveg: 'Evaporation from canopy'

- description
    - Eday.evspsblveg: 'The same as the current variable evspsblveg but defined on daily timescales.'
    - 3hr.evspsblveg: 'Evaporation from canopy'


**evspsblpot_tavg-u-hxy-lnd**

- description
    - Emon.evspsblpot: 'at surface; potential flux of water into the atmosphere due to conversion of both liquid and solid phases to vapor (from underlying surface and vegetation)'
    - Eday.evspsblpot: 'water\\_potential\\_evapotranspiration\\_flux'


**evspsblsoi_tavg-u-hxy-u**

- ui-label
    - Eday.evspsblsoi: 'Daily water evaporation flux from soil'
    - 3hr.evspsblsoi: 'Water evaporation from soil'

- description
    - Eday.evspsblsoi: 'Water evaporation flux from soil but for daily averages i.e., the evspsblsoi variable, which is only currently defined for monthly averages'
    - 3hr.evspsblsoi: 'Water evaporation from soil'


**ficeberg_tavg-ol-hxy-sea**

- description
    - Omon.ficeberg: 'computed as the iceberg melt water  flux into the ocean divided by the area of the ocean portion of the grid cell.'
    - 3hr.ficeberg: 'Computed as the iceberg melt water flux into the ocean divided by the area of the ocean portion of the grid cell.'


**flandice_tavg-u-hxy-sea**

- description
    - Emon.flandice: 'Computed as the water flux into the ocean due to land ice (runoff water from surface and base of land ice or melt from base of ice shelf or vertical ice front) into the ocean divided by the area ocean portion of the grid cell'
    - 3hr.flandice: 'Computed as the water flux into the ocean due to land ice (runoff water from surface and base of land ice or melt from base of ice shelf or vertical ice front) into the ocean divided by the area ocean portion of the grid cell.'


**fracLut_tpt-u-hxy-u**

- description
    - Eyr.fracLut: 'End of year values (not annual mean); note that percentage should be reported as percentage of land grid cell (example: frac\\_lnd = 0.5, frac\\_ocn = 0.5, frac\\_crop\\_lnd = 0.2 (of land portion of grid cell), then frac\\_lut(crop) = 0.5\\*0.2 = 0.1)'
    - Emon.fracLut: 'End of month values (not monthly mean); note that percentage should be reported as percentage of land grid cell (example: frac\\_lnd = 0.5, frac\\_ocn = 0.5, frac\\_crop\\_lnd = 0.2 (of land portion of grid cell), then frac\\_lut(crop) = 0.5\\*0.2 = 0.1)'


**friver_tavg-u-hxy-sea**

- description
    - Omon.friver: 'computed as the river flux of water into the ocean divided by the area of the ocean portion of the grid cell.'
    - 3hr.friver: 'Computed as the river flux of water into the ocean divided by the area of the ocean portion of the grid cell.'


**hfdsn_tavg-u-hxy-lnd**

- description
    - LImon.hfdsn: 'the net downward heat flux from the atmosphere into the snow that lies on land divided by the land area in the grid cell; reported as missing for snow-free land regions or where the land fraction is 0.'
    - Eday.hfdsn: 'Downward heat flux at snow top'


**hfgeoubed_ti-u-hxy-gis**

- dimensions
    - IfxGre.hfgeoubed: ['xgre', 'ygre']
    - IfxAnt.hfgeoubed: ['xant', 'yant']


**hfds_tavg-u-hxy-sea**

- ui-label
    - 3hr.hfds: 'Downward Heat Flux at Sea Water Surface\n'
    - Omon.hfdsSouth30: 'Downward Heat Flux at Sea Water Surface'

- description
    - 3hr.hfds: "Net flux of heat entering the liquid water column through its upper surface (excluding any 'flux adjustment')."
    - Omon.hfdsSouth30: 'This is the net flux of heat entering the liquid water column through its upper surface (excluding any "flux adjustment") .'
