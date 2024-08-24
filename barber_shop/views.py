from django.views import View
from django.shortcuts import render
from reservations.forms import ReservationForm
from users.models import Customer

class HomeViewSet(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'barber_shop/home.html', context={'form': form})
    
    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            user = request.user
            customer = Customer.objects.get(user=user)
            reservation = form.save(commit=False)
            reservation.customer = customer
            reservation.save()
            form = ReservationForm()
            return render(request, 'barber_shop/home.html', context={'form': form})
        return render(request, 'barber_shop/home.html', context={'form': form})
