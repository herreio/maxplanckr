import os
from pybman import utils
from pybman.rest import OrgUnitRestController

from .utils_paths import PURE_DIR

OUS_DIR = os.path.join(PURE_DIR, 'ous')


def routine():

    if not os.path.exists(OUS_DIR):
        os.makedirs(OUS_DIR)

    ###########################################
    ### RETRIEVE ORGANIZATIONAL UNITS (OUS) ###
    ###########################################

    ou_controller = OrgUnitRestController()
    ous = ou_controller.get_all()

    utils.write_json(os.path.join(OUS_DIR, "all.json"), ous)


if __name__ == "__main__":
    routine()
