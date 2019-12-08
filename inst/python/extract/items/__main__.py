from ..utils.local import ld, data_paths
import os
import sys
import time

from pybman import utils
from pybman import DataSet

from . import utils as extract
from ..utils.clean import clean_title
from ..utils.paths import LOG_DIR, GRAPH_DIR, TABLES_DIR

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

if not os.path.exists(GRAPH_DIR):
    os.makedirs(GRAPH_DIR)

if not os.path.exists(TABLES_DIR):
    os.makedirs(TABLES_DIR)

print("start extraction of items!")

print("console output is redirected to items.log ...")

stdout = sys.stdout

log = open(os.path.join(LOG_DIR, "items.log"), "w+")
sys.stdout = log


items_total = []

pub_table = [["Id", "Label", "Year", "Genre", "Lang",
              "Identifier", "IdentifierType", "Context"]]
org_table = [["Id", "Item", "Label", "Role", "Identifier"]]
aut_table = [["Id", "Item", "Label", "givenName", "Role",
              "Identifier", "IdentiferType", "Organization"]]
ext_table = [["Id", "Item", "Label", "givenName", "Role", "Organization"]]
src_table = [["Id", "Item", "Label", "Genre", "Identifier", "IdentiferType"]]
src_aut_table = [["Id", "Item", "Source", "Label", "givenName",
                  "Role", "Identifier", "IdentiferType", "Organization"]]
src_ext_table = [["Id", "Item", "Source",
                  "Label", "givenName", "Role", "Organization"]]
src_org_table = [["Id", "Item", "Source", "Label", "Role", "Identifier"]]

pub_nodes = [["Id", "Label"]]
pub_org_nodes = [["Id", "Label"]]
pub_auth_nodes = [["Id", "Label", "givenName", "IdType"]]
pub_ext_nodes = [["Id", "Label", "givenName"]]
pub_auth_org_nodes = [["Id", "Label", "IdentifierPath", "Address"]]
pub_ext_org_nodes = [["Id", "Label", "IdentifierPath", "Address"]]

pub_src_org_nodes = [["Id", "Label"]]
pub_src_ext_nodes = [["Id", "Label", "givenName"]]
pub_src_auth_nodes = [["Id", "Label", "givenName", "IdType"]]
pub_src_auth_org_nodes = [["Id", "Label", "IdentifierPath", "Address"]]
pub_src_ext_org_nodes = [["Id", "Label", "IdentifierPath", "Address"]]

pub_org_edges = [["Source", "Target"]]
pub_ext_edges = [["Source", "Target"]]
pub_auth_edges = [["Source", "Target"]]
pub_auth_org_edges = [["Source", "Target"]]
pub_ext_org_edges = [["Source", "Target"]]

pub_src_org_edges = [["Source", "Target"]]
pub_src_auth_edges = [["Source", "Target"]]
pub_src_ext_edges = [["Source", "Target"]]
pub_src_auth_org_edges = [["Source", "Target"]]
pub_src_ext_org_edges = [["Source", "Target"]]

all_pers = []
all_orgs = []
all_pers_orgs = []
all_ext_orgs = []
all_src_pers = []
all_src_orgs = []
all_src_pers_orgs = []
all_src_ext_orgs = []

aut_table_i = 1
ext_table_i = 1
org_table_i = 1
src_table_i = 1
src_aut_table_i = 1
src_ext_table_i = 1
src_org_table_i = 1

print("start processing data!")

start_time = time.time()

