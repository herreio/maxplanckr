import os
from tqdm import tqdm
from pybman import utils
from pybman.rest import LanguageConeController

from .utils_paths import PURE_DIR

LANG_DIR = os.path.join(PURE_DIR, "lang")


def routine():

    if not os.path.exists(LANG_DIR):
        os.makedirs(LANG_DIR)

    #################################################
    ### RETRIEVE LIST OF LANGUAGES (CoNE/ISO 639) ###
    #################################################

    lang_controller = LanguageConeController()
    langs = lang_controller.get_entities()

    utils.write_json(os.path.join(LANG_DIR, 'all.json'), langs)

    #################################################
    ### RETRIEVE INDIVIDUAL ENTRIES FOR LANGUAGES ###
    #################################################

    lang_meta = {}

    for lang in langs:
        idx = lang['id'].split("/")[-1]
        lang_meta[idx] = lang['value']

    lang_ids = list(lang_meta.keys())

    # request data
    lang_data = {}
    for idx in tqdm(lang_ids):
        lang_details = lang_controller.get_entity(idx)
        lang_data[idx] = lang_details

    utils.write_json(os.path.join(LANG_DIR, 'collection.json'), lang_data)


if __name__ == "__main__":
    routine()
