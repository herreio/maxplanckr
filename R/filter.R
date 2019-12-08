# //////////////// #
# /// ENTITIES /// #
# //////////////// #

context_names <- function(ctx_ids) {
  sapply(ctx_ids, function(x) pure_ctx[pure_ctx$Id == x, ]$Label)
}

context_maintainer <- function(ctx_idx) {
  sapply(ctx_idx, function(x) pure_ctx_ous[pure_ctx_ous$Source == x,]$Target)
}

orgunit_names <- function(ou_ids) {
  sapply(ou_ids, function(x) pure_ous[pure_ous$Id == x, ]$Label)
}

orgunit_contexts <- function(ou_ids) {
  sapply(ou_ids, function(x) pure_ctx_ous[pure_ctx_ous$Target == x,]$Source)
}

# ////////////////// #
# /// INSTITUTES /// #
# ////////////////// #

institute_tags <- function(ou_ids) {
  sapply(ou_ids, function(x) {
    tag_id <- mpis_tags_edges[mpis_tags_edges$Source == x,]$Target
    mpis_tags[mpis_tags$Id %in% tag_id,]$Label
  })
}

institute_cats <- function(ou_ids) {
  sapply(ou_ids, function(x) {
    cat_id <- mpis_cats_edges[mpis_cats_edges$Source == x,]$Target
    mpis_cats[mpis_cats$Id %in% cat_id,]$Label
  })
}

tags_institutes <- function(tag_name, names=T) {
  tag_id <- mpis_tags[mpis_tags$Label == tag_name,]$Id
  ou_ids <- mpis_tags_edges[mpis_tags_edges$Target==tag_id,]$Source
  mpis_ous[mpis_ous$Id %in% ou_ids,]
}

cats_institutes <- function(cat_name, names=T) {
  cat_id <- mpis_cats[mpis_cats$Label == cat_name,]$Id
  ou_ids <- mpis_cats_edges[mpis_cats_edges$Target==cat_id,]$Source
  mpis_ous[mpis_ous$Id %in% ou_ids,]
}

# //////////////////// #
# /// PUBLICATIONS /// #
# //////////////////// #

orgunit_items <- function(items, ou_ids) {
  institutes_ctx <- as.vector(unlist(orgunit_contexts(ou_ids)))
  items[items$Context %in% institutes_ctx,]
}

search_titles <- function(items, query) {
  items[grepl(query,items$Label, ignore.case = T),]
}

selected_items <- function(items) {
  items[items$Context %in% sel_ctx$Id & items$Lang == "eng",]
}

filter_items <- function(items) {
  items[items$Context %in% mpis_ctx$Id, ]
}
