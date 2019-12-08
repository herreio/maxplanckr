import re

from .stopwords import get_stopwords

from ..utils.clean import clean_title

stop = get_stopwords('smart')

latex = re.compile(r"\\bold|\\widehat|\\overline|\\times|\\sqrt|\\log|\\rightarrow|\\vert|\\Bbb")
latex_math = re.compile(r"[^a-z\s]?\$.+?\$[^a-z\s]?")
roman = re.compile(r"\b[ivx]+\b")
punct = re.compile(r"[^\w\s]")
chars = re.compile(r"[^a-z]")


def clean(title):
    title = clean_title(title)
    title = title.lower()
    title = latex.sub(" ", title)
    title = latex_math.sub(" ", title)
    title = roman.sub(" ", title)
    title = punct.sub(" ", title)
    title = remove_numbers(title)
    title = remove_stopwords(title)
    title = remove_nonascii(title)
    title = remove_short(title)
    title = re.sub(r"\s+", " ", title)
    title = title.strip()
    return title


def remove_stopwords(title):
    return " ".join([word for word in title.split() if word not in stop])


def remove_short(title):
    return " ".join([word for word in title.split() if len(word) > 2])


def remove_nonascii(title):
    return " ".join([word for word in title.split() if word == chars.sub(" ", word)])


def remove_numbers(title):
    return " ".join([word for word in title.split() if not has_number(word)])


def has_number(word):
    return any(i.isdigit() for i in word)
