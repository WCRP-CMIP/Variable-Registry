

<section id="description">

# Coordinate  (universal)



## Description
[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/coordinate/coordinate)

[View in HTML](https://wcrp-cmip.github.io/Variable-Registry/coordinate/coordinate)

</section>



<section id="info">


| Item | Reference |
| --- | --- |
| Type | `wrcp:coordinate` |
| Pydantic class | [`False`](https://github.com/ESGF/esgf-vocab/blob/main/src/esgvoc/api/data_descriptors/False.py):  Not yet implemented |
| | |
| JSON-LD | `vr:coordinate` |
| Expanded reference link | [https://wcrp-cmip.github.io/Variable-Registry/coordinate](https://wcrp-cmip.github.io/Variable-Registry/coordinate) |
| Developer Repo | [![Open in GitHub](https://img.shields.io/badge/Open-GitHub-blue?logo=github&style=flat-square)](https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/coordinate) |


</section>
    No external links found. 
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
To view a file in a browser use the content link with `.json` appended. 
eg. https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/coordinate/deltasigt.json

### Getting a File. 

A short example of how to integrate the computed ld file into your code. 

```python

import cmipld
cmipld.get( "vr:coordinate/deltasigt")

```

### Framing
Framing is a way we can filter the downloaded data to match what we want. 
```python
frame = {
            "@context": "https://wcrp-cmip.github.io/Variable-Registry/coordinate/_context_",
            "@type": "wcrp:coordinate",
            "keys we want": "",
            "@explicit": True

        }
        
import cmipld
cmipld.frame( "vr:coordinate/deltasigt" , frame)

```
</section>

    