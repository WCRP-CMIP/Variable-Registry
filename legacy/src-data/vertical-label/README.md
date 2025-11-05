[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/vertical-label/vertical-label)

<section id="description">

# Vertical Label  (vr)

## Description


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:vertical-label` |
| Pydantic class | [`vertical_label`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/vertical_label.py): VerticalLabel |
| | |
| JSON-LD | `vr:vertical-label` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/vertical-label](https://wcrp-cmip.github.io/Variable-Registry/vertical-label) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/vertical-label) |

</section>

<section id="links">

## 🔗 Links and Dependencies

No external links or dependencies found.

</section>


<section id="schema">

## Content Schema

- **`id`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`regex`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`type`** (**str**) 
  _No description in pydantic model (see esgvoc)_


</section>   

<section id="usage">

## Usage

### Online Viewer 
#### Direct
To view a file in a browser use the content link with `.json` appended.

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/vertical-label/1000hPa.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Avertical-label/1000hPa)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:vertical-label/1000hPa")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/vertical-label/_context_",
    "@type": "vr:vertical-label",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:vertical-label/1000hPa", frame)
```
</section>
