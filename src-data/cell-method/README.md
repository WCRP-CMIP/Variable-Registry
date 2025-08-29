[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/cell-method/cell-method)

<section id="description">

# Cell Method  (vr)

## Description

Cell methods define how climate variables are processed across spatial and temporal dimensions. These specify operations like time averaging, spatial means, maximum/minimum calculations, and other statistical operations applied to grid cells or time intervals in climate model output.

[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/cell-method/cell-method)

</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:cell-method` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:cell-method` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/cell-method](https://wcrp-cmip.github.io/Variable-Registry/cell-method) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/cell-method) |

</section>

<section id="links">

## 🔗 Links and Dependencies

No external links or dependencies found.

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
- **`mask`**  
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

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/cell-method/adm-tm.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Acell-method/adm-tm)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:cell-method/adm-tm")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/cell-method/_context_",
    "@type": "vr:cell-method",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:cell-method/adm-tm", frame)
```
</section>
