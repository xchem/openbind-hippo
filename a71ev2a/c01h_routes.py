from pathlib import Path
import hippo
import mrich
from os import environ

mrich.var("hippo", hippo.__file__)

target_name = "A71EV2A"
target_dir = Path(environ["BULK"]) / "TARGETS" / target_name
cycle_name = "cycle_01"
cycle_dir = Path(cycle_name)
aligned_dir = target_dir / "aligned_files"

animal = hippo.HIPPO(target_name, target_dir / f"{target_name}.sqlite")
animal.db.backup()

scaffolds = animal.compounds(tag="openbind_a71ev2a_c1_scaffolds_chemok_bbok")
elabs = scaffolds.elabs
products = scaffolds + elabs

mrich.var("products", products)

for i, c in mrich.track(enumerate(products), total=len(products)):

    try:
        reactions = c.reactions
    except Exception as e:
        mrich.error(f"Error getting {c}'s reactions", e)
        continue

    for reaction in reactions:

        try:
            recipes = reaction.get_recipes(supplier="Enamine")
        except Exception as e:
            mrich.error(f"Error getting {reaction}'s ({c}) recipes", e)
            continue

        for recipe in recipes:

            route = animal.register_route(recipe=recipe)

            mrich.print(f"registered {route=}")

    if i % 100 == 99:
        mrich.success("Committing...")
        animal.db.commit()

animal.db.prune_duplicate_routes()

animal.db.close()

# sb.sh --job-name 2a_routes --exclusive $HOME2/slurm/run_python.sh c01h_routes.py
