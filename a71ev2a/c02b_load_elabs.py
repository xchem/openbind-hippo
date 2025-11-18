from pathlib import Path
import hippo
import mrich
from os import environ

mrich.var("hippo", hippo.__file__)

target_name = "A71EV2A"
target_dir = Path(environ["BULK"]) / "TARGETS" / target_name
cycle_name = "cycle_02"
cycle_dir = Path(cycle_name)
aligned_dir = target_dir / "aligned_files"

animal = hippo.HIPPO(target_name, target_dir / f"{target_name}.sqlite")
animal.db.backup()

output_root = cycle_dir / "syndirella/elabs/"

files = list(output_root.glob("*/*-*-?/*to_hippo*"))

product_tags = ["syndirella_product", "openbind_a71ev2a_c2_elabs"]
pose_tags = ["syndirella_product", "syndirella_placed", "openbind_a71ev2a_c2_elabs"]

for i,file in enumerate(files):

    mrich.h2(f"{i+1}/{len(files)}")

    try:
        pose_name = file.parent.parent.name.split("_")[-1]
        scaffold = animal.poses[pose_name].compound
    
        animal.add_syndirella_elabs(file, scaffold_compound=scaffold, product_tags=product_tags, pose_tags=pose_tags)
        
    except Exception as e:
        mrich.error(file)
        mrich.error(e)
        # break
        continue

    # break
    
animal.db.close()

# sb.sh --job-name a71ev2a_c02b_load_elabs --exclusive --no-requeue $HOME2/slurm/run_python.sh c02b_load_elabs.py
