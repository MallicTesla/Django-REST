from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rc%f6(vg76pxawvfglc7kcnstv7*$p+%b@u*t6tpwb3)0#&p*&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#   las aplicaciones con las que viene dejango
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#   Las aplicaciones que creo
LOCAL_APPS = [
    "usuarios",
    "productos",
    "base",
]

#   las aplicaciones de terseros
THIRD_APPS = [
    "rest_framework",
    # este es un jenerador de tokens que viene incluido en el framework
    "rest_framework.authtoken",
    #   despues de instalar esta libreria agregas algo en MIDDLEWARE
    "simple_history",
    # libreria para ver las apis documentacion https://drf-yasg.readthedocs.io/en/stable/readme.html
    "drf_yasg",
    # libreria para politica CORS
    "corsheaders",
    #   libreria jwt
    "rest_framework_simplejwt",

]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

SWAGGER_SETTINGS = {
    # esto hace que los menus desplegables de swagger aparescan contraidos existen munchas mas configurasiones en la documentacion
    "DOC_EXPANSION":"none"
}

MIDDLEWARE = [
    # politica CORS
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #   agregas esto que es para reconoser el istorial de cada usuario
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = 'tienda.urls'

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

WSGI_APPLICATION = 'tienda.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# verificar las credenciales de usuario y determinar si un usuario tiene acceso a la aplicación
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Montevideo'

# define el tiempo en el que expira el token en segundos
# si usas la libreria simple JWT esto no es nesesario
# TIEMPO_EXPIRASION_TOKEN = 8000

USE_I18N = True

USE_TZ = True

#   especifica un modelo de usuario personalizado
AUTH_USER_MODEL = "usuarios.Usuario"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # autenticasion global personalisada
        #  aca va la clase que se usa para autentificar
        # "usuarios.autentificasion_mixer.Autentificador",
        #   este es para la libreria simple JWT
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
        # para agregarle la autentificasion de forma global
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
# }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
#    "https://example.com",
#    "https://sub.example.com",
#   en este caso se permite solo del puerto 3000
    "http://localhost:3000",
#    "http://127.0.0.1:9000",
]

CORS_ORIGIN_WHITELIST = [
#   la misma rutas que estan autorisadas ariba
    "http://localhost:3000",
]

STATIC_URL = 'static/'