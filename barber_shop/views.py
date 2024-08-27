from django.views.generic import TemplateView
from reservations.forms import ReservationForm


class HomeView(TemplateView):

    template_name = 'barber_shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()
        context['btn_action'] = 'Confirm'
        return context
