#!/bin/bash

set -e

if [[ -z $KNIT ]]; then
	echo '$KNIT' variable not set
	exit 1
fi

ls $KNIT/Fragment/runEnumeration.py

python $KNIT/Fragment/runEnumeration.py \
	-i *_input.csv \
	-o fragment_output \
	--record_equiv_synthon \
	--r_group_expansions
