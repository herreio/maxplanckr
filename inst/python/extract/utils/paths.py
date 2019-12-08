import os

FILE_DIR, _ = os.path.split(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(FILE_DIR, '../../../..')
EXTDATA_DIR = os.path.join(PROJECT_DIR, 'inst/extdata')


BASE_DIR = os.path.join(EXTDATA_DIR, 'collection')

MPIS_DIR = os.path.join(BASE_DIR, 'mpis')
SCRAPE_DIR = os.path.join(MPIS_DIR, 'scrape')
MAP_DIR = os.path.join(MPIS_DIR, 'map')
MAPPED_DIR = os.path.join(MPIS_DIR, 'mapped')

PURE_DIR = os.path.join(BASE_DIR, 'pure')
CTX_DIR = os.path.join(PURE_DIR, 'ctx')
ITEMS_DIR = os.path.join(PURE_DIR, 'item')
LANG_DIR = os.path.join(PURE_DIR, 'lang')
OUS_DIR = os.path.join(PURE_DIR, 'ous')
PERS_DIR = os.path.join(PURE_DIR, 'pers')

DATA_DIR = os.path.join(EXTDATA_DIR, 'prepared')

LOG_DIR = os.path.join(DATA_DIR, 'log')
STATS_DIR = os.path.join(DATA_DIR, 'count')
TITLES_DIR = os.path.join(DATA_DIR, 'titles')
GRAPH_DIR = os.path.join(DATA_DIR, 'graph')
TABLES_DIR = os.path.join(DATA_DIR, 'tables')
