[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/area-label/area-label)

<section id="description">

# Area Label  (vr)

## Description

Area labels define surface area types and spatial domains for climate variables. These labels specify whether a variable applies to land surfaces, ocean areas, sea ice, or other surface types, enabling proper spatial categorization and filtering of climate data.


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:area-label` |
| Pydantic class | [`area_label`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/area_label.py): AreaLabel |
| | |
| JSON-LD | `vr:area-label` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/area-label](https://wcrp-cmip.github.io/Variable-Registry/area-label) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/area-label) |

</section>

<section id="links">

## 🔗 Links and Dependencies

No external links or dependencies found.

</section>


<section id="schema">

## Content Schema

- **`id`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`description`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`drs_name`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`label`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`type`** (**str**) 
  _No description in pydantic model (see esgvoc)_


</section>   

<section id="usage">

## Usage

### Online Viewer 
#### Direct
To view a file in a browser use the content link with `.json` appended.

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/area-label/air.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Aarea-label/air)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:area-label/air")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/area-label/_context_",
    "@type": "vr:area-label",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:area-label/air", frame)
```
</section>
