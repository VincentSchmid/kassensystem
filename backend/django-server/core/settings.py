"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import environ
import dj_database_url
from datetime import timedelta

env = environ.Env(
    DJANGO_ENVIRONMENT=(str, "dev"),
    DJANGO_DEBUG=(bool, True),
    DJANGO_SUPERUSER_USERNAME=(str, "admin"),
    DJANGO_SUPERUSER_PASSWORD=(str, "admin"),
    DJANGO_SUPERUSER_EMAIL=(str, "admin@admin.ch"),
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
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "storages",
    "authentication",
    "domain.product_catalogue",
    "domain.pos",
]

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

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Point of Sale API",
    "DESCRIPTION": "point of sale system",
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": "/api/v[0-9]/[a-zA-Z0-9-_]*/",
    "SERVE_INCLUDE_SCHEMA": False,
}

ADMIN = {
    "USERNAME": env("DJANGO_SUPERUSER_USERNAME"),
    "EMAIL": env("DJANGO_SUPERUSER_EMAIL"),
    "PASSWORD": env("DJANGO_SUPERUSER_PASSWORD"),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer"),
}
