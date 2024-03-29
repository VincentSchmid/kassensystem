"""
Django 4.0.5.

"""

from pathlib import Path
import environ
from enum import Enum
import sys
from datetime import timedelta

import dj_database_url


env = environ.Env(
    DJANGO_ENVIRONMENT=(str, "dev"),
    DJANGO_DEBUG=(bool, True),
    JWT_ACCESS_TOKEN_LIFETIME_MINUTES=(int, 120),
    JWT_REFRESH_TOKEN_LIFETIME_DAYS=(int, 1),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR.joinpath(".env"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = "django-insecure-yjon%!*t6=x9-+3$h#j$_)2d@@!9=u(nzq-0w1b&7i@!8s)9-!"
else:
    SECRET_KEY = env("DJANGO_SECRET_KEY")

# Application definition

INSTALLED_APPS = [
    "account",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "ninja_extra",
    "ninja_jwt",
    "storages",
    "authentication",
    "domain.product_catalogue",
    "domain.pos",
    "domain.employee",
]

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"
CORS_URLS_REGEX = r"^/api/.*$"

if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_ALLOW_ALL = True
else:
    ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOST").split(",")
    CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(",")
    CORS_ALLOWED_ORIGINS = env("DJANGO_CORS_ALLOWED_ORIGIN").split(",")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(conn_max_age=600)}

if "test" in sys.argv:
    DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Zurich"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if DEBUG:
    STATIC_ROOT = BASE_DIR.joinpath("static")
    STATIC_URL = "static/"
else:
    DEFAULT_FILE_STORAGE = "core.custom_azure.AzureMediaStorage"
    STATICFILES_STORAGE = "core.custom_azure.AzureStaticStorage"

    STATIC_LOCATION = "static"
    MEDIA_LOCATION = "media"

    AZURE_ACCOUNT_NAME = env("AZURE_ACCOUNT_NAME")
    AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
    STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Groups
class Groups(Enum):
    WAITER: str = "Waiter"
    MANAGER: str = "Manager"


GROUPS = {Groups.WAITER.value: [], Groups.MANAGER.value: []}

AUTH_USER_MODEL = "account.Account"

NINJA_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=env("JWT_ACCESS_TOKEN_LIFETIME_MINUTES")
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=env("JWT_REFRESH_TOKEN_LIFETIME_DAYS")),
}
