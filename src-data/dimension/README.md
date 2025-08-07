[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/dimension/dimension)

<section id="description">

# Dimension  (vr)

## Description

Dimensions define the axes and coordinate systems used to organize climate data arrays. These specify spatial dimensions (longitude, latitude, vertical levels), temporal dimensions (time), and other axes that structure how climate variables are stored and accessed.

[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/dimension/dimension)

</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:dimension` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:dimension` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/dimension](https://wcrp-cmip.github.io/Variable-Registry/dimension) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/dimension) |

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
- **`spatial-shape`**  
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

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/dimension/alevel.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Adimension/alevel)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:dimension/alevel")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/dimension/_context_",
    "@type": "vr:dimension",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:dimension/alevel", frame)
```
</section>
