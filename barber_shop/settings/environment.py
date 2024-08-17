import os


SECRET_KEY = os.environ.get('SECRET_KEY')


# Converta a string para booleano
DEBUG = os.environ.get('DEBUG').lower() in ('true', '1', 't', 'yes', 'y')

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]
