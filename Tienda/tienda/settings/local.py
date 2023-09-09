#   tenes que entrar a manage.py y modificar la linia os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings.py) y agregarle la ruta a este archivo
#   quedaria asi os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings.local')
#   tenes que hacer lo mismo en el archivo asgi.py
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'