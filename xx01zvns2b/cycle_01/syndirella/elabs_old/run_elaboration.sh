#!/bin/bash

set -e

KEY=$1

echo $MANIFOLD_API_KEY

echo --input $(pwd)/$KEY"_syndirella_input.csv"
echo --hits_path $(pwd)/"c01_elabs_syndirella_inspiration_hits.sdf"
echo --output $(pwd)/$KEY
echo --metadata "/opt/xchem-fragalysis-2/maxwin/BulkDock/TARGETS/A71EV2A/metadata.csv"
echo --templates "$(pwd)/templates"
echo --db_search_tool hippo
echo --reference_db "/opt/xchem-fragalysis-2/maxwin/EnamineCatalogs/enamine_bb_hippo.sqlite"

/opt/xchem-fragalysis-2/maxwin/conda/bin/syndirella run \
	--input $(pwd)/$KEY"_syndirella_input.csv" \
	--hits_path $(pwd)/"c01_elabs_syndirella_inspiration_hits.sdf" \
	--output $(pwd)/$KEY \
	--metadata "/opt/xchem-fragalysis-2/maxwin/BulkDock/TARGETS/A71EV2A/metadata.csv" \
	--templates "$(pwd)/templates" \
    --db_search_tool hippo \
    --reference_db "/opt/xchem-fragalysis-2/maxwin/EnamineCatalogs/enamine_bb_hippo.sqlite" \
	--no_scaffold_place \
    --use_sdf_names \
    --manual
    
# sb.sh --job-name syndirella $HOME2/slurm/run_bash_with_conda.sh ./run_elaboration.sh

