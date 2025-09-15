[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/cmip6-mip-table/cmip6-mip-table)

<section id="description">

# Cmip6 Mip Table  (vr)

## Description

CMIP6 MIP tables provide mappings between CMIP7 variable definitions and legacy CMIP6 Model Intercomparison Project tables. These maintain backward compatibility and facilitate data transition from CMIP6 to CMIP7 experimental frameworks.


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:cmip6-mip-table` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:cmip6-mip-table` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/cmip6-mip-table](https://wcrp-cmip.github.io/Variable-Registry/cmip6-mip-table) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/cmip6-mip-table) |

</section>
<section id="links">

## 🔗 Links and Dependencies


### Contexts of External Mappings

- **`variables`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/variable/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/variable/_context_)
  - Source: `Variable-Registry/variable/_context_`


</section>

<section id="schema">

## Content Schema

- **`id`**  
   [**unknown**]
  No Pydantic model found.
- **`validation-key`**  
   [**unknown**]
  No Pydantic model found.
- **`ui-label`**  
   [**unknown**]
  No Pydantic model found.
- **`description`**  
   [**unknown**]
  No Pydantic model found.
- **`variables`**  
   [**unknown**]
  No Pydantic model found.
- **`@context`**  
   [**unknown**]
  No Pydantic model found.
- **`type`**  
   [**unknown**]
  No Pydantic model found.


</section>   

<section id="usage">

## Usage

### Online Viewer 
#### Direct
To view a file in a browser use the content link with `.json` appended.

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/cmip6-mip-table/3hr.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Acmip6-mip-table/3hr)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:cmip6-mip-table/3hr")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/cmip6-mip-table/_context_",
    "@type": "vr:cmip6-mip-table",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:cmip6-mip-table/3hr", frame)
```
</section>
