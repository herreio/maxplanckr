import os
from tqdm import tqdm
from pybman import utils
from pybman.rest import JournalConeController

from .utils_paths import PURE_DIR

JOUR_DIR = os.path.join(PURE_DIR, 'jour')


def routine():

    if not os.path.exists(JOUR_DIR):
        os.makedirs(JOUR_DIR)

    #################################
    ### RETRIEVE LIST OF JOURNALS ###
    #################################

    jour_controller = JournalConeController()
    journals = jour_controller.get_entities()

    utils.write_json(os.path.join(JOUR_DIR, 'all.json'), journals)

    ################################################
    ### RETRIEVE INDIVIDUAL ENTRIES FOR JOURNALS ###
    ################################################

    jour_meta = {}

    for jour in journals:
        idx = jour['id'].split("/")[-1]
        jour_meta[idx] = jour['value']

    jour_ids = list(jour_meta.keys())

    # request data
    jour_data = {}
    for idx in tqdm(jour_ids):
        jour_details = jour_controller.get_entity(idx)
        jour_data[idx] = jour_details

    utils.write_json(os.path.join(JOUR_DIR, 'collection.json'), jour_data)


if __name__ == "__main__":
    routine()
