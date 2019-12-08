import os
from tqdm import tqdm

from pybman import utils
from pybman import Client

from .utils_paths import PURE_DIR

CTX_DIR = os.path.join(PURE_DIR, 'ctx')
ITEMS_DIR = os.path.join(PURE_DIR, 'item')


def routine():

    if not os.path.exists(ITEMS_DIR):
        os.makedirs(ITEMS_DIR)

    ################################
    ### RETRIEVE RECORDS OF CTXs ###
    ################################

    ctxs = utils.read_json(os.path.join(CTX_DIR, "all.json"))

    ctx_meta = {}

    for rec in ctxs['records']:
        objectId = rec['data']['objectId']
        ctx_meta[objectId] = rec['data']['name']

    ctx_ids = list(ctx_meta.keys())
    ctx_ids.sort()

    client = Client()

    for ctx_idx in tqdm(ctx_ids):
        print("retrieve data of context:", ctx_meta[ctx_idx])
        ctx_data = client.get_data(ctx_id=ctx_idx)
        utils.write_json(os.path.join(ITEMS_DIR, ctx_idx+".json"),
                         ctx_data.collection)


if __name__ == "__main__":
    routine()
