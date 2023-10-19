from config.settings.base import *


PRODUCTION = True


if PRODUCTION:
    from config.settings import production
else:
    from config.settings import dev
