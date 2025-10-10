#!/bin/bash
set -e

which sb.sh
echo $(ls -l "c01_elabs_C"*"_syndirella_input.csv" | wc -l)

# for KEY in "c01_elabs_C"*"_syndirella_input.csv"; do
# 	KEY=${KEY:0:-21}
#     echo $KEY
#     echo sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=3GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
#     sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=3GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
#     # sleep 5m
# done

KEY="c01_elabs_C55308"

echo sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=8GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=8GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
