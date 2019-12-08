import os
import sys

from pybman import utils

from ..utils.paths import LOG_DIR, PERS_DIR, GRAPH_DIR


def routine():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(GRAPH_DIR):
        os.makedirs(GRAPH_DIR)

    print("console output is redirected to graph_persons.log ...")

    stdout = sys.stdout

    log = open(os.path.join(LOG_DIR, "graph_persons.log"), "w+")

    sys.stdout = log

    pers = utils.read_json(os.path.join(PERS_DIR, 'collection.json'))

    escidoc_pos = 'http_purl_org_escidoc_metadata_terms_0_1_position'
    dc_idx = 'http_purl_org_dc_elements_1_1_identifier'
    dc_title = 'http_purl_org_dc_elements_1_1_title'
    dc_alternative = 'http_purl_org_dc_terms_alternative'
    # xmlns_family = 'http_xmlns_com_foaf_0_1_family_name'
    # xmlns_given = 'http_xmlns_com_foaf_0_1_givenname'
    # eprint_affilation = 'http_purl_org_eprint_terms_affiliatedInstitution'

    persons = [['Id', 'Label']]
    persons_institutes = [['Source', 'Target']]

    for p in pers:
        pers_id = pers[p]['id'].split("/")[-1]
        if dc_title in pers[p]:
            pers_name = pers[p][dc_title]
        elif dc_alternative in pers[p]:
            pers_name = pers[p][dc_alternative]
        else:
            pers_name = 'None'
            print("no name found for", pers_id, "!")
        persons.append([pers_id, pers_name])
        if escidoc_pos in pers[p]:
            affiliation = pers[p][escidoc_pos]
            if type(affiliation) == dict:
                if dc_idx in affiliation:
                    affiliation_id = affiliation[dc_idx]
                    persons_institutes.append([pers_id, affiliation_id])
                else:
                    print("no ou_id found for affiliation of", pers_id + "!")
            elif type(affiliation) == list:
                found = False
                for a in affiliation:
                    if dc_idx in a:
                        affiliation_id = a[dc_idx]
                        persons_institutes.append([pers_id, affiliation_id])
                        found = True
                if not found:
                    print("no ou_id found for affiliation of", pers_id + "!")
            elif not affiliation:
                pass
            else:
                print("impossible! affiliation type unknown of person",
                      pers_id + '!')
                print(type(affiliation))
                print(affiliation)
        else:
            print("no affilation found for", pers_id + "!")
            print("skip person...")
            continue

    utils.write_csv(os.path.join(GRAPH_DIR, 'pure--pers_nodes.csv'), persons)
    utils.write_csv(os.path.join(
        GRAPH_DIR, 'pure--pers_ous_edges.csv'), persons_institutes)

    log.close()
    sys.stdout = stdout


if __name__ == "__main__":
    routine()
