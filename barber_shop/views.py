from django.views import View
from django.shortcuts import render


class HomeViewSet(View):
    def get(self, request):
        return render(request, 'barber_shop/home.html')
