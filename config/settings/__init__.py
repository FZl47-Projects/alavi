from config.settings.base import *
from os import getenv


PRODUCTION = getenv('PRODUCTION', False)

if PRODUCTION:
    from config.settings.production import *
else:
    from config.settings.development import *
