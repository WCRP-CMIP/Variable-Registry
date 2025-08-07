[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/variable-root/variable-root)

<section id="description">

# Variable Root  (vr)

## Description


</section>

<section id="info">

| Item | Reference |
| --- | --- |
| Type | `vr:variable-root` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:variable-root` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/variable-root](https://wcrp-cmip.github.io/Variable-Registry/variable-root) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/variable-root) |

</section>
<section id="links">

## 🔗 Links and Dependencies


### External Dependencies
**variable-root** depends on **1 external vocabularies**  

The following external vocabularies are required to fully describe the data:


- `standard-name → cf:standard-name` [link](https://wcrp-cmip.github.io/CF/standard-name/)


### Contexts of External Mappings

- **`standard-name`** → `@type: @id`
  - Context: [https://wcrp-cmip.github.io/CF/standard-name/\_context\_](https://wcrp-cmip.github.io/CF/standard-name/_context_)
  - Source: `CF/standard-name/_context_`


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
- **`data-type`**  
   [**unknown**]
  No Pydantic model found.
- **`standard-name`**  
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

For example: `https://github.com/wcrp-cmip/Variable-Registry//tree/main/src-data/variable-root/abs550aer.json`

#### Use cmipld.js [in development]
[View self resolving files here](https://wcrp-cmip.github.io/CMIPLD/viewer/index.html?uri=vr%253Avariable-root/abs550aer)

### Getting a File

A short example of how to integrate the computed ld file into your code. 

```python
import cmipld
cmipld.get("vr:variable-root/abs550aer")
```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
    "@context": "https://wcrp-cmip.github.io/Variable-Registry/variable-root/_context_",
    "@type": "vr:variable-root",
    "keys we want": "",
    "@explicit": True
}
        
import cmipld
cmipld.frame("vr:variable-root/abs550aer", frame)
```
</section>
