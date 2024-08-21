import os


SECRET_KEY = str(os.environ.get('SECRET_KEY'))
SECRET_KEY = str(os.environ.get('SECRET_KEY'))


DEBUG = bool(os.environ.get('DEBUG', False))

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]
