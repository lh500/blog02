"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bm2bwyde7-k0(=$-1f7gl(wf*4*0-_3c1((pbc5deznj$!*q*m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

COMPRESS_ENABLED = True
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',)

# Application definition


INSTALLED_APPS = [
    # 'simplepro',
    'simpleui',
    # 'import_export'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'models',
    'article',
    'mdeditor',
    'myblog.templatetags',
    'haystack',
    'compressor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'myblog.mymiddleware.SimpleMiddleware',
    # 加入simplepro的中间件
    # 'simplepro.middlewares.SimpleMiddleware'
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'common_tag': 'myblog.templatetags.common',
            }
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog02',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'OPTIONS': {'charset': 'utf8mb4'},
        # 'CONN_MAX_AGE': 600
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
COMPRESS_ROOT = STATIC_ROOT
UEDITOR_UPLOAD_PREFIX = "/static/upload/"
UEDITOR_UPLOAD_DIR = os.path.join(BASE_DIR, 'static/upload/')

# 文件不上传阿里云 注释掉DEFAULT_FILE_STORAGE
# mediafile将自动上传
DEFAULT_FILE_STORAGE = 'aliyun.oss_backends.AliyunStorage'
# staticfile将自动上传
# STATICFILES_STORAGE = 'aliyun.oss_backends.AliyunStorage'

# GitHub
GITHUB_CLIENT_ID = 'c233704c664cd1059401'
GITHUB_CLIENT_SECRET = 'c3791ed0ae599d87ece527595362e3f6e3e20f96'
GITHUB_CLIENT_CALLBACK = '/oauth/github/callback'

# QQ
QQ_CLIENT_ID = '101071455'
QQ_CLIENT_SECRET = '588b4f9300ce23968a73d22bb9a90a38'
QQ_CLIENT_CALLBACK = '/oauth/qq/callback'

# 代码集市
# SEEJOKE_CLIENT_ID = '68117296551460865'
# SEEJOKE_CLIENT_SECRET = 'cb431343628c4b6fb10b51d17c164796'
SEEJOKE_CLIENT_CALLBACK = '/oauth/seejoke/callback'

SEEJOKE_CLIENT_ID = '69343595613814785'
SEEJOKE_CLIENT_SECRET = '1898750ee24343e7b4b92b6dd278eb49'

# 全文检索配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'myblog.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        'INCLUDE_SPELLING': True
    }
}
HAYSTACK_DEFAULT_OPERATOR = 'OR'
# 添加此项，当数据库改变时，会自动更新索引，非常方便
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

# redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

# 首页配置
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
SIMPLEUI_HOME_TITLE = '百度一下你就知道'
SIMPLEUI_HOME_ICON = 'layui-icon-rate'