import os
import sys

from pybman import utils

from .utils_paths import SCRAPE_DIR, CTX_DIR, MAP_DIR, MAPPED_DIR, LOG_DIR

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

if not os.path.exists(MAPPED_DIR):
    os.makedirs(MAPPED_DIR)

print("console output is redirected to map_post.log ...")

stdout = sys.stdout

log = open(os.path.join(LOG_DIR, "map_post.log"), "w+")
sys.stdout = log

mpis = utils.read_json(os.path.join(SCRAPE_DIR, "all.json"))

print("scraped", len(mpis), "institues!")

mpis_mapped = utils.read_json(os.path.join(
    MAP_DIR, "mpi_ous.json"))  # ous.json

o = list(mpis_mapped.values())
m = list(mpis_mapped.keys())

ous_mpi = {}

for i in range(len(o)):
    ou = o[i]
    name = m[i]
    ous_mpi[ou] = name

print("done with reverse mapping!")
utils.write_json(os.path.join(MAPPED_DIR, 'ous_mpi.json'), ous_mpi)

m = list(mpis.keys())
n = list(mpis_mapped.keys())

counter = 0
no_map = []

for i in m:
    if i in n:
        counter += 1
        continue
    elif i == 'Research Group Social Neuroscience':
        # part of the Max Planck Institute for Human Cognitive and Brain Sciences
        continue
    else:
        no_map.append(i)

print("")
print(str(counter), "institutes mapped to ous")
print("")
print("ignored 'Research Group Social Neuroscience' (part of an institute...)")
if no_map:
    print("")
    print(len(no_map), "institutes could not be mapped to ou")
    print("")
    print("no mapping found for")
    for i in no_map:
        print("    ", i)

print("")
print("found", len(ous_mpi), "individual identifiers for institutes!")

########################
### MAP: OUS --> CTX ###
########################

print("")
print("")
print("map: ous --> ctx")


pure_ctxs = utils.read_json(os.path.join(CTX_DIR, "all.json"))

collections = {}

for rec in pure_ctxs['records']:
    objectId = rec['data']['objectId']
    maintainers = rec['data']['responsibleAffiliations']
    for maintainer in maintainers:
        maintainer = maintainer['objectId']
        if maintainer in collections:
            collections[maintainer].append(objectId)
        else:
            collections[maintainer] = [objectId]

m = list(set(mpis_mapped.values()))
m.sort()
n = list(collections.keys())

fnd = {}
counter = 0
print("")

for mpi in m:
    if mpi in n:
        fnd[mpi] = collections[mpi]
        counter += 1
    else:
        print(mpi, "has no context")

print("")
print(str(counter), "ous mapped to contexts")
print("")

utils.write_json(os.path.join(MAPPED_DIR, 'ous_ctx.json'), fnd)

########################
### MAP: CAT --> OUS ###
########################

print("")
print("")
print("map: cat --> ous")

cats = utils.read_json(os.path.join(SCRAPE_DIR, "categories.json"))
print("")

c = list(cats.keys())
n = list(mpis_mapped.keys())

cats_mapped = {}

total = 0
counter = 0

for cat in cats:
    cats_mapped[cat] = []
    total += len(cats[cat])
    for mpi in cats[cat]:
        if mpi in n:
            # prevent duplicate
            if mpis_mapped[mpi] not in cats_mapped[cat]:
                counter += 1
                cats_mapped[cat].append(mpis_mapped[mpi])
            else:
                continue
        elif mpi == 'Research Group Social Neuroscience':
            # part of the Max Planck Institute for Human Cognitive and Brain Sciences
            continue
        elif mpi in no_map:
            # mpi has no mapping
            continue
        else:
            print(mpi, "could not be mapped to", cat)


print("found", str(counter),"("+str(total)+")", "mappings to categories")
print("")
for cat in cats:
    print("number of institutes in category", cat+":", len(cats_mapped[cat]), "("+str(len(cats[cat]))+")")
print("")
utils.write_json(os.path.join(MAPPED_DIR, 'cat_ous.json'), cats_mapped)
print("")

n = list(mpis_mapped.values())

ous_cat = {}

for mpi in n:
    for cat in c:
        if mpi in cats_mapped[cat]:
            if mpi in ous_cat:
                ous_cat[mpi].append(cat)
            else:
                ous_cat[mpi] = [cat]
        else:
            continue

print("found mappings from", str(len(ous_cat)), "institutes to",str(len(cats)),"categories")
print("")
utils.write_json(os.path.join(MAPPED_DIR, 'ous_cat.json'), ous_cat)
print("")

########################
### MAP: TAG --> OUS ###
########################

m = list(mpis.keys())
n = list(mpis_mapped.keys())


all_tags = {}
mpis_tags = {}

total = 0
counter = 0
for mpi in m:
    idx = None
    tags = mpis[mpi]['tags']
    total += len(tags)
    for tag in tags:
        if tag not in all_tags:
            all_tags[tag] = [mpi]
        else:
            all_tags[tag].append(mpi)
    if mpi in n:
        idx = mpis_mapped[mpi]
    elif mpi == 'Research Group Social Neuroscience':
        # part of the MPI for Human Cognitive and Brain Sciences
        pass
    elif mpi in no_map:
        pass
    else:
        print("no idx found for", mpi)
    if idx:
        counter += len(tags)
        if idx not in mpis_tags:
            mpis_tags[idx] = tags
        else:
            if tags == mpis_tags[idx]:
                pass
            else:
                for tag in tags:
                    if tag not in mpis_tags[idx]:
                        mpis_tags[idx].append(tag)
    else:
        continue

tags = list(all_tags)
tags.sort()

tags_mpis = {}

for tag in tags:
    tag_mpis = [i for i in mpis_tags if tag in mpis_tags[i]]
    tags_mpis[tag] = tag_mpis

print("found", str(counter),"("+str(total)+")", "mappings to tags")
print("")

for tag in tags:
    print("number of institutes with tag", tag+":", len(tags_mpis[tag]),"("+str(len(all_tags[tag]))+")" )

print("")
utils.write_json(os.path.join(MAPPED_DIR, 'tags_ous.json'), tags_mpis)
print("")

print("found mappings from", str(len(mpis_tags)), "institutes to",str(len(all_tags)),"tags")
print("")


utils.write_json(os.path.join(MAPPED_DIR, 'all_tags.json'), all_tags)
utils.write_json(os.path.join(MAPPED_DIR, 'ous_tags.json'), mpis_tags)
# utils.write_list(os.path.join(MAPPED_DIR, 'ous_tags_all.txt'), all_tags)

log.close()
sys.stdout = stdout
