# devtools::load_all()

pure_ctx <- read_data(pc_graph$pure_nodes_ctx)
pure_ous <- read_data(pc_graph$pure_nodes_ous)
pure_ctx_ous <- read_data(pc_graph$pure_edges_ctx_ous)

mpis_ous <- read_data(pc_graph$mpis_nodes_ous)
mpis_ctx <- read_data(pc_graph$mpis_nodes_ctx)
mpis_cats <- read_data(pc_graph$mpis_nodes_cats)
mpis_tags <- read_data(pc_graph$mpis_nodes_tags)
mpis_ous_tree <- read_data(pc_graph$mpis_nodes_ous_tree_full)
mpis_ous_kids <- read_data(pc_graph$mpis_nodes_ous_tree_children)

mpis_ctx_edges <- read_data(pc_graph$mpis_edges_ous_ctx)
mpis_ous_edges <- read_data(pc_graph$mpis_edges_ous_ous)
mpis_cats_edges <- read_data(pc_graph$mpis_edges_ous_cats)
mpis_tags_edges <- read_data(pc_graph$mpis_edges_ous_tags)
mpis_cats_tags_edges <- read_data(pc_graph$mpis_edges_cats_tags)

sel_ctx <- read_data(pc_graph$sel_nodes_ctx)
sel_ous <- read_data(pc_graph$sel_nodes_ous)
sel_ous_ctx <- read_data(pc_graph$sel_edges_ous_ctx)

usethis::use_data(pure_ctx, pure_ous, pure_ctx_ous,
                  mpis_ous, mpis_ctx, mpis_tags, mpis_cats,
                  mpis_ous_tree, mpis_ous_kids,
                  mpis_ctx_edges, mpis_ous_edges,
                  mpis_cats_edges, mpis_tags_edges,
                  mpis_cats_tags_edges,
                  sel_ctx, sel_ous, sel_ous_ctx,
                  internal=T,
                  overwrite=T)
