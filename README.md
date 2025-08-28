# openbind-hippo
HIPPO notebooks driving the algorithmics for OpenBind phase 0

<img width="360" height="100" alt="OpenBind_Wordmark Dark" src="https://github.com/user-attachments/assets/0f23b643-4167-4373-afc1-ae70489a32f1" />
<img width="262" height="150" alt="HIPPO" src="https://github.com/user-attachments/assets/8144af7a-7e28-4116-9877-395ef76dd5db" />

## Instructions

This repository documents the phase 0 fragment merging, compound ordering, elaboration and downsampling done with HIPPO.
The procedure roughly follows the [FFF_Template](https://github.com/xchem/FFF_Template/blob/main/README.md)

Make sure to do the pre-requisites of the FFF_Template

### Starting on a new target/cycle

Use the notebook `notebooks/setup_cycle.ipynb` to set up for a new target and/or cycle

## Merge stats

|     Cycle     | Hits | Fragmenstein | Knitwork Pure | Knitwork Impure | Acceptable Placements | Exported Scaffolds |
|---------------|------|--------------|---------------|-----------------|-----|----|
| `xx01zvns2b-01` |  `337` | `98k->25k->2825` (14h) | `140k->15k->411` | `150k->12k->378` | `50k` | `3614` |
| `a71ev2a-01`    |  `645` | `306k` (3.5d) | `1.6M` | `1.9M` (11h) |                     | |
| `d68ev3c-01`    |  `202` | `6356->1665->153` (8h) | `268k->19k->83` | `285k->12k->109` (14h) | `31k` | `345` |

## Pocket stats

### d68ev3c

3 major clusters?

<img width="500" height="400" alt="Screenshot 2025-08-28 at 16 17 57" src="https://github.com/user-attachments/assets/494e52a4-d64e-4f8d-87bf-b740999d0891" />
