[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/coordinate/coordinate)

<section id="description">

# Coordinate  (vr)

## Description

Coordinates define reference systems and specific coordinate values used in climate data. These include pressure levels, height coordinates, depth levels, and other spatial reference points that specify where in the Earth system variables are measured or computed.

[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/coordinate/coordinate)

</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:coordinate` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:coordinate` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/coordinate](https://wcrp-cmip.github.io/Variable-Registry/coordinate) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/coordinate) |

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
- **`axis-flag`**  
   [**unknown**]
  No Pydantic model found.
- **`cf-standard-name`**  
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

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/coordinate/deltasigt.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Acoordinate/deltasigt)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:coordinate/deltasigt")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/coordinate/_context_",
    "@type": "vr:coordinate",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:coordinate/deltasigt", frame)
```
</section>
