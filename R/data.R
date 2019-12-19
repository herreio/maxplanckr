#' Meta data from the Institutional Repository of the Max Planck Society
#'
#' A named list with nodes (contexts, organizational units) and edges between them.
#'
#' @docType data
#'
#' @usage data(pure)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://pure.mpg.de/rest}
"pure"

#' Publications from the Institutional Repository of the Max Planck Society
#'
#' A data.frame (tibble) with more than 390.000 publications.
#'
#' @docType data
#'
#' @usage data(pure_items)
#'
#' @format An object of class \code{"tbl_df"}
#'
#' @source \url{https://pure.mpg.de/rest}
"pure_items"

#' Meta data from the Publications of the Institutional Repository of the Max Planck Society
#'
#' A named list with nodes (publications, sources, persons, organizational units) and edges between them.
#'
#' @docType data
#'
#' @usage data(items)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://pure.mpg.de/rest}
"items"

#' Meta data of Max Planck Institutes
#'
#' A named list with nodes (contexts, organizational units, categories, tags) and edges between them.
#'
#' @docType data
#'
#' @usage data(mpis)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://mpg.de}
"mpis"

#' Meta data of Max Planck Institutes
#'
#' A named list with nodes (contexts, organizational units) and edges between them.
#'
#' @docType data
#'
#' @usage data(sel)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://pure.mpg.de/rest}
"sel"

#' Publications from Max Planck Institutes
#'
#' A data.frame (tibble) with more than 200.000 publications.
#'
#' @docType data
#'
#' @usage data(sel_items)
#'
#' @format An object of class \code{"tbl_df"}
#'
#' @source \url{https://pure.mpg.de/rest}
"sel_items"

#' Meta Data of Publications from Max Planck Institutes
#'
#' A named list with nodes (persons, externals, ous) and edges between them and publication items.
#'
#' @docType data
#'
#' @usage data(sel_items_rel)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://pure.mpg.de/rest}
"sel_items_rel"

#' Sources of Publications from Max Planck Institutes
#'
#' A data.frame (tibble) with more than 200.000 publication sources (JOURNALS, COLLECTED_EDITIONS, ...).
#'
#' @docType data
#'
#' @usage data(sel_items_src)
#'
#' @format An object of class \code{"tbl_df"}
#'
#' @source \url{https://pure.mpg.de/rest}
"sel_items_src"

#' Meta Data of Publication’s Sources from Max Planck Institutes
#'
#' A named list with nodes (persons, externals, ous) and edges between them and publication’s sources.
#'
#' @docType data
#'
#' @usage data(sel_items_src_rel)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://pure.mpg.de/rest}
"sel_items_src_rel"

#' Statistics of Publications from Max Planck Institutes
#'
#' A named list with different count data derived from the publication corpus:
#' records per institute, articles per journal and publications per person.
#'
#' @docType data
#'
#' @usage data(sel_stats)
#'
#' @format An object of class \code{"list"}
#'
#' @source \url{https://pure.mpg.de/rest}
"sel_stats"

#' Documents with English Publication Titles
#'
#' A plain text corpus consisting of more than 220.000 documents with one
#' publication title per document.
#'
#' @docType data
#'
#' @usage data(titles_eng)
#'
#' @format An object of class \code{"VCorpus"}; see \code{\link[tm]{VCorpus}}.
#'
#' @source \url{https://pure.mpg.de/rest}
"titles_eng"

#' Documents with English Publication Titles from Max Planck Institutes
#'
#' A plain text corpus consisting of 73 documents with publication titles
#' from different Max Planck Institutes
#'
#' @docType data
#'
#' @usage data(titles_mpi)
#'
#' @format An object of class \code{"VCorpus"}; see \code{\link[tm]{VCorpus}}.
#'
#' @source \url{https://pure.mpg.de/rest}
"titles_mpi"

#' Documents with English Publication Titles from Scientists of Max Planck Institutes
#'
#' A plain text corpus consisting of more than 30.000 documents with publication titles
#' from different scientists of Max Planck Institutes
#'
#' @docType data
#'
#' @usage data(titles_pers)
#'
#' @format An object of class \code{"VCorpus"}; see \code{\link[tm]{VCorpus}}.
#'
#' @source \url{https://pure.mpg.de/rest}
"titles_pers"
