import re

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    return regex.match(password)


if __name__ == "__main__":
    password = '123123'
    print(strong_password(password))