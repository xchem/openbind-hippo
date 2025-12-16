
import mrich
from mrich import print

import hippo
from os import environ
from pathlib import Path

# connect to postgres

animal = hippo.HIPPO(
    "postgres", 
    dict(
        username=environ["HIPPO_POSTGRES_USERNAME"],
        password=environ["HIPPO_POSTGRES_PASSWORD"],
        port=5555,
        host="localhost",
        dbname="postgres",
        create_indexes=False,
    )
)

# define targets to migrate

TARGETS = [
    # "A71EV2A",
    # "D68EV3C",
    # "XX01ZVNS2B",
    # "A71EV2AZ", # pose_alias_from_metadata_field="observation_longname"
    # "ZIKA_NS3_helicase", # pose_alias_from_metadata_field="observation_longname"
    # "Flavi_NS5_RdRp",
    # "../../CHIKV_FFF/hippo_prod/CHIKV_prod10c.sqlite", # interactions=False, features=False,
    
    # "CpKRS", # FAILED w/ pose_alias_from_metadata_field="observation_longname"
]

for target in TARGETS:

    mrich.h1(target)

    if target.endswith(".sqlite"):
        path = Path(target)
    else:
        path = Path(environ["BULK"]) / "TARGETS" / target / f"{target}.sqlite"

    mrich.var("path", path)
    
    assert path.exists()

    source = hippo.HIPPO(path.name.removesuffix(".sqlite"), path)

    backup_path = source.db.backup()

    source.db.close()

    mrich.var(backup_path.name.removesuffix(".sqlite"), backup_path)
    
    animal.db.migrate_sqlite(backup_path) #, interactions=False, features=False) #, pose_alias_from_metadata_field="observation_longname")

    animal.db.commit()
    mrich.success("Committed")
