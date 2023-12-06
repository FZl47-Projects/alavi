from config.settings.base import BASE_DIR
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.getenv("SQLITE_PATH", "db.sqlite3"),
    }
}
