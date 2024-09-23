import os
from dotenv import load_dotenv

load_dotenv()


def get_env_list(variable_name: str) -> list:
    if not isinstance(variable_name, str):
        return []
    value = os.environ.get(variable_name)
    list_value = [value.strip() for value in value.split(",") if value]
    return list_value


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG_MODE", "False").lower() in ["true", "1"]

ALLOWED_HOSTS = get_env_list("ALLOWED_HOSTS")

# Django DEBUG Toolbar
INTERNAL_IPS = get_env_list("INTERNAL_IPS")

CSRF_TRUSTED_ORIGINS = get_env_list("TRUSTED_ORIGINS")
