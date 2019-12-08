import os
import sys

from pybman import utils

from ..utils.paths import LOG_DIR, LANG_DIR, GRAPH_DIR


def routine():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(GRAPH_DIR):
        os.makedirs(GRAPH_DIR)

    stdout = sys.stdout

    print("console output is redirected to graph_languages.log ...")

    log = open(os.path.join(LOG_DIR, "graph_languages.log"), "w+")
    sys.stdout = log

    languages_raw = utils.read_json(os.path.join(LANG_DIR, 'collection.json'))

    languages = [['Id', 'Label', 'Coordinates']]

    dc_title = 'http_purl_org_dc_elements_1_1_title'
    # dc_idx = 'http_purl_org_dc_elements_1_1_identifier'
    google_coordinates = 'http_earth_google_com_kml_2_1_coordinates'

    for lang in languages_raw:
        name = ''
        if dc_title in languages_raw[lang]:
            name = languages_raw[lang][dc_title]
            if type(name) == list:
                name = name[0]
        else:
            print("no name found for language", lang)
        coordinates = ''
        if google_coordinates in languages_raw[lang]:
            coordinates = languages_raw[lang][google_coordinates]
        languages.append([lang, name, coordinates])

    utils.write_csv(os.path.join(GRAPH_DIR, 'pure--lang_nodes.csv'), languages)

    log.close()
    sys.stdout = stdout


if __name__ == "__main__":
    routine()
