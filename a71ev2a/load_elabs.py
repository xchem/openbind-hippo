
import hippo
import mrich
from mrich import print
from pathlib import Path
from os import environ

target_name = "A71EV2A"
target_dir = Path(environ["BULK"]) / "TARGETS" / target_name
cycle_name = "cycle_01"
cycle_dir = Path(cycle_name)
aligned_dir = target_dir / "aligned_files"

animal = hippo.HIPPO(target_name, target_dir / f"{target_name}.sqlite")
animal.db.backup()

files = list(output_root.glob("*/*-*-?/*to_hippo*"))

for i,file in enumerate(files):
    mrich.h2(f"{i+1}/{len(files)}")
    try:
        animal.add_syndirella_elabs(file)
    except Exception as e:
        mrich.error(file)
        mrich.error(e)
        continue

animal.db.close()

# sb.sh --job-name RDRP_load_elabs --exclusive --no-requeue $HOME2/slurm/run_python.sh 4_load_elabs.py