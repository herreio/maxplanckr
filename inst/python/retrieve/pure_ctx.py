import os
from pybman import utils
from pybman.rest import ContextRestController

from .utils_paths import PURE_DIR

CTX_DIR = os.path.join(PURE_DIR, 'ctx')


def routine():

    if not os.path.exists(CTX_DIR):
        os.makedirs(CTX_DIR)

    ################################
    ### RETRIEVE CONTEXTS (CTXs) ###
    ################################

    ctx_controller = ContextRestController()
    ctxs = ctx_controller.get_all()

    utils.write_json(os.path.join(CTX_DIR, 'all.json'), ctxs)


if __name__ == "__main__":
    routine()
