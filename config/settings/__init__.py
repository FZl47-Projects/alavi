from config.settings.base import *
from os import getenv


PRODUCTION = int(getenv('PRODUCTION', 0))

if PRODUCTION:
    from config.settings.production import *
else:
    from config.settings.development import *
