filter_items <- function(items) {
  items[items$Context %in% mpis_ctx$Id, ]
}

search_titles <- function(items, query) {
  items[grepl(query,items$Label, ignore.case = T),]
}

context_names <- function(ctx_idx) {
  as.character(sapply(
    as.character(ctx_idx),
    function(x) pure_ctx[pure_ctx$Id == x, ]$Label
  ))
}

context_maintainer <- function(ctx_idx) {
  as.character(sapply(
    as.character(ctx_idx),
    function(x) pure_ctx_ous[pure_ctx_ous$Source == x,]$Target
  ))
}

orgunit_contexts <- function(ou_idx) {
  sapply(as.character(ou_idx),
    function(x) pure_ctx_ous[pure_ctx_ous$Target == x,]$Source)
}

orgunit_items <- function(items, ou_idx) {
  institutes_ctx <- as.vector(unlist(orgunit_contexts(ou_idx)))
  dplyr::filter(items, Context %in% institutes_ctx)
}

selected_items <- function(items) {
  dplyr::filter(items, Context %in% sel_ctx$Id & Lang == "eng")
}

institute_tags <- function(ou_idx) {
  tag_id <- dplyr::filter(mpis_tags_edges, Source==ou_idx)$Target
  dplyr::filter(mpis_tags, Id %in% tag_id)$Label
}

tags_institutes <- function(tag_name, names=T) {
  tag_id <- dplyr::filter(mpis_tags, Label==tag_name)$Id
  ou_id <- dplyr::filter(mpis_tags_edges, Target==tag_id)$Source
}
