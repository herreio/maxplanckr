# devtools::load_all()

pure_ctx <- maxplanckr::read_data(pc_graph$pure_nodes_ctx)
pure_ous <- maxplanckr::read_data(pc_graph$pure_nodes_ous)
pure_ctx_ous <- maxplanckr::read_data(pc_graph$pure_edges_ctx_ous)

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

sel_ctx <- maxplanckr::read_data(pc_graph$sel_nodes_ctx)
sel_ous <- maxplanckr::read_data(pc_graph$sel_nodes_ous)
sel_ous_ctx <- maxplanckr::read_data(pc_graph$sel_edges_ous_ctx)

usethis::use_data(pure_ctx, pure_ous, pure_ctx_ous,
                  mpis_ous, mpis_ctx, mpis_tags, mpis_cats,
                  mpis_ous_tree, mpis_ous_kids,
                  mpis_ctx_edges, mpis_ous_edges,
                  mpis_cats_edges, mpis_tags_edges,
                  mpis_cats_tags_edges,
                  sel_ctx, sel_ous, sel_ous_ctx,
                  internal=T,
                  overwrite=T)