for path in data_paths:

    idx = path.split("/")[-1].replace(".json", "")

    print("")
    print("processing", idx, "...")

    all = ld.get_data(idx)[0]

    # consider only released items
    data_set = DataSet(data_id=all.idx + "_released",
                       raw=all.get_items_released())

    print(data_set.num, "records to process...")

    # loop over every record
    for record in data_set.records:

        # ///////////////////// #
        # /// PUBLICATIONS /// #
        # /////////////////// #

        item_id = extract.idx_from_item(record)
        item_year = extract.date_from_item(record)
        item_title = clean_title(extract.title_from_item(record))
        item_genre = extract.genre_from_item(record)
        item_lang = ";".join(extract.languages_from_items(record))
        item_id_type, item_id_value = extract.identifers_from_item(record)[0]
        item_ctx = extract.ctx_idx_from_item(record)

        items_total.append(item_id)

        pub_table.append([item_id,
                          item_title,
                          item_year,
                          item_genre,
                          item_lang,
                          item_id_value,
                          item_id_type,
                          item_ctx])

        pub_nodes.append([item_id,
                          item_title])

        # ///////////////// #
        # /// CREATORS /// #
        # ////////////// #

        # PERSONS

        for j, persons in enumerate(extract.persons_from_item(record)):
            pers_role = extract.role_from_creator(persons)
            pers_name = extract.persons_name_from_creator(persons)
            pers_id, pers_id_type = extract.persons_id_from_creator(persons)
            pers_org_id, pers_org_id_path, pers_org_name,\
                pers_org_address = extract.persons_affiliation_from_creator(persons)[0]\
                if extract.persons_affiliation_from_creator(persons) else ("", "", "", "")
            if pers_id:
                aut_table.append([str(aut_table_i),
                                  item_id,
                                  pers_name[1],
                                  pers_name[0],
                                  pers_role,
                                  pers_id,
                                  pers_id_type,
                                  pers_org_id])

                aut_table_i += 1
                pub_auth_edges.append([item_id, pers_id])

                if pers_id not in all_pers:
                    pub_auth_nodes.append([pers_id,
                                           pers_name[1],
                                           pers_name[0],
                                           pers_id_type])
                    all_pers.append(pers_id)

                if pers_org_id:
                    # pub_auth_org--coop_edges.append([item_id,pers_org_id])
                    pub_auth_org_edges.append([pers_id, pers_org_id])

                    if pers_org_id not in all_pers_orgs:
                        pub_auth_org_nodes.append([pers_org_id,
                                                   pers_org_name,
                                                   ";".join(pers_org_id_path),
                                                   pers_org_address])
                        all_pers_orgs.append(pers_org_id)

            else:
                ext_table.append([str(ext_table_i),
                                  item_id,
                                  pers_name[1],
                                  pers_name[0],
                                  pers_role,
                                  pers_org_id])
                ext_id = 'external' + str(ext_table_i)
                pub_ext_nodes.append([ext_id,
                                      pers_name[1],
                                      pers_name[0]])
                pub_ext_edges.append([item_id,
                                      ext_id])

                if pers_org_id:
                    # pub_ext_org--coop_edges.append([item_id,pers_org_id])
                    pub_ext_org_edges.append([ext_id, pers_org_id])

                    if pers_org_id not in all_ext_orgs:
                        pub_ext_org_nodes.append([pers_org_id,
                                                  pers_org_name,
                                                  ";".join(pers_org_id_path),
                                                  pers_org_address])
                        all_ext_orgs.append(pers_org_id)

                ext_table_i += 1

        # ORGANIZATIONS

        for j, organization in enumerate(extract.organizations_from_item(record)):
            org_role = extract.role_from_creator(organization)
            org_id = extract.organizations_identifier_from_creator(
                organization)
            org_name = extract.organizations_name_from_creator(organization)
            org_table.append([str(org_table_i),
                              item_id,
                              org_name,
                              org_role,
                              org_id])
            if org_id:
                pub_org_edges.append([item_id, org_id])
                if org_id not in all_orgs:
                    pub_org_nodes.append([org_id, org_name])
                    all_orgs.append(org_id)
            org_table_i += 1

        # //////////////// #
        # /// SOURCES /// #
        # ////////////// #

        src_idx = extract.sources_identifiers_from_item(record)
        src_title_genre = extract.sources_titles_genres_from_item(record)
        src_pers = extract.sources_persons_id_from_item(record)
        src_pers_affil = extract.sources_persons_affiliations_from_item(record)
        src_orgs = extract.sources_organizations_from_item(record)

        for i, title_genre in enumerate(src_title_genre):
            src_title, src_genre = title_genre
            src_title = clean_title(src_title)
            src_id_type, src_id_value = src_idx[i][0]

            src_table.append([str(src_table_i),
                              item_id,
                              src_title,
                              src_genre,
                              src_id_value,
                              src_id_type])

            for j, src_pers_data in enumerate(src_pers[i]):
                src_pers_id, src_pers_gname, src_pers_name,\
                    src_pers_role, src_pers_id_type = src_pers_data
                src_pers_org_id, src_pers_org_idpath,\
                    src_pers_org_name, src_pers_org_address = src_pers_affil[i][j][0]\
                    if src_pers_affil[i][j] else ("", "", "", "")
                if src_pers_id:
                    src_aut_table.append([str(src_aut_table_i),
                                          item_id,
                                          str(src_table_i),
                                          src_pers_name,
                                          src_pers_gname,
                                          src_pers_role,
                                          src_pers_id,
                                          src_pers_id_type,
                                          src_pers_org_id])

                    pub_src_auth_edges.append([item_id, src_pers_id])
                    if src_pers_id not in all_src_pers:
                        pub_src_auth_nodes.append([src_pers_id,
                                                   src_pers_name,
                                                   src_pers_gname,
                                                   src_pers_id_type])
                        all_src_pers.append(src_pers_id)

                    if src_pers_org_id:
                        # pub_src_auth_org--coop_edges.append([item_id,src_pers_org_id])
                        pub_src_auth_org_edges.append(
                            [src_pers_id, src_pers_org_id])
                        if src_pers_org_id not in all_src_pers_orgs:
                            pub_src_auth_org_nodes.append([src_pers_org_id,
                                                           src_pers_org_name,
                                                           ";".join(
                                                               src_pers_org_idpath),
                                                           src_pers_org_address])
                            all_src_pers_orgs.append(src_pers_org_id)

                    src_aut_table_i += 1
                else:
                    src_ext_table.append([str(src_ext_table_i),
                                          item_id,
                                          str(src_table_i),
                                          src_pers_name,
                                          src_pers_gname,
                                          src_pers_role,
                                          src_pers_org_id])
                    src_ext_id = 'src_external' + str(src_ext_table_i)
                    pub_src_ext_nodes.append(
                        [src_ext_id, src_pers_name, src_pers_gname])
                    pub_src_ext_edges.append([item_id, src_ext_id])

                    if src_pers_org_id:
                        # pub_src_ext_org--coop_edges.append([item_id,src_pers_org_id])
                        pub_src_ext_org_edges.append(
                            [src_ext_id, src_pers_org_id])
                        if src_pers_org_id not in all_src_ext_orgs:
                            pub_src_ext_org_nodes.append([src_pers_org_id,
                                                          src_pers_org_name,
                                                          ";".join(
                                                              src_pers_org_idpath),
                                                          src_pers_org_address])
                            all_src_ext_orgs.append(src_pers_org_id)

                    src_ext_table_i += 1

            for j, organization in enumerate(src_orgs[i]):
                src_org_role = extract.role_from_creator(organization)
                src_org_id = extract.organizations_identifier_from_creator(
                    organization)
                src_org_name = extract.organizations_name_from_creator(
                    organization)
                src_org_table.append([str(src_org_table_i),
                                      item_id,
                                      str(src_table_i),
                                      src_org_name,
                                      src_org_role,
                                      src_org_id])
                if src_org_id:
                    pub_src_org_edges.append([item_id, src_org_id])
                    if src_org_id not in all_src_orgs:
                        pub_src_org_nodes.append([src_org_id, src_org_name])
                        all_src_orgs.append(src_org_id)
                src_org_table_i += 1

            src_table_i += 1

