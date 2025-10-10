#!/bin/bash

set -e

KEY=$1

echo "SYNDIRELLA"
echo "input        "$(pwd)/$KEY"_syndirella_input.csv"
echo "hits_path    "$(pwd)/"a71ev2a_c01_elabs_syndirella_inspiration_hits.sdf"
echo "output       "$(pwd)/$KEY
echo "templates    ""$(pwd)/templates"
echo "reference_db ""/opt/xchem-fragalysis-2/maxwin/EnamineCatalogs/enamine_bb_hippo.sqlite"
echo

/opt/xchem-fragalysis-2/maxwin/conda/bin/syndirella run \
	--input $(pwd)/$KEY"_syndirella_input.csv" \
	--hits_path $(pwd)/"a71ev2a_c01_elabs_syndirella_inspiration_hits.sdf" \
	--output $(pwd)/$KEY \
	--templates "$(pwd)/templates" \
    --scaffold_place_num 20 \
    --db_search_tool hippo \
    --reference_db "/opt/xchem-fragalysis-2/maxwin/EnamineCatalogs/enamine_bb_hippo.sqlite" \
    --manual \
	--no_scaffold_place
#    --no_assert_scaffold_intra_geom_flatness
    
# sb.sh --job-name syndirella $HOME2/slurm/run_bash_with_conda.sh ./run_elaboration.sh

