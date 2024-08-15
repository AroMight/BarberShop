from django.views.generic import CreateView
from ..forms.register_form import RegisterForm
from ..models import Customer


class RegisterView(CreateView):
    template_name = 'users/pages/register.html'
    form_class = RegisterForm
    model = Customer
    success_url = '/users/login/'