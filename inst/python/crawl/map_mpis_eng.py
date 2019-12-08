import os
import sys
from pybman import utils

from .utils_paths import SCRAPE_DIR, OUS_DIR, MAP_DIR, LOG_DIR

def routine():

    if not os.path.exists(MAP_DIR):
        os.makedirs(MAP_DIR)

    ##############################################################
    ### READ FILES CONTAINING ALL MAX PLANCK INSTITUTES (MPIs) ###
    ### AND ORGANIZATIONAL UNITS (OUs) FROM PURE #################
    ##############################################################

    mpis = utils.read_json(os.path.join(SCRAPE_DIR, 'all.json'))
    pure_ous = utils.read_json(os.path.join(OUS_DIR, 'all.json'))

    ############################
    ### EXTRACT NAMES OF OUs ###
    ############################

    names = {}

    for record in pure_ous['records']:
        idx = record['data']['objectId']
        metadata = record['data']['metadata']
        name = metadata['name'].strip()
        names[name] = idx
        if 'alternativeNames' in metadata and metadata['alternativeNames'][0]:
            for altname in metadata['alternativeNames']:
                names[altname.strip()] = idx

    m = list(mpis.keys())
    n = list(names.keys())

    #############################
    ### MAP MPIs TO NAMES/OUs ###
    #############################

    not_fnd = []
    fnd = {}

    for mpi in m:
        if mpi in n:
            fnd[mpi] = names[mpi]
        elif mpi.replace('Max Planck Institute', 'MPI') in n:
            fnd[mpi] = names[mpi.replace('Max Planck Institute', 'MPI')]
        elif mpi.split(",")[0] in n:
            fnd[mpi] = names[mpi.split(",")[0]]
            # Max Planck Institute for Software Systems, Kaiserslautern site
            # Max Planck Institute for Software Systems, Saarbrücken site
            # Max Planck Institute for Intelligent Systems, Stuttgart site
            # Max Planck Institute for Intelligent Systems, Tübingen site
        elif mpi.split(" (")[0] in n:
            fnd[mpi] = names[mpi.split(" (")[0]]
            # Max Planck Institute for Gravitational Physics (Hannover)
            # Max Planck Institute for Ornithology (Radolfzell)
            # Max Planck Institute for Plasma Physics (Greifswald)
        elif mpi == 'Research Group Social Neuroscience':
            # part of the Max Planck Institute for Human Cognitive and Brain Sciences
            continue
        else:
            # print("no equivalent found for", mpi)
            not_fnd.append(mpi)

    idea = {}

    for no_eq in not_fnd:
        parts = no_eq.split('Max Planck Institute for')
        if len(parts) > 1:
            for ou in n:
                if parts[1].strip().lower() in ou.lower():
                    if no_eq in idea:
                        if ou not in idea[no_eq]:
                            idea[no_eq].append(ou)
                    else:
                        idea[no_eq] = [ou]

    for no_eq in not_fnd:
        parts = no_eq.split('for')
        if len(parts) > 1:
            for ou in n:
                if parts[1].strip().lower() in ou.lower():
                    if no_eq in idea:
                        if ou not in idea[no_eq]:
                            idea[no_eq].append(ou)
                    else:
                        idea[no_eq] = [ou]

    for no_eq in not_fnd:
        parts = no_eq.split('of')
        if len(parts) > 1:
            for ou in n:
                if parts[1].strip().lower() in ou.lower():
                    if no_eq in idea:
                        if ou not in idea[no_eq]:
                            idea[no_eq].append(ou)
                    else:
                        idea[no_eq] = [ou]

    for no_eq in not_fnd:
        parts = no_eq.split(',')
        if len(parts) > 1:
            for ou in n:
                if parts[0].strip().lower() in ou.lower():
                    if no_eq in idea:
                        if ou not in idea[no_eq]:
                            idea[no_eq].append(ou)
                    else:
                        idea[no_eq] = [ou]

    ###############################
    ### PRINT AND WRITE RESULTS ###
    ###############################

    print("")
    print("found matches for")
    counter = 0
    for mpi in m:
        if mpi not in not_fnd:
            counter += 1
            print(mpi)

    print(str(counter),"in total")
    utils.write_json(os.path.join(MAP_DIR, "ous_fnd_eng.json"), fnd)

    print("")
    print("found possible matches for")
    counter = 0
    for nt_eq in idea:
        counter += 1
        print(nt_eq)

    print(str(counter),"in total")
    utils.write_json(os.path.join(MAP_DIR, "ous_ideas_eng.json"), idea)

    print("")
    print("no match found for")
    counter = 0
    for nt_eq in not_fnd:
        if nt_eq not in idea:
            counter += 1
            print(nt_eq)

    print(str(counter),"in total")
    print("")
    utils.write_json(os.path.join(MAP_DIR, "ous_not_fnd_eng.txt"), not_fnd)


if __name__ == "__main__":

    print("console output is redirected to map_eng.log ...")

    stdout = sys.stdout
    log = open(os.path.join(LOG_DIR, "map_eng.log"), "w+")
    sys.stdout = log

    routine()

    log.close()
    sys.stdout = stdout
