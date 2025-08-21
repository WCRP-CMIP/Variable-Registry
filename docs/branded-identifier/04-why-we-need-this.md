# Why We Need Branded Identifiers



<KT to fill in content here>



---

## The Problem: Model Intercomparison Chaos

Imagine comparing climate models without standards:

| Model | Temperature Variable | What It Actually Means |
|-------|---------------------|------------------------|
| Model A | `T2M` | 2-meter air temperature |
| Model B | `TEMP_SFC` | Surface temperature |
| Model C | `tas` | Near-surface temperature (but which height?) |
| Model D | `T_air_sfc` | Air temperature at surface |

**Result**: Cannot compare models directly!

With branded identifiers:

| Model | Branded Identifier | Everyone Knows It Means |
|-------|-------------------|-------------------------|
| Model A | `tas_tavg-h2m-hxy-u` | 2m air temp, time-averaged |
| Model B | `tas_tavg-h2m-hxy-u` | 2m air temp, time-averaged |
| Model C | `tas_tavg-h2m-hxy-u` | 2m air temp, time-averaged |
| Model D | `tas_tavg-h2m-hxy-u` | 2m air temp, time-averaged |



---
