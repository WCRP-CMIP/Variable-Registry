[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/data-request/data-request)

<section id="description">

# Data Request  (vr)

## Description


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:data-request` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:data-request` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/data-request](https://wcrp-cmip.github.io/Variable-Registry/data-request) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/data-request) |

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

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/data-request/v1.2.2.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Adata-request/v1.2.2)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:data-request/v1.2.2")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/data-request/_context_",
    "@type": "vr:data-request",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:data-request/v1.2.2", frame)
```
</section>
