#!/bin/bash

set -e

TARGET=$1

if [[ -z $TARGET ]]; then
	echo must pass target name
	exit 1
fi

if [[ -z $KNIT ]]; then
	echo '$KNIT' variable not set
	exit 2
fi

ls $KNIT/Knitwork/runKnitting.py

python $KNIT/Knitwork/runKnitting.py \
	--substructure_pair_file fragment_output/substructure_pairs.json \
	--descriptor prop_pharmfp \
	--working_dir knitwork_temp \
	--output_dir knitwork_impure_output \
	--run_parallel \
	--n_parallel 10 \
	--limit 50 \
	--prolif_prioritization \
	--max_prioritize 100 \
	--target $TARGET \
	--substructure_dir fragment_output \
	-fd $TARGET
