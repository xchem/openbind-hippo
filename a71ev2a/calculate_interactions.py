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

# pose_pool = animal.poses.get_by_metadata_substring_match("GNINA pK")

pose_pool = animal.poses

print(pose_pool)

for i,pose in enumerate(pose_pool):
    mrich.print(i, pose)
    try:
        pose.calculate_interactions()
    except Exception as e:
        mrich.error(pose, e)

# sb.sh --job-name 'd68ev3c_interactions' /opt/xchem-fragalysis-2/maxwin/slurm/run_python.sh -m hippo calculate-interactions $BULK/TARGETS/A71EV2A/A71EV2A.sqlite