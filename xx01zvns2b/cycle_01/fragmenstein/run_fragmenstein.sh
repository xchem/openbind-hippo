#!/bin/bash

set -e

which fragmenstein

time fragmenstein laboratory combine -i ../cycle_??_hits.sdf -t *_apo-desolv.pdb --victor Wictor

cd ..

python to_bulkdock.py

# sb.sh --job-name "xx01zvns2b" $HOME2/slurm/run_bash_with_conda.sh run_fragmenstein.sh