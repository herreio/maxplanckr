import os
import sys
import time

from . import cone_jour
from . import cone_lang
from . import cone_pers
from . import pure_ctx
from . import pure_ous
from . import pure_item

from .utils_paths import LOG_DIR

print("console output is redirected to retrieve.log ...")

stdout = sys.stdout
sterr = sys.stderr

log = open(os.path.join(LOG_DIR, "retrieve.log"), "w+")
sys.stdout = log
sys.stderr = log

print("start retrieval!")

start_time = time.time()

# ///////////////// #
# /// JOURNALS /// #
# /////////////// #

print("retrieve journals!")
cone_jour.routine()
print("done retrieving journals!")
print("")

# ////////////////// #
# /// LANGUAGES /// #
# //////////////// #

print("retrieve languages!")
cone_lang.routine()
print("done retrieving languages!")
print("")

# //////////////// #
# /// PERSONS /// #
# ////////////// #

print("retrieve persons!")
cone_pers.routine()
print("done retrieving persons!")
print("")

# ///////////////// #
# /// CONTEXTS /// #
# /////////////// #

print("retrieve contexts!")
pure_ctx.routine()
print("done retrieving contexts!")
print("")

# ////////////////////// #
# /// ORGANIZATIONS /// #
# //////////////////// #

print("retrieve organizational units!")
pure_ous.routine()
print("done retrieving organizational units!")
print("")

# ///////////////////// #
# /// PUBLICATIONS /// #
# /////////////////// #

print("retrieve items from contexts!")
pure_item.routine()
print("done retrieving items from contexts!")
print("")

# ///////////// #

fin_time = time.time()
print("finished retrieval after %s sec!" % round(fin_time - start_time, 2))
print("")

log.close()
sys.stdout = stdout
sys.stderr = stderr

print("finished retrieval after %s sec!" % round(fin_time - start_time, 2))
