# devtools::load_all()

save_guessed_language_titles <- function(guess, profile = "ECIMCI") {
  guessed_langs <- dplyr::pull(dplyr::distinct(guess, Lang))
  sapply(guessed_langs, function(x) {
    lang_guess <- guess[guess$Lang == x, ]$Label
    c <- tm::VCorpus(tm::VectorSource(paste(lang_guess, collapse = "\n")))
    tm::writeCorpus(
      c, path = file.path(system.file("lnggss", package="maxplanckr"), "txt"),
                    filenames = c(paste(profile, x, "txt", sep = "."))
    )
  })
}

items <- maxplanckr::pure_items

system.time({ # ~20min
  languages_non <- items[items["Lang"] == "", ]
  languages_non$Lang <- sapply(
    languages_non$Label,
    function(x) textcat::textcat(
      x,
      p = textcat::ECIMCI_profiles
    )
  )
  saveRDS(languages_non, file.path(
    system.file("lnggss", package="maxplanckr"),
    "RDS/ECIMCI.RDS"
  ))
  languages_non$Lang <- sapply(
    languages_non$Label,
    function(x) textcat::textcat(
      x,
      p = textcat::TC_byte_profiles
    )
  )
  saveRDS(languages_non, file.path(
    system.file("lnggss", package="maxplanckr"),
    "RDS/TC_byte.RDS"
  ))
  languages_non$Lang <- sapply(
    languages_non$Label,
    function(x) textcat::textcat(
      x,
      p = textcat::TC_char_profiles
    )
  )
  saveRDS(languages_non, file.path(
    system.file("lnggss", package="maxplanckr"),
    "RDS/TC_char.RDS"
  ))
})

guess_ecimci <- readRDS(
  file.path(
    system.file("lnggss", package="maxplanckr"),
    "RDS/ECIMCI.RDS"
  )
)
guess_tc_byte <- readRDS(
  file.path(
    system.file("lnggss", package="maxplanckr"),
    "RDS/TC_byte.RDS"
  )
)
guess_tc_char <- readRDS(
  file.path(
    system.file("lnggss", package="maxplanckr"),
    "RDS/TC_char.RDS"
  )
)

save_guessed_language_titles(guess_ecimci, profile = "ECIMI")
save_guessed_language_titles(guess_tc_byte, profile = "TC_BYTE")
save_guessed_language_titles(guess_tc_char, profile = "TC_CHAR")
