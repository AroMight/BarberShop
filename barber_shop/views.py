import datetime
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from reservations.forms import ReservationForm
from users.models import Customer


class HomeViewSet(View):

    def render_home(self, request, form):
        return render(
            request,
            'barber_shop/home.html',
            context={
                'form': form,
                'btn_action': 'Confirm',
            }
        )

    def get(self, request):
        form = ReservationForm()
        return self.render_home(request, form)

    @method_decorator(login_required(login_url='users/login/'))
    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():

            #tirar isso daqui e colocar no forms
            if form.cleaned_data['date'] < datetime.date.today():
                form.add_error('date', 'The date cannot be in the past')
                #talvez redirect seja melhor
                return self.render_home(request, form)

            user = request.user
            customer = Customer.objects.get(user=user)
            reservation = form.save(commit=False)
            reservation.customer = customer
            reservation.save()
            form = ReservationForm()
            return self.render_home(request, form)
        return self.render_home(request, form)
