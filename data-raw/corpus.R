# devtools::load_all()

pc_titles <- maxplanckr::get_pc_titles()

# /////////////////////// #
# /// LANGUAGE SCHEME /// #
# /////////////////////// #

titles_eng <- maxplanckr::lines_to_corpus(file.path(pc_titles$all_lang, "eng.txt"))
usethis::use_data(titles_eng, overwrite=T)
titles_eng_raw <- maxplanckr::lines_to_corpus(file.path(pc_titles$all_lang, "eng_raw.txt"))
usethis::use_data(titles_eng_raw, overwrite=T)
titles_eng_year <- maxplanckr::plain_to_corpus(pc_titles$all_lang_year)
usethis::use_data(titles_eng_year, overwrite=T)
titles_eng_genre <- maxplanckr::plain_to_corpus(pc_titles$all_lang_genre)
usethis::use_data(titles_eng_genre, overwrite=T)
titles_eng_year_genre <- maxplanckr::plain_to_corpus(pc_titles$all_lang_year_genre)
usethis::use_data(titles_eng_year_genre, overwrite=T)

# //////////////////// #
# /// INDEX SCHEME /// #
# //////////////////// #

titles_cat <- maxplanckr::plain_to_corpus(pc_titles$cat_lang)
usethis::use_data(titles_cat, overwrite=T)
titles_cat_year <- maxplanckr::plain_to_corpus(pc_titles$cat_lang_year)
usethis::use_data(titles_cat_year, overwrite=T)
titles_cat_genre <- maxplanckr::plain_to_corpus(pc_titles$cat_lang_genre)
usethis::use_data(titles_cat_genre, overwrite=T)
titles_cat_year_genre <- maxplanckr::plain_to_corpus(pc_titles$cat_lang_year_genre)
usethis::use_data(titles_cat_year_genre, overwrite=T)

# //////////////////////// #
# /// INSTITUTE SCHEME /// #
# //////////////////////// #

titles_mpi <- maxplanckr::plain_to_corpus(pc_titles$mpi_lang)
usethis::use_data(titles_mpi, overwrite=T)
titles_mpi_genre <- maxplanckr::plain_to_corpus(pc_titles$mpi_lang_genre)
usethis::use_data(titles_mpi_genre, overwrite=T)
titles_mpi_year <- maxplanckr::plain_to_corpus(pc_titles$mpi_lang_year)
usethis::use_data(titles_mpi_year, overwrite=T)
titles_mpi_year_genre <- maxplanckr::plain_to_corpus(pc_titles$mpi_lang_year_genre)
usethis::use_data(titles_mpi_year_genre, overwrite=T)

# ///////////////////// #
# /// PERSON SCHEME /// #
# ///////////////////// #

titles_pers <- maxplanckr::plain_to_corpus(pc_titles$pers_lang)
usethis::use_data(titles_pers, overwrite=T)
titles_pers_genre <- maxplanckr::plain_to_corpus(pc_titles$pers_lang_genre)
usethis::use_data(titles_pers_genre, overwrite=T)
titles_pers_year <- maxplanckr::plain_to_corpus(pc_titles$pers_lang_year)
usethis::use_data(titles_pers_year, overwrite=T)
titles_pers_year_genre <- maxplanckr::plain_to_corpus(pc_titles$pers_lang_year_genre)
usethis::use_data(titles_pers_year_genre, overwrite=T)
