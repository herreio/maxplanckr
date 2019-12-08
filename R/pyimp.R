#' Prepocess character vector
#'
#' @export
preprocess <- function(title) {
  reticulate::use_virtualenv(system.file("python/env", package = "maxplanckr"), required = T)
  extract <- reticulate::import_from_path("extract", path = system.file("python", package = "maxplanckr"), convert = T)
  extract$titles$preprocess$clean(title)
}
