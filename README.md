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
| `a71ev2a-01`    |  `645` | `306k->61k->309` (3.5d) | `1.6M->30k->396` | `1.9M->22k->813` (11h) | `114k` | `1518` |
| `d68ev3c-01`    |  `202` | `6356->1665->153` (8h) | `268k->19k->83` | `285k->12k->109` (14h) | `31k` | `345` |

## Pocket stats

### d68ev3c

5 pockets?
<img width="596" height="568" alt="Screenshot 2025-08-28 at 16 21 46" src="https://github.com/user-attachments/assets/3e822e57-90cb-43f8-a8b3-dedfc7226b4f" />

### a71ev2a



### xx01zvns2b

3 pockets?
<img width="904" height="999" alt="Screenshot 2025-08-28 at 16 23 18" src="https://github.com/user-attachments/assets/b503fc6c-840f-4e55-bb03-9524da2dcffc" />
