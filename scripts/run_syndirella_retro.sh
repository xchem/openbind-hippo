#!/bin/bash

mkdir -p retrosynthesis

/opt/xchem-fragalysis-2/maxwin/conda/bin/syndirella run --input *_syndirella_input.csv --output retrosynthesis --just_retro
