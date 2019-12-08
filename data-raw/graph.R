# devtools::load_all()

pc_graph <- maxplanckr::get_pc_graph()

# ////////////////// #
# /// REPOSITORY /// #
# ////////////////// #

pure_ctx <- maxplanckr::read_data(pc_graph$pure_nodes_ctx)
pure_ous <- maxplanckr::read_data(pc_graph$pure_nodes_ous)
pure_ctx_ous <- maxplanckr::read_data(pc_graph$pure_edges_ctx_ous)

pure <- setNames(
  list(pure_ctx, pure_ous, pure_ctx_ous),
  c("ctx", "ous", "ctx_ous")
)

usethis::use_data(pure, overwrite=T)

# ////////////////// #
# /// INSTITUTES /// #
# ////////////////// #

mpis_ous <- maxplanckr::read_data(pc_graph$mpis_nodes_ous)
mpis_ctx <- maxplanckr::read_data(pc_graph$mpis_nodes_ctx)
mpis_cats <- maxplanckr::read_data(pc_graph$mpis_nodes_cats)
mpis_tags <- maxplanckr::read_data(pc_graph$mpis_nodes_tags)
mpis_ous_tree <- maxplanckr::read_data(pc_graph$mpis_nodes_ous_tree_full)
mpis_ous_kids <- maxplanckr::read_data(pc_graph$mpis_nodes_ous_tree_children)
mpis_ctx_edges <- maxplanckr::read_data(pc_graph$mpis_edges_ous_ctx)
mpis_ous_edges <- maxplanckr::read_data(pc_graph$mpis_edges_ous_ous)
mpis_cats_edges <- maxplanckr::read_data(pc_graph$mpis_edges_ous_cats)
mpis_tags_edges <- maxplanckr::read_data(pc_graph$mpis_edges_ous_tags)
mpis_cats_tags_edges <- maxplanckr::read_data(pc_graph$mpis_edges_cats_tags)

mpis <- setNames(
  list(mpis_ous, mpis_ctx, mpis_cats,mpis_tags,
       mpis_ous_tree,mpis_ous_kids,mpis_ctx_edges,
       mpis_ous_edges, mpis_cats_edges, mpis_tags_edges,
       mpis_cats_tags_edges),
  c("ous","ctx","cats","tags",
    "ous_tree","ous_kids","ctx_edges",
    "ous_edges","cats_edges","tags_edges",
    "cats_tags_edges")
)

usethis::use_data(mpis, overwrite=T)

# ///////////// #
# /// ITEMS /// #
# ///////////// #

items_nodes_pub <- maxplanckr::read_data(pc_graph$items_nodes_pub)
items_nodes_ous <- maxplanckr::read_data(pc_graph$items_nodes_ous)
items_nodes_pers <- maxplanckr::read_data(pc_graph$items_nodes_pers)
items_nodes_pers_ous <- maxplanckr::read_data(pc_graph$items_nodes_pers_ous)
items_nodes_ext <- maxplanckr::read_data(pc_graph$items_nodes_ext)
items_nodes_ext_ous <- maxplanckr::read_data(pc_graph$items_nodes_ext_ous)
items_nodes_src_ous <- maxplanckr::read_data(pc_graph$items_nodes_src_ous)
items_nodes_src_pers <- maxplanckr::read_data(pc_graph$items_nodes_src_pers)
items_nodes_src_pers_ous <- maxplanckr::read_data(pc_graph$items_nodes_src_pers_ous)
items_nodes_src_ext <- maxplanckr::read_data(pc_graph$items_nodes_src_ext)
items_nodes_src_ext_ous <- maxplanckr::read_data(pc_graph$items_nodes_src_ext_ous)
items_edges_pub_ous <- maxplanckr::read_data(pc_graph$items_edges_pub_ous)
items_edges_pub_pers <- maxplanckr::read_data(pc_graph$items_edges_pub_pers)
items_edges_pub_ext <- maxplanckr::read_data(pc_graph$items_edges_pub_ext)
items_edges_pers_ous <- maxplanckr::read_data(pc_graph$items_edges_pers_ous)
items_edges_ext_ous <- maxplanckr::read_data(pc_graph$items_edges_ext_ous)
items_edges_src_ext <- maxplanckr::read_data(pc_graph$items_edges_src_ext)
items_edges_src_ext_ous <- maxplanckr::read_data(pc_graph$items_edges_src_ext)
items_edges_src_ous <- maxplanckr::read_data(pc_graph$items_edges_src_ous)
items_edges_src_pers <- maxplanckr::read_data(pc_graph$items_edges_src_pers)
items_edges_src_pers_ous <- maxplanckr::read_data(pc_graph$items_edges_src_pers_ous)


items <- setNames(
  list(items_nodes_pub, items_nodes_ous, items_nodes_pers, items_nodes_pers_ous,
      items_nodes_ext, items_nodes_ext_ous, items_nodes_src_ous, items_nodes_src_pers,
      items_nodes_src_pers_ous, items_nodes_src_ext, items_nodes_src_ext_ous,
      items_edges_pub_ous, items_edges_pub_pers, items_edges_pub_ext,
      items_edges_pers_ous, items_edges_ext_ous, items_edges_src_ext,
      items_edges_src_ext_ous, items_edges_src_ous, items_edges_src_pers,
      items_edges_src_pers_ous),
  c("nodes_pub", "nodes_ous", "nodes_pers", "nodes_pers_ous",
  "nodes_ext", "nodes_ext_ous", "nodes_src_ous", "nodes_src_pers",
  "nodes_src_pers_ous", "nodes_src_ext", "nodes_src_ext_ous",
  "edges_pub_ous", "edges_pub_pers", "edges_pub_ext",
  "edges_pers_ous", "edges_ext_ous", "edges_src_ext",
  "edges_src_ext_ous", "edges_src_ous", "edges_src_pers",
  "edges_src_pers_ous")
)

usethis::use_data(items, overwrite=T)

# ///////////////// #
# /// SELECTION /// #
# ///////////////// #

sel_ctx <- maxplanckr::read_data(pc_graph$sel_nodes_ctx)
sel_ous <- maxplanckr::read_data(pc_graph$sel_nodes_ous)
sel_ous_ctx <- maxplanckr::read_data(pc_graph$sel_edges_ous_ctx)

sel <- setNames(list(sel_ctx, sel_ous, sel_ous_ctx),
                   c("ctx", "ous", "ous_ctx"))
usethis::use_data(sel, overwrite=T)
