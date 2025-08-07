[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/temporal-label/temporal-label)

<section id="description">

# Temporal Label  (vr)

## Description


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:temporal-label` |
| Pydantic class | [`temporal_label`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/temporal_label.py): TemporalLabel |
| | |
| JSON-LD | `vr:temporal-label` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/temporal-label](https://wcrp-cmip.github.io/Variable-Registry/temporal-label) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/temporal-label) |

</section>
<section id='links'>

## 🔗 Links and Dependencies

No context file found!!!</section> 


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

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/temporal-label/tavg.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Atemporal-label/tavg)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:temporal-label/tavg")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/temporal-label/_context_",
    "@type": "vr:temporal-label",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:temporal-label/tavg", frame)
```
</section>
