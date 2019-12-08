import os
import sys
import csv
import time

from pybman import utils
from pybman import DataSet

from ..utils.paths import EXTDATA_DIR, LOG_DIR, MAPPED_DIR, STATS_DIR


def routine():

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    print("console output is redirected to count_records.log ...")

    stdout = sys.stdout
    log = open(os.path.join(LOG_DIR, "count_records.log"), "w+")
    sys.stdout = log

    from ..utils.local import ld

    REC_STATS = os.path.join(STATS_DIR, 'records')

    if not os.path.exists(REC_STATS):
        os.makedirs(REC_STATS)

    ous_ctx = utils.read_json(os.path.join(EXTDATA_DIR, 'selected.json'))
    mpis = utils.read_json(os.path.join(MAPPED_DIR, 'ous_mpi.json'))

    stats = {}

    print("start counting!")
    start_time = time.time()

    for mpi in mpis:
        if mpi not in ous_ctx:
            print(mpi, "has no contexts!")
            print("")
            continue
        print("")
        print("processing", mpi, "...")
        mpi_ctxs = ous_ctx[mpi]
        mpi_total = 0
        for mpi_ctx in mpi_ctxs:
            print("extracting", mpi_ctx, "...")

            all = ld.get_data(mpi_ctx)[0]

            # consider only released items
            data_set = DataSet(data_id=all.idx + "_released",
                               raw=all.get_items_released())

            if not data_set.records:
                print(mpi_ctx, "has no records!")
                print("")
                continue

            print("with", data_set.num, "records...")
            mpi_total += data_set.num

        stats[mpi] = mpi_total

    print("finished counting after %s sec!" %
          round(time.time() - start_time, 2))

    total = len(stats)

    stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

    path = os.path.join(REC_STATS, 'all.csv')

    with open(path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t',
                                quotechar='"', quoting=csv.QUOTE_NONE)
        csv_writer.writerow(['institute', 'publications'])
        for i in range(0, total):
            ou, pub = stats[i]
            mpi = mpis[ou].replace(" (Hannover)", "").replace(
                " (Greifswald)", "")
            csv_writer.writerow([mpi, pub])

    log.close()
    sys.stdout = stdout


if __name__ == '__main__':
    routine()
