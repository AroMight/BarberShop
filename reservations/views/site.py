from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from reservations.forms import ReservationForm
from users.models import Customer


class ReservationView(View):

    def render_home(self, request, form):
        return render(
            request,
            'barber_shop/home.html',
            context={
                'form': form,
                'btn_action': 'Confirm'
            }
        )

    @method_decorator(login_required(login_url=reverse_lazy('users:login')))
    def post(self, request):
        form = ReservationForm(request.POST)

        if form.is_valid():
            user = request.user
            customer = Customer.objects.get(user=user)
            reservation = form.save(commit=False)
            reservation.customer = customer
            reservation.save()

            messages.success(request, 'Reservation made successfully!')

            form = ReservationForm()
            return self.render_home(request, form)

        messages.error(
            request, "There's an error in the form, please check it!")
        return self.render_home(request, form)
