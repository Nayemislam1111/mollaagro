"""
Django settings for mulla_agro project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-x+ghq@x-5$a$p@3j-_*qk&9=e@_9+r5x@v+hkfm+dv7lsr-he!'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'unfold',  # Django Unfold Modern Theme (প্রিমিয়াম লুকের জন্য সবার উপরে রাখা হলো)
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Apnar toiri kora app
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

ROOT_URLCONF = 'mulla_agro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mulla_agro.wsgi.application'


# Database (PostgreSQL Configuration)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mulla_agro_db',
        'USER': 'postgres',      # Apnar PostgreSQL username
        'PASSWORD': '1234', # Apnar PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'  # Bangladesh time zone

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Media files (Product Images Upload-er jonno)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# লগইন এবং লগআউটের পর হোমপেজে রিডাইরেক্ট করার জন্য
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# ==========================================
# Django Unfold Theme Customization
# ==========================================
UUNFOLD = {
    "SITE_TITLE": "Molla Agro Admin",
    "SITE_HEADER": "Molla Agro Dashboard",
    "SITE_URL": "/",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Business Management",
                "separator": True,
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": "/admin/",
                    },
                    {
                        "title": "Live Orders",
                        "icon": "shopping_cart",
                        "link": "/admin/core/order/",
                    },
                    {
                        "title": "Products Inventory",
                        "icon": "inventory_2",
                        "link": "/admin/core/product/",
                    },
                    {
                        "title": "Categories",
                        "icon": "category",
                        "link": "/admin/core/category/",
                    },
                ],
            },
            {
                "title": "User Administration",
                "separator": True,
                "items": [
                    {
                        "title": "System Users",
                        "icon": "group",
                        "link": "/admin/auth/user/",
                    },
                ],
            },
        ],
    },
}