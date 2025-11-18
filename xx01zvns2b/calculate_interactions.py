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

pose_pool = animal.poses.get_by_metadata_substring_match("GNINA pK")

for i,pose in enumerate(pose_pool):
    mrich.print(i, pose)
    try:
        pose.calculate_interactions()
    except Exception as e:
        mrich.error(pose, e)