print("")
print("processed", len(items_total), "records from",
      len(data_paths), "collections!")
print("found", len(src_table) - 1, "sources!")
print("found", aut_table_i, "internal authorships!")
print("found", ext_table_i, "external authorships!")

print("")

utils.write_csv(os.path.join(TABLES_DIR, "publications.csv"), pub_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_sources.csv"), src_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_authors.csv"), aut_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_externals.csv"), ext_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_organizations.csv"), org_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_sources_authors.csv"), src_aut_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_sources_externals.csv"), src_ext_table)
utils.write_csv(os.path.join(
    TABLES_DIR, "publications_sources_organizations.csv"), src_org_table)

utils.write_csv(os.path.join(GRAPH_DIR, "items--pub-nodes.csv"), pub_nodes)
utils.write_csv(os.path.join(GRAPH_DIR, "items--ous-nodes.csv"), pub_org_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--pers-nodes.csv"), pub_auth_nodes)
utils.write_csv(os.path.join(GRAPH_DIR, "items--ext-nodes.csv"), pub_ext_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--pers-ous-nodes.csv"), pub_auth_org_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--ext-ous-nodes.csv"), pub_ext_org_nodes)

utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-ous-nodes.csv"), pub_src_org_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-pers-nodes.csv"), pub_src_auth_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-ext-nodes.csv"), pub_src_ext_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-pers-ous-nodes.csv"), pub_src_auth_org_nodes)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-ext-ous-nodes.csv"), pub_src_ext_org_nodes)

utils.write_csv(os.path.join(
    GRAPH_DIR, "items--pub-ous-edges.csv"), pub_org_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--pub-pers-edges.csv"), pub_auth_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--pub-ext-edges.csv"), pub_ext_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--pers-ous-edges.csv"), pub_auth_org_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--ext-ous-edges.csv"), pub_ext_org_edges)

utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-ous-edges.csv"), pub_src_org_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-pers-edges.csv"), pub_src_auth_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-ext-edges.csv"), pub_src_ext_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-pers-ous-edges.csv"), pub_src_auth_org_edges)
utils.write_csv(os.path.join(
    GRAPH_DIR, "items--src-ext-ous-edges.csv"), pub_src_ext_org_edges)

finished = time.time()

print("finished extraction after %s min!" %
      round((finished - start_time) / 60, 2))

log.close()
sys.stdout = stdout

print("finished extraction after %s min!" %
      round((finished - start_time) / 60, 2))
