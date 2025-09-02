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

## Merge (compound) stats

Legend: `CSV rows` `unique smiles` `compounds with placements` `exported scaffolds`

|     Cycle     | Hits | Fragmenstein | Knitwork Pure | Knitwork Impure | Acceptable Placements | Exported Scaffolds | Retro OK (Manifold) | Selected Chemistry
|---------------|------|--------------|---------------|-----------------|-----|----|---|---|
| `xx01zvns2b-01` |  `337` | `98k` `73k` `25k` `2825` (14h) | `140k` `34k` `15k` `411` | `150k` `27k` `12k` `378` | `50k` | `3614` | | |
| `a71ev2a-01`    |  `645` | `306k` `168k` `61k` `309` (3.5d) | `1.6M` `89k` `30k` `396` | `1.9M` `63k` `22k` `813` (11h) | `114k` | `1518` | `1213` | |
| `d68ev3c-01`    |  `228` | `6356` `4829` `1665` `153` (8h) | `269k` `58k` `19k` `83` | `286k` `44k` `12k` `109` (14h) | `31k` | `345` | `200` | |

## Pocket stats

### d68ev3c

```
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ subsite            ┃ num_poses ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 2 - 7gon/B/201/1   │ 176       │
│ 1 - 7gp9/A/201/1   │ 111       │
│ 4 - 7gp7/A/201/1   │ 61        │
│ 5 - B1120/A/308/1  │ 42        │
│ 3 - 7gpw/B/202/1   │ 17        │
│ 11 - B0517/A/209/1 │ 14        │
│ 10 - 7gq5/A/201/1  │ 8         │
│ 30 - 7gqr/B/201/1  │ 8         │
│ 14 - 7go6/A/201/1  │ 5         │
│ 15 - 7gob/B/201/1  │ 2         │
│ 17 - 7gok/A/201/1  │ 1         │
│ 24 - 7gpz/B/201/1  │ 1         │
│ 25 - 7gq1/A/201/1  │ 1         │
│ 28 - 7gqn/A/201/1  │ 1         │
│ 29 - 7gqn/A/202/1  │ 1         │
└────────────────────┴───────────┘
```

<img width="596" height="568" alt="Screenshot 2025-08-28 at 16 21 46" src="https://github.com/user-attachments/assets/3e822e57-90cb-43f8-a8b3-dedfc7226b4f" />

### a71ev2a

```
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ subsite            ┃ num_poses ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1 - Active Site    │ 1431      │
│ 6 - A0486/A/147/1  │ 79        │
│ 5 - A3181/A/202/1  │ 73        │
│ 3 - A0541/A/147/1  │ 62        │
│ 2 - A3977/A/202/1  │ 44        │
│ 17 - A1081/A/201/1 │ 30        │
│ 4 - A0525/A/246/1  │ 16        │
└────────────────────┴───────────┘
```

### xx01zvns2b

```
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ subsite           ┃ num_poses ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1 - Z4590/B/203/1 │ 3614      │
│ 6 - Z0788/B/302/1 │ 24        │
│ 5 - Z0773/B/401/1 │ 13        │
│ 7 - Z0846/B/301/1 │ 9         │
└───────────────────┴───────────┘
```
<img width="904" height="999" alt="Screenshot 2025-08-28 at 16 23 18" src="https://github.com/user-attachments/assets/b503fc6c-840f-4e55-bb03-9524da2dcffc" />
