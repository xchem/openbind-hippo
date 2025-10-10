#!/bin/bash
set -e
shopt -s nullglob

which sb.sh
echo $(ls -l *"c01_elabs_C"*"_syndirella_input.csv" | wc -l)

for KEY in *_c??_elabs_C*.csv; do

	KEY=${KEY:0:-21}
	echo $KEY

	files=($KEY/*/*_to_hippo.pkl.gz)
	if (( ${#files[@]} )); then
		echo "Output exists"
	else
		echo sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=8GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
		sb.sh --job-name $KEY --ntasks=1 --cpus-per-task=1 --mem=8GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY >> sbatch.log
	fi
done
