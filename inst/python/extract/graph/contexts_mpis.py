import os
import sys

from pybman import utils

from ..utils.paths import LOG_DIR, CTX_DIR, OUS_DIR, MAPPED_DIR, GRAPH_DIR


def routine():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(GRAPH_DIR):
        os.makedirs(GRAPH_DIR)

    print("console output is redirected to graph_contexts_mpis.log ...")

    stdout = sys.stdout

    log = open(os.path.join(LOG_DIR, "graph_contexts_mpis.log"), "w+")
    sys.stdout = log

    ctxs = utils.read_json(os.path.join(CTX_DIR, "all.json"))
    ous = utils.read_json(os.path.join(OUS_DIR, "all.json"))
    mpis = utils.read_json(os.path.join(MAPPED_DIR, "ous_ctx.json"))

    institutes = [['Id', 'Label']]
    contexts = [['Id', 'Label', 'Created']]

    for rec in ous['records']:
        if rec['data']['objectId'] in mpis:
            objectId = rec['data']['objectId']
            name = utils.clean_string(rec['data']['name'])
            institutes.append([objectId, name])

    utils.write_csv(os.path.join(
        GRAPH_DIR, 'mpis--ous_nodes--ctx.csv'), institutes)

    institutes_contexts = [['Source', 'Target']]
    mpis_ctx = []

    for mpi in mpis:
        for context in mpis[mpi]:
            institutes_contexts.append([mpi, context])
            mpis_ctx.append(context)

    utils.write_csv(os.path.join(
        GRAPH_DIR, 'mpis--ous_ctx_edges.csv'), institutes_contexts)

    for rec in ctxs['records']:
        objectId = rec['data']['objectId']
        if objectId in mpis_ctx:
            name = rec['data']['name'].replace('"', '')
            created = rec['data']['creationDate'].split("-")[0]
            contexts.append([objectId, name, created])

    utils.write_csv(os.path.join(
        GRAPH_DIR, 'mpis--ctx_nodes--ous.csv'), contexts)

    log.close()
    sys.stdout = stdout


if __name__ == "__main__":
    routine()
