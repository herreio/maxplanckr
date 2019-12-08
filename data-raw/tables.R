# devtools::load_all()

pc_tables <- maxplanckr::get_pc_tables()
pure_items <- maxplanckr::read_csv(pc_tables$publications)
pure_items <- dplyr::as_tibble(pure_items)
pure_items$Year <- gsub("-.+", "", pure_items$Year)
pure_items$Year <- as.integer(pure_items$Year)
usethis::use_data(pure_items, overwrite=T)

sel_items <- selected_items(pure_items)
usethis::use_data(sel_items, overwrite=T)
