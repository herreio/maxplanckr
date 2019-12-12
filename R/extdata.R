#' @export
get_dp_graph <- function() {
  system.file("extdata/prepared/graph", package="maxplanckr")
}

#' @export
get_dp_tables <- function() {
  system.file("extdata/prepared/tables", package="maxplanckr")
}

#' @export
get_dp_titles <- function() {
  system.file("extdata/prepared/titles", package="maxplanckr")
}

#' @export
get_pc_graph <- function() {
  dp_graph <- get_dp_graph()
  data.frame(
    "items_nodes_pub" = file.path(dp_graph, "items--pub-nodes.csv"),
    "items_nodes_ous" = file.path(dp_graph, "items--ous-nodes.csv"),
    "items_nodes_pers" = file.path(dp_graph, "items--pers-nodes.csv"),
    "items_nodes_pers_ous" = file.path(dp_graph, "items--pers-ous-nodes.csv"),
    "items_nodes_ext" = file.path(dp_graph, "items--ext-nodes.csv"),
    "items_nodes_ext_ous" = file.path(dp_graph, "items--ext-ous-nodes.csv"),
    "items_nodes_src_ous" = file.path(dp_graph, "items--src-ous-nodes.csv"),
    "items_nodes_src_pers" = file.path(dp_graph, "items--src-pers-nodes.csv"),
    "items_nodes_src_pers_ous" = file.path(dp_graph, "items--src-pers-ous-nodes.csv"),
    "items_nodes_src_ext" = file.path(dp_graph, "items--src-ext-nodes.csv"),
    "items_nodes_src_ext_ous" = file.path(dp_graph, "items--src-ext-ous-nodes.csv"),
    "items_edges_pub_ous" = file.path(dp_graph, "items--pub-ous-edges.csv"),
    "items_edges_pub_pers" = file.path(dp_graph, "items--pub-pers-edges.csv"),
    "items_edges_pub_ext" = file.path(dp_graph, "items--pub-ext-edges.csv"),
    "items_edges_pers_ous" = file.path(dp_graph, "items--pers-ous-edges.csv"),
    "items_edges_ext_ous" = file.path(dp_graph, "items--ext-ous-edges.csv"),
    "items_edges_src_ext" = file.path(dp_graph, "items--src-ext-edges.csv"),
    "items_edges_src_ext_ous" = file.path(dp_graph, "items--src-ext-ous-edges.csv"),
    "items_edges_src_ous" = file.path(dp_graph, "items--src-ous-edges.csv"),
    "items_edges_src_pers" = file.path(dp_graph, "items--src-pers-edges.csv"),
    "items_edges_src_pers_ous" = file.path(dp_graph, "items--src-pers-ous-edges.csv"),
    "mpis_nodes_ous" = file.path(dp_graph, "mpis--ous_nodes.csv"),
    "mpis_nodes_cats" = file.path(dp_graph, "mpis--cats_nodes.csv"),
    "mpis_nodes_tags" = file.path(dp_graph, "mpis--tags_nodes.csv"),
    "mpis_nodes_ctx" = file.path(dp_graph, "mpis--ctx_nodes--ous.csv"),
    "mpis_nodes_ous_cat" = file.path(dp_graph, "mpis--ous_nodes--cats.csv"),
    "mpis_nodes_ous_ctx" = file.path(dp_graph, "mpis--ous_nodes--ctx.csv"),
    "mpis_nodes_ous_tree_full" = file.path(dp_graph, "mpis--ous_nodes--tree-full.csv"),
    "mpis_nodes_ous_tree_children" = file.path(dp_graph, "mpis--ous_nodes--tree-children.csv"),
    "mpis_edges_ous_ctx" = file.path(dp_graph, "mpis--ous_ctx_edges.csv"),
    "mpis_edges_ous_ous" = file.path(dp_graph, "mpis--ous_ous_edges--tree.csv"),
    "mpis_edges_ous_cats" = file.path(dp_graph, "mpis--ous_cat_edges.csv"),
    "mpis_edges_ous_tags" = file.path(dp_graph, "mpis--ous_tags_edges.csv"),
    "mpis_edges_cats_tags" = file.path(dp_graph, "mpis--cats-tags_edges.csv"),
    "pure_nodes_ctx" = file.path(dp_graph, "pure--ctx_nodes.csv"),
    "pure_nodes_jour" = file.path(dp_graph, "pure--jour_nodes.csv"),
    "pure_nodes_lang" = file.path(dp_graph, "pure--lang_nodes.csv"),
    "pure_nodes_ous" = file.path(dp_graph, "pure--ous_nodes.csv"),
    "pure_nodes_pers" = file.path(dp_graph, "pure--pers_nodes.csv"),
    "pure_edges_ous_ous" = file.path(dp_graph, "pure--ous_ous_edges.csv"),
    "pure_edges_ctx_ous" = file.path(dp_graph, "pure--ctx_ous_edges.csv"),
    "pure_edges_pers_ous" = file.path(dp_graph, "pure--pers_ous_edges.csv"),
    "sel_nodes_ctx" = file.path(dp_graph, "sel--ctx_nodes.csv"),
    "sel_nodes_ous" = file.path(dp_graph, "sel--ous_nodes.csv"),
    "sel_nodes_ous_tree" = file.path(dp_graph, "sel--ous_nodes--tree.csv"),
    "sel_nodes_ous_kids" = file.path(dp_graph, "sel--ous_nodes--children.csv"),
    "sel_edges_ous_ctx" = file.path(dp_graph, "sel--ous_ctx_edges.csv"),
    "sel_edges_ous_ous" = file.path(dp_graph, "sel--ous_ous_edges.csv"),
    stringsAsFactors = F
  )
}

#' @export
get_pc_tables <- function() {
  dp_tables <- get_dp_tables()
  data.frame(
    "publications" = file.path(dp_tables, "publications.csv"),
    "authors" = file.path(dp_tables, "publications_authors.csv"),
    "externals" = file.path(dp_tables, "publications_externals.csv"),
    "organizations" = file.path(dp_tables, "publications_organizations.csv"),
    "sources" = file.path(dp_tables, "publications_sources.csv"),
    "sources_authors" = file.path(dp_tables, "publications_sources_authors.csv"),
    "sources_externals" = file.path(dp_tables, "publications_sources_externals.csv"),
    "sources_organizations" = file.path(dp_tables, "publications_sources_organizations.csv"),
    stringsAsFactors = F
  )
}

#' @export
get_pc_titles <- function() {
  dp_titles <- get_dp_titles()
  data.frame(
    "all_lang" = file.path(dp_titles, "all-lang"),
    "mpi_lang" = file.path(dp_titles, "mpi-lang"),
    "pers_lang" = file.path(dp_titles, "pers-lang"),
    stringsAsFactors = F
  )
}
