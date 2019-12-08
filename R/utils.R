# -------------- #
# -- CSV I/O -- #
# ------------ #

read_csv <- function(fp) {
  csv <- read.csv(fp,
                  sep = ",",
                  quote = '"',
                  header = T,
                  encoding = "UTF-8",
                  stringsAsFactors = F)
  return(csv)
}

read_data <- function(fp) {
  csv <- read_csv(fp)
  dplyr::as_tibble(csv)
}
