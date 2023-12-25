from django.utils.translation import gettext_lazy as _
from pathlib import Path

import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-#*g^+y5-plch-=q=@yre0go(@er5diu*!poca-()#p01*1#$qq')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

HOST_ADDRESS = os.getenv('HOST_ADDRESS', 'http://127.0.0.1:8000').split(',')

CSRF_TRUSTED_ORIGINS = [*HOST_ADDRESS]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'django_q',
    'ckeditor',
    'phonenumber_field',
    'nested_admin',

    # Apps
    'apps.account',
    'apps.core',
    'apps.public',
    'apps.diet',
    'apps.exercise',
    'apps.package',
    'apps.notification',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGES = [
    ('fa', _("Persian")),
]

LOCALE_PATHS = [
    os.getenv('LOCALE_PATHS', BASE_DIR / 'locale'),
]

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.getenv('STATIC_ROOT')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.getenv('MEDIA_ROOT', BASE_DIR / 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'
LOGIN_URL = '/u/login-register'

TIME_INPUT_FORMATS = [
    '%H:%M',
]

SUPER_ADMIN_ROLES = [
    'super_user'
]
ADMIN_USER_ROLES = [
    *SUPER_ADMIN_ROLES
]
USER_ROLES = [
    'normal_user',
]

IMAGE_FORMATS = [
    'jpg',
    'png'
]

Q_CLUSTER = {
    'name': 'django-q',
    'timeout': int(os.getenv('Q_CLUSTER_TIMEOUT', 60)),
    'orm': os.getenv('Q_CLUSTER_ORM', 'default'),
}

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

REDIS_CONFIG = {
    'HOST': os.getenv('REDIS_HOST', 'localhost'),
    'PORT': os.getenv('REDIS_PORT', '6379')
}

RESET_PASSWORD_CONFIG = {
    'TIMEOUT': int(os.getenv('RESET_PASS_CONFIG_TIMEOUT', 60)),  # by sec
    'CODE_LENGTH': int(os.getenv('RESET_PASS_CONFIG_CODE_LENGTH', 6)),
    'STORE_BY': 'reset_password_phonenumber_{}'
}


# Email backend config
EMAIL_SUBJECT = f'اعلان از طرف سامانه علوی '
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_USER', 'fzl47.projects@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', 'zrqxdunuaorfagaq')

# SMS configurations
SMS_CONFIG = {
    'API_KEY': os.getenv('SMS_CONFIG_API_KEY', 'ml23kKIXh-JXCBNfbs-6DWnU1ZaBJuVxcZGjLRnggvs='),
    'API_URL': os.getenv('SMS_CONFIG_API_URL', 'http://rest.ippanel.com/v1/messages/patterns/send'),
    'ORIGINATOR': os.getenv('SMS_CONFIG_ORIGINATOR', '983000505')
}
