from pathlib import Path
import hippo
import mrich
from os import environ

mrich.var("hippo", hippo.__file__)

target_name = "XX01ZVNS2B"
target_dir = Path(environ["BULK"]) / "TARGETS" / target_name
cycle_name = "cycle_01"
cycle_dir = Path(cycle_name)
aligned_dir = target_dir / "aligned_files"

animal = hippo.HIPPO(target_name, target_dir / f"{target_name}.sqlite")
animal.db.backup()

output_root = cycle_dir / "syndirella/elabs/"

files = list(output_root.glob("*/*-*-?/*to_hippo*"))

for i,file in enumerate(files):

    mrich.h2(f"{i+1}/{len(files)}")
    
    try:
    
        scaffold_id = int(file.parent.parent.name.split("_C")[-1])
        routes = hippo.RouteSet.from_product_ids(animal.db, [scaffold_id])
        assert len(routes) == 1, "Wrong number of routes"

        route = routes.pop()
    
        animal.add_syndirella_elabs(file, scaffold_route=route)
        
    except Exception as e:
        mrich.error(file)
        mrich.error(e)
        continue
    
animal.db.close()

# sb.sh --job-name zika_load_elabs --exclusive --no-requeue $HOME2/slurm/run_python.sh c01g_load_elabs.py
