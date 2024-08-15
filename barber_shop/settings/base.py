from pathlib import Path
from .environment import SECRET_KEY, DEBUG, ALLOWED_HOSTS

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ROOT_URLCONF = 'barber_shop.urls'

WSGI_APPLICATION = 'barber_shop.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
