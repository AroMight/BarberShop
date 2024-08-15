from django.http import HttpResponse


def register(request):
    return HttpResponse('Register page')

def login(request):
    return HttpResponse('Login page')

def logout(request):
    return HttpResponse('Logout page')