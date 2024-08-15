from django.shortcuts import render

def home(request):
    return render(request, 'barber_shop/home.html')