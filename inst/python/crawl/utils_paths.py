import os

FILE_DIR, _ = os.path.split(os.path.abspath(__file__))
EXTDATA_DIR = os.path.join(FILE_DIR, "../../extdata")
BASE_DIR = os.path.join(EXTDATA_DIR, "collection")
MPIS_DIR = os.path.join(BASE_DIR, "mpis")
SCRAPE_DIR = os.path.join(MPIS_DIR, "scrape")
MAP_DIR = os.path.join(MPIS_DIR, "map")
MAPPED_DIR = os.path.join(MPIS_DIR, "mapped")
PURE_DIR = os.path.join(BASE_DIR, "pure")
OUS_DIR = os.path.join(PURE_DIR, "ous")
CTX_DIR = os.path.join(PURE_DIR, "ctx")
LOG_DIR = os.path.join(BASE_DIR, "log")
