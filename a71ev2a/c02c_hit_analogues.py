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

refdb = hippo.HIPPO("Enamine In-Stock", "/opt/xchem-fragalysis-2/maxwin/EnamineCatalogs/enamine_bb_hippo.sqlite")

hit_compounds = animal.poses(tag="hits").compounds

for threshold in [85,90,95]:

    similar = {}
    for i,hit in enumerate(hit_compounds):
        print(i, hit, len(similar))
        results = refdb.db.query_similarity(hit.smiles, threshold=threshold/100)
        if not results:
            continue
        similar[hit.id] = results

    for hit_id, analogues in similar.items():
        hit = animal.compounds[hit_id]
        values = animal.register_compounds(smiles=analogues.smiles)
        inchikeys = [i for i,s in values]
        analogues = animal.compounds[inchikeys] - hit
        analogues.add_tag(f"openbind_a71ev2a_c2_hit_analogues_{threshold}percent")
        analogues.add_tag(f"C{hit.id} {threshold}percent analogue")

animal.db.close()
refdb.db.close()

# sb.sh --job-name a71ev2a_c02c_hit_analogues --exclusive --no-requeue $HOME2/slurm/run_python.sh c02c_hit_analogues.py
