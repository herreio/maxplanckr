# ----------------- #
# -- CORPUS I/O -- #
# --------------- #

#' Collect paths of plain texts
#'
#' @export
plain_paths <- function(fp, fpattern = ".txt", full = T, ftype = T) {
  cat("collecting file names...\n")
  raw_src <- tm::DirSource(fp, pattern = fpattern)
  raw_src$filelist <- grep(raw_src$filelist, pattern="raw.txt|.csv", inv=T, value=T)
  raw_src$length <- length(raw_src$filelist)
  if(full) { raw_src } else {
    fname <- sapply(strsplit(raw_src$filelist, "/"),
                    function(x) x[[length(x)]])
    if (ftype) { fname } else {
      sapply(strsplit(fname, ".", fixed = T), function(x) x[[1]])
    }
  }
}

#' Create corpus from directory containing plain text files
#'
#' @export
plain_to_corpus <- function(fp, fpattern = ".txt") {
  raw_src <- plain_paths(fp, fpattern=fpattern)
  cat("read files and create corpus...\n")
  return(tm::VCorpus(raw_src))
}

#' Read single file and create corpus (1 line, 1 doc)
#'
#' @export
lines_to_corpus <- function(fp) {
  cat("read file and create corpus...\n")
  lines <- readLines(fp)
  corpus <- tm::VCorpus(tm::VectorSource(lines))
  cat("success!\n")
  return(corpus)
}

#' Read single file and create corpus (1 line, 1 doc)
#'
#' @export
lines_to_dtm <- function(fp) {
  corpus <- lines_to_corpus(fp)
  #cat("read file and create corpus...\n")
  #lines <- readLines(fp)
  #corpus <- tm::VCorpus(tm::VectorSource(lines))
  cat("create document term matrix...\n")
  dtm <- tm::DocumentTermMatrix(corpus)
  dtm <- dtm[slam::row_sums(dtm) > 0, ]
  cat("success!\n")
  return(dtm)
}

#' Create document term matrix from directory containing plain text files
#'
#' @export
plain_to_dtm <- function(fp, fpattern = ".txt") {
  corpus <- plain_to_corpus(fp, fpattern = fpattern)
  cat("create document term matrix...\n")
  dtm <- tm::DocumentTermMatrix(corpus)
  dtm <- dtm[slam::row_sums(dtm) > 0, ]
  cat("success!\n")
  return(dtm)
}

# docterm_csv <- function(fp, fpattern = ".csv") {
#   cat("collecting file names...\n")
#   fpaths <- list.files(fp, pattern=fpattern, full.names=TRUE)
#   cat("read files and create corpus...\n")
#   list_docterm <- lapply(fpaths, function(x) { read_docterm(x) })
#   docterm <- list_docterm[[1]]
#   if (length(list_docterm) > 1) {
#     n <- 2:length(list_docterm)
#     for(i in n) { docterm <- dplyr::bind_rows(docterm, list_docterm[[i]]) }
#   }
#   cat("success!\n")
#   return(docterm)
# }
# 
# read_docterm <- function(x) {
#   readr::read_delim(
#     x,
#     ",",
#     escape_double = FALSE,
#     col_types = readr::cols(
#       Doc = col_character(),
#       Term = col_character()),
#     trim_ws = TRUE
#   )
# }
# 
