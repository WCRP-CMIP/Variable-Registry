[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/variable/variable)

<section id="description">

# Variable  (vr)

## Description


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:variable` |
| Pydantic class | [`variable`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/variable.py): Variable |
| | |
| JSON-LD | `vr:variable` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/variable](https://wcrp-cmip.github.io/Variable-Registry/variable) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/variable) |

</section>
<section id="links">

## 🔗 Links and Dependencies


### Contexts of External Mappings

- **`Variable-root`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/variable-root/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/variable-root/_context_)
  - Source: `Variable-Registry/variable-root/_context_`

- **`cell-methods`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/cell-method/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/cell-method/_context_)
  - Source: `Variable-Registry/cell-method/_context_`

- **`temporal-label`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/temporal-label/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/temporal-label/_context_)
  - Source: `Variable-Registry/temporal-label/_context_`

- **`vertical-label`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/vertical-label/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/vertical-label/_context_)
  - Source: `Variable-Registry/vertical-label/_context_`

- **`horizontal-label`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/horizontal-label/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/horizontal-label/_context_)
  - Source: `Variable-Registry/horizontal-label/_context_`

- **`area-label`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/area-label/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/area-label/_context_)
  - Source: `Variable-Registry/area-label/_context_`

- **`dimensions`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/Variable-Registry/area-label/\_context\_](https://wcrp-cmip.github.io/Variable-Registry/area-label/_context_)
  - Source: `Variable-Registry/area-label/_context_`

- **`model-realm`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/WCRP-universe/realm/\_context\_](https://wcrp-cmip.github.io/WCRP-universe/realm/_context_)
  - Source: `WCRP-universe/realm/_context_`


</section>

<section id="schema">

## Content Schema

- **`id`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`drs_name`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`long_name`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`standard_name`** (**str | None**) 
  _No description in pydantic model (see esgvoc)_
- **`units`** (**str | None**) 
  _No description in pydantic model (see esgvoc)_
- **`validation_method`** (**str**) 
  _No description in pydantic model (see esgvoc)_
- **`type`** (**str**) 
  _No description in pydantic model (see esgvoc)_


</section>   

<section id="usage">

## Usage

### Online Viewer 
#### Direct
To view a file in a browser use the content link with `.json` appended.

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/variable/abs550aer_tavg-u-hxy-u.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Avariable/abs550aer_tavg-u-hxy-u)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:variable/abs550aer_tavg-u-hxy-u")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/variable/_context_",
    "@type": "vr:variable",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:variable/abs550aer_tavg-u-hxy-u", frame)
```
</section>
