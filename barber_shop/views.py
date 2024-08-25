from django.views import View
from django.shortcuts import render
from reservations.forms import ReservationForm
from users.models import Customer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime


class HomeViewSet(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'barber_shop/home.html', context={'form': form})

    @method_decorator(login_required(login_url='users/login/'))
    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['date'] < datetime.date.today():
                form.add_error('date', 'The date cannot be in the past')
                return render(request, 'barber_shop/home.html', context={'form': form})

            user = request.user
            customer = Customer.objects.get(user=user)
            reservation = form.save(commit=False)
            reservation.customer = customer
            reservation.save()
            form = ReservationForm()
            return render(request, 'barber_shop/home.html', context={'form': form})
        return render(request, 'barber_shop/home.html', context={'form': form})
