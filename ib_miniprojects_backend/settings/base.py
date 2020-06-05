"""
Django settings for ib_miniprojects_backend project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development conf - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


ALLOWED_HOSTS = [
    "ib-miniprojects-backend-prod.apigateway.in",
    "ib-miniprojects-backend-alpha.apigateway.in",
    "ib-miniprojects-backend-beta.apigateway.in",
    "ib-miniprojects-backend-gamma.apigateway.in",
    "127.0.0.1",
    "localhost",
    "*"
]

ROOT_URLCONF = 'ib_miniprojects_backend.urls'

CSRF_COOKIE_SECURE = False

WSGI_APPLICATION = 'ib_miniprojects_backend.wsgi.application'

SCRIPT_NAME = "/" + os.environ.get("STAGE", "alpha")

################## CORS #####################

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1',
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'x-api-key',
    'x-source'
)
#*************** Internationalization *******************#
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


from ib_common.logger.log_custom_formatter import LogCustomFormatter

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        },
        'user_id': {
            '()': 'django_swagger_utils.logger.log_filters.UserIDFilter'
        },
        'path_info': {
            '()': 'ib_common.logger.log_filters.PathInfoFilter'
        },
        'aws_request_id': {
            '()': 'ib_common.logger.log_filters.AWSRequestIdFilter'
        },
        'stage': {
            '()': 'ib_common.logger.log_filters.StageFilter'
        },
        'operation_id': {
            '()': 'django_swagger_utils.logger.log_filters.OperationIdFilter'
        },
        'app_name': {
            '()': 'django_swagger_utils.logger.log_filters.AppNameFilter'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            "filters": ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage", "operation_id", "app_name"]
        },
        'logentries': {
            'level': 'DEBUG',
            'token': os.environ.get('LE_TOKEN', ''),
            'class': 'logentries.LogentriesHandler',
            'formatter': 'le_console',
            "filters": ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage", "operation_id", "app_name"],
        },
        'logentries_200': {
            'level': 'DEBUG',
            'token': os.environ.get('LE_200_TOKEN', ''),
            'class': 'logentries.LogentriesHandler',
            'formatter': 'le_console',
            "filters": ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage", "operation_id", "app_name"],
        },
        'logentries_non_200': {
            'level': 'DEBUG',
            'token': os.environ.get('LE_NON_200_TOKEN', ''),
            'class': 'logentries.LogentriesHandler',
            'formatter': 'le_console',
            "filters": ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage", "operation_id", "app_name"],
        },
        'logentries_non_api': {
            'level': 'DEBUG',
            'token': os.environ.get('LE_NON_API_TOKEN', ''),
            'class': 'logentries.LogentriesHandler',
            'formatter': 'le_console',
            "filters": ["request_id", "user_id", "path_info",
                        "aws_request_id", "stage", "operation_id", "app_name"],
        }
    },
    'formatters': {
        'le_console': {
            '()': LogCustomFormatter,
        },
        'console': {
            'format': "[%(request_id)s] [ib_miniprojects_backend - "+os.environ.get("STAGE", "local")+
                      '] %(levelname)-8s [%(asctime)s]  '
                      '[%(pathname)s] [%(filename)s]'
                      '[%(funcName)s] [%(lineno)d]: %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logentries'],
            'level': 'INFO',
            'propagate': False,
        },
        'dsu.error': {
            'handlers': ['console', 'logentries'],
            'level': 'ERROR',
            'propagate': False,
        },
        'dsu.debug': {
            'handlers': ['console', 'logentries'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'LogAPI200': {
            'handlers': ['logentries_200', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'LogAPINON200': {
            'handlers': ['logentries_non_200', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'LogNONAPI': {
            'handlers': ['logentries_non_api', ],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
# ********************** Installed Apps ****************************

INSTALLED_APPS = [
    'django.contrib.admin',  # admin interface
    'django.contrib.auth',  # django authentication
    'django.contrib.contenttypes',  # response content types used in admin
    'django.contrib.sessions',  # django sessions used in admin
    'django.contrib.messages',  # info, success, error message in response. admin requires this
    'django.contrib.staticfiles',  # host the static files
]

THIRD_PARTY_APPS_BASE = [
    # oauth
    # 'oauth',
    'oauth2_provider',
    # aws storage
    'storages',
    # django rest framework
    'rest_framework',
    'rest_framework_xml',  # xml renderers, parsers
    'corsheaders',

    # CUSTOM APPS
    'django_swagger_utils',

    # django fine uploader
    'django_fine_uploader_s3',

]
INSTALLED_APPS += THIRD_PARTY_APPS_BASE

# ********************** Password Validators ***************************
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# ************************* Django Rest Framework ******************************
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework.renderers.AdminRenderer',
    ),
    'EXCEPTION_HANDLER': 'django_swagger_utils.drf_server.exceptions.drf_custom_exception.custom_exception_handler'
}

# ************************** Templates ******************************
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# *********************** Middleware *************************#

MIDDLEWARE = [
    'log_request_id.middleware.RequestIDMiddleware',  # request logging
    'django_swagger_utils.middlewares.reset_dsu_data_middleware.ResetDSUDataMiddleware',
    # 'ib_sentry_wrapper.utils.response_status_code_4xx_5xx_middleware.ResponseStatusCode4xx5xxMiddleware',
    # 'ib_sentry_wrapper.utils.request_id_middleware.RequestIdMiddleware',
    # 'ib_sentry_wrapper.utils.dsu_data_middleware.DSUDataMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # django sessions, usefull in admin
    'corsheaders.middleware.CorsMiddleware',  # cors headers middleware
    'django.middleware.common.CommonMiddleware',
    # handling the url redirect, adding / in the end of url.
    # ref https://docs.djangoproject.com/en/1.9/ref/middleware/#django.middleware.common.CommonMiddleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # set request.user value after authenticating
    'django.contrib.messages.middleware.MessageMiddleware',
    # messaging framework middleware, django admin requires this
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # save from clickjack attack ref https://docs.djangoproject.com/en/1.9/ref/clickjacking/
    'django.middleware.locale.LocaleMiddleware',
]

### api log config

MIDDLEWARE.insert(0, 'ib_common.logger.log_filters_middleware.LogFiltersMiddleware')

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('te', _('Telugu')),
    ('hi', _('Hindi')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

OTP_LIMIT = int(os.environ.get('OTP_LIMIT', 4))
SMSCOUNTRY_USERNAME = os.environ.get('SMSCOUNTRY_USERNAME', '')
SMSCOUNTRY_PASSWORD = os.environ.get('SMSCOUNTRY_PASSWORD', '')
SMSCOUNTRY_DEFAULT_SENDER_ID = os.environ.get('SMSCOUNTRY_DEFAULT_SENDER_ID', 'IBHUBS')

# sms & email
import base64

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = str(os.environ.get("EMAIL_HOST", ""))
EMAIL_PORT = str(os.environ.get("EMAIL_PORT", ""))
EMAIL_HOST_USER = str(os.environ.get("EMAIL_HOST_USER", ""))
EMAIL_HOST_PASSWORD = base64.b64decode(os.environ.get("EMAIL_HOST_PASSWORD", "")).decode("utf-8")
EMAIL_USE_TLS = str(os.environ.get("EMAIL_USE_TLS", ""))
DEFAULT_SENDER_EMAIL = str(os.environ.get("DEFAULT_SENDER_EMAIL", ""))

# ****************** App Source Config ******************
IB_MINIPROJECTS_BACKEND_SOURCE = "ib-miniprojects-backend-source"

# test runner setting
TEST_RUNNER = 'snapshottest.django.TestRunner'
MOCK_X_IB_REQUEST_ID = True

STAGE = os.environ.get("STAGE", "local")