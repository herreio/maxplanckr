# devtools::load_all()

pc_tables <- maxplanckr::get_pc_tables()

# ///////////// #
# /// ITEMS /// #
# ///////////// #

pure_items <- maxplanckr::read_data(pc_tables$publications)
pure_items$Year <- gsub("-.+", "", pure_items$Year)
pure_items$Year <- as.integer(pure_items$Year)
usethis::use_data(pure_items, overwrite=T)

# ///////////////// #
# /// SELECTION /// #
# ///////////////// #

sel_items <- maxplanckr::selected_items(pure_items)
usethis::use_data(sel_items, overwrite=T)
