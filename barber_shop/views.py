from django.views.generic import TemplateView
from reservations.forms import ReservationForm


class HomeView(TemplateView):

    template_name = 'barber_shop/home.html'
    extra_context = {
        'btn_action': 'Confirm',
        'form': ReservationForm(),
    }
