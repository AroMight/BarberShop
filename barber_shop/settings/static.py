from .base import BASE_DIR

STATICFILES_DIRS = [
    BASE_DIR / 'global_static',
]

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
