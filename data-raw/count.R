devtools::load_all()

name_from_path <- function(path) {
  gsub("\\.[a-zA-Z0-9]+$", "", gsub("^.*\\/", "", path))
}

pc_count <- maxplanckr::get_pc_count()

# ///////////////// #
# /// RECORDS /// #
# ///////////// #

fp_rec <- file.path(pc_count$records, "all.csv")

rec <- maxplanckr::read_tsv(fp_rec)
rec <- dplyr::as_tibble(rec)

# ///////////////// #
# /// JOURNALS /// #
# /////////////// #

pc_journals <- list.files(pc_count$journals, pattern=".csv", full.names=T)
jour_ids <- make.names(name_from_path(pc_journals))
pc_journals <- setNames(pc_journals, jour_ids)

jour <- lapply(pc_journals, function(x) {  
  tmp <- maxplanckr::read_tsv(x)
  dplyr::as_tibble(tmp)
})

# ///////////////// #
# /// PERSONS /// #
# ///////////// #

pc_persons <- list.files(pc_count$persons, pattern=".csv", full.names=T)
pers_ids <- make.names(name_from_path(pc_persons))
pc_persons <- setNames(pc_persons, pers_ids)

pers <- lapply(pc_persons, function(x) {
  tmp <- maxplanckr::read_tsv(x)
  dplyr::as_tibble(tmp)
})


sel_stats <- list(rec, jour, pers)
sel_stats <- setNames(sel_stats, c("rec","jour","pers"))

usethis::use_data(sel_stats, overwrite=T)
