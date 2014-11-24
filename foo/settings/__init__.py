from base import *

try:
    from local import *
except:
    pass

try:
    INSTALLED_APPS += ADD_APPS
except:
    pass
