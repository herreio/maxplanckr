#' Read csv function
#'
#' @export
read_csv <- function(fp) {
  csv <- utils::read.csv(fp,
                  sep = ",",
                  quote = '"',
                  header = T,
                  encoding = "UTF-8",
                  stringsAsFactors = F)
  return(csv)
}

#' Read csv as tibble function
#'
#' @export
read_data <- function(fp) {
  csv <- read_csv(fp)
  dplyr::as_tibble(csv)
}

#' Read tsv function
#'
#' @export
read_tsv <- function(fp) {
    utils::read.csv(fp,
        sep = "\t",
        quote = "",
        header = T,
        encoding = "UTF-8",
        stringsAsFactors = F
    )
}
