import hippo
import mrich
from mrich import print
from pathlib import Path
from os import environ
import shutil
import molparse as mp
import pandas as pd
import plotly.express as px

target_name = "A71EV2A"
target_dir = Path(environ["BULK"]) / "TARGETS" / target_name
cycle_name = "cycle_01"
cycle_dir = Path(cycle_name)
aligned_dir = target_dir / "aligned_files"

animal = hippo.HIPPO(target_name, target_dir / f"{target_name}.sqlite")

gen = hippo.RandomRecipeGenerator.from_json(animal.db, "cycle_01/rgen/a71ev2a_c1_elabs_rgen.json")

budget = 10_000
budget = 20_000

n = 100
for i in range(n):
    mrich.print(i+1, n)
    recipe = gen.generate(
        budget = budget,
        currency = "EUR",
        balance_clusters=True,
    )
    
    recipe = gen.generate(
        budget = budget,
        currency = "EUR",
        balance_clusters=False,
    )
