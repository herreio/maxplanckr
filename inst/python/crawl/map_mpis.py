import os
from pybman import utils

from .utils_paths import MAP_DIR


def routine():

    all_ous = []
    all_fnd = {}

    eng_fnd = utils.read_json(os.path.join(MAP_DIR, "ous_fnd_eng.json"))

    for eng_ou in eng_fnd:
        all_fnd[eng_ou] = eng_fnd[eng_ou]
        all_ous.append(eng_fnd[eng_ou])

    deu_fnd = utils.read_json(os.path.join(MAP_DIR, "ous_fnd_deu.json"))
    # deu_ous = list(deu_fnd.values())

    for deu_ou in deu_fnd:
        if deu_fnd[deu_ou] not in all_ous:
            all_fnd[deu_ou] = deu_fnd[deu_ou]
            all_ous.append(deu_fnd[deu_ou])

    utils.write_json(os.path.join(MAP_DIR, "mpi_ous.json"), all_fnd)


if __name__ == "__main__":
    routine()
