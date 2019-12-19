devtools::load_all()

pc_titles <- maxplanckr::get_pc_titles()

# /////////////////////// #
# /// LANGUAGE SCHEME /// #
# /////////////////////// #

titles_eng <- maxplanckr::lines_to_corpus(file.path(pc_titles$all_lang, "eng.txt"))
usethis::use_data(titles_eng, overwrite=T)
titles_eng_raw <- maxplanckr::lines_to_corpus(file.path(pc_titles$all_lang, "eng_raw.txt"))

fp <- file.path(system.file("extdata", package="maxplanckr"), "titles_eng_raw.rda")
save(titles_eng_raw, fp)
# usethis::use_data(titles_eng_raw, overwrite=T)

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
