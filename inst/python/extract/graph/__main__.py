import time

from . import contexts
from . import contexts_mpis
from . import contexts_sel
from . import ous
from . import ous_mpis
from . import ous_sel
from . import persons
from . import descriptor
from . import languages

print("start extraction of graph!")

start_time = time.time()

# //////////////// #
# /// CONTEXTS /// #
# //////////////// #

contexts.routine()
contexts_mpis.routine()
contexts_sel.routine()

# ///////////////////// #
# /// ORGANIZATIONS /// #
# ///////////////////// #

ous.routine()
ous_mpis.routine()
ous_sel.routine()

# /////////////// #
# /// PERSONS /// #
# /////////////// #

persons.routine()

# /////////////////// #
# /// DESCRIPTION /// #
# /////////////////// #

descriptor.routine()

# ///////////////// #
# /// LANGUAGES /// #
# ///////////////// #

languages.routine()

# ///////////// #

print("finished extraction after %s sec!" % round(time.time() - start_time, 2))
