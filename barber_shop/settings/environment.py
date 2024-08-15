import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')


# Converta a string para booleano
DEBUG = os.getenv('DEBUG').lower() in ('true', '1', 't', 'yes', 'y')

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]