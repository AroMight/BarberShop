from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms.register_form import RegisterForm


class RegisterView(SuccessMessageMixin, FormView):
    template_name = 'users/pages/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    success_message = "Account created successfully, please login!"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
