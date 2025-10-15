import hippo
import mrich
from mrich import print
from pathlib import Path
from os import environ
import shutil
import molparse as mp
import pandas as pd
import plotly.express as px

target_name = "XX01ZVNS2B"
target_dir = Path(environ["BULK"]) / "TARGETS" / target_name
cycle_name = "cycle_01"
cycle_dir = Path(cycle_name)
aligned_dir = target_dir / "aligned_files"

animal = hippo.HIPPO(target_name, target_dir / f"{target_name}.sqlite")

gen = hippo.RandomRecipeGenerator.from_json(animal.db, "cycle_01/rgen/xx01zvns2b_c1_scaffolds_rgen.json")

n = 350
for i in range(n):
    mrich.print(i+1, n)
    recipe = gen.generate(
        budget = 10_000,
        currency = "EUR",
    )
