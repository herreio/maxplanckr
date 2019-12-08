devtools::load_all() # library(bsc)

pure_items <- read_csv(pc_tables$publications)
pure_items <- dplyr::as_tibble(pure_items)
pure_items$Year <- gsub("-.+", "", pure_items$Year)
pure_items$Year <- as.integer(pure_items$Year)
usethis::use_data(pure_items)

items <- selected_items(pure_items)
usethis::use_data(items)
