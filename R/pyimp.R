#' Use python environment
#'
#' @export
setpython <- function() {
  reticulate::use_virtualenv(
    system.file("python/env",
      package = "maxplanckr"),
    required = T)
}

#' Prepocess character vector
#'
#' @export
preprocess <- function(title) {
  setpython()
  extract <- reticulate::import_from_path(
    "extract",
    path = system.file("python", package = "maxplanckr"),
    convert = T)
  extract$titles$preprocess$clean(title)
}
