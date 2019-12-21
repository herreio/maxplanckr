devtools::load_all()

pc_titles <- maxplanckr::get_pc_titles()

# //////////////////// #
# /// TITLE SCHEME /// #
# //////////////////// #

titles_eng <- maxplanckr::plain_to_corpus(pc_titles$all_lang_items)
usethis::use_data(titles_eng, overwrite=T)

# //////////////////////// #
# /// INSTITUTE SCHEME /// #
# //////////////////////// #

titles_mpi <- maxplanckr::plain_to_corpus(pc_titles$mpi_lang)
usethis::use_data(titles_mpi, overwrite=T)

# ///////////////////// #
# /// PERSON SCHEME /// #
# ///////////////////// #

titles_pers <- maxplanckr::plain_to_corpus(pc_titles$pers_lang)
usethis::use_data(titles_pers, overwrite=T)
