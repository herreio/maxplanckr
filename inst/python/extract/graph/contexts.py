import os
import sys

from pybman import utils

from ..utils.paths import LOG_DIR, CTX_DIR, GRAPH_DIR


def routine():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(GRAPH_DIR):
        os.makedirs(GRAPH_DIR)

    print("console output is redirected to graph_contexts.log ...")

    stdout = sys.stdout

    log = open(os.path.join(LOG_DIR, "graph_contexts.log"), "w+")
    sys.stdout = log

    ctxs = utils.read_json(os.path.join(CTX_DIR, "all.json"))

    ctx_nodes = [["Id", "Label", "Created"]]
    ctx_edges = [["Source", "Target"]]

    for rec in ctxs['records']:
        objectId = rec['data']['objectId']
        name = rec['data']['name']
        created = rec['data']['creationDate'].split("-")[0]
        ctx_nodes.append([objectId, name, created])
        maintainers = rec['data']['responsibleAffiliations']
        for m in maintainers:
            maintainer = m['objectId']
            ctx_edges.append([objectId, maintainer])

    utils.write_csv(os.path.join(GRAPH_DIR, "pure--ctx_nodes.csv"), ctx_nodes)
    utils.write_csv(os.path.join(
        GRAPH_DIR, "pure--ctx_ous_edges.csv"), ctx_edges)

    log.close()
    sys.stdout = stdout


if __name__ == "__main__":
    routine()
