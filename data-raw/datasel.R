devtools::load_all()

# ///////////// #
# /// GRPAH /// #
# ///////////// #

pc_graph <- maxplanckr::get_pc_graph()

sel_ctx <- maxplanckr::read_data(pc_graph$sel_nodes_ctx)
sel_ous <- maxplanckr::read_data(pc_graph$sel_nodes_ous)
sel_ous_ctx <- maxplanckr::read_data(pc_graph$sel_edges_ous_ctx)

sel <- setNames(list(sel_ctx, sel_ous, sel_ous_ctx),
                   c("ctx", "ous", "ous_ctx"))
usethis::use_data(sel, overwrite=T)

# ////////////// #
# /// TABLES /// #
# ////////////// #

pc_tables <- maxplanckr::get_pc_tables()

# CREATORS

authors <- read_data(pc_tables$authors)
sel_items_aut <- authors[authors$Item %in% maxplanckr::sel_items$Id,]

externals <- maxplanckr::read_data(pc_tables$externals)
sel_items_ext <- externals[externals$Item %in% maxplanckr::sel_items$Id,]

organizations <- maxplanckr::read_data(pc_tables$organizations)
sel_items_ous <- organizations[organizations$Item %in% maxplanckr::sel_items$Id,]

sel_items_rel <- list(sel_items_aut, sel_items_ext, sel_items_ous)
sel_items_rel <- setNames(sel_items_rel, c("aut","ext","ous"))
usethis::use_data(sel_items_rel, overwrite=T)

# SOURCES

sources <- maxplanckr::read_data(pc_tables$sources)
sel_items_src <- sources[sources$Item %in% maxplanckr::sel_items$Id,]
usethis::use_data(sel_items_src, overwrite=T)

# SOURCES CREATORS

sources_authors <- maxplanckr::read_data(pc_tables$sources_authors)
sel_items_src_aut <- sources_authors[sources_authors$Item %in% maxplanckr::sel_items$Id,]

sources_externals <- maxplanckr::read_data(pc_tables$sources_externals)
sel_items_src_ext <- sources_externals[sources_externals$Item %in% maxplanckr::sel_items$Id,]

sources_organizations <- maxplanckr::read_data(pc_tables$sources_organizations)
sel_items_src_ous <- sources_organizations[sources_organizations$Item %in% maxplanckr::sel_items$Id,]

sel_items_src_rel <- list(sel_items_src_aut,sel_items_ext,sel_items_src_ous)
sel_items_src_rel <- setNames(sel_items_src_rel, c("aut","ext","ous"))

usethis::use_data(sel_items_src_rel, overwrite=T)
