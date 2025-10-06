#!/bin/bash
set -e

which sb.sh
echo $(ls -l "c01_elabs_C"*"_syndirella_input.csv" | wc -l)

REQUEUE="c01_elabs_C1047 c01_elabs_C10728 c01_elabs_C108379 c01_elabs_C108383 c01_elabs_C109063 c01_elabs_C108828 c01_elabs_C11169 c01_elabs_C11345 c01_elabs_C114282 c01_elabs_C119143 c01_elabs_C120359 c01_elabs_C120734 c01_elabs_C120894 c01_elabs_C13732 c01_elabs_C14716 c01_elabs_C15670 c01_elabs_C2607 c01_elabs_C3291 c01_elabs_C58201 c01_elabs_C58690 c01_elabs_C60764 c01_elabs_C61266 c01_elabs_C61575 c01_elabs_C61598 c01_elabs_C62126 c01_elabs_C62466 c01_elabs_C63872 c01_elabs_C65268 c01_elabs_C74983 c01_elabs_C9828 c01_elabs_C61503 c01_elabs_C64652 c01_elabs_C118804"

for KEY in "c01_elabs_C"*"_syndirella_input.csv"; do
	# KEY=${KEY:0:-21}
    echo $KEY
    echo sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=8GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
    sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=8GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
    # sleep 5m
done
