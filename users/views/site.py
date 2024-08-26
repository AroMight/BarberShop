from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms import RegisterForm, LoginForm


class RegisterViewSet(SuccessMessageMixin, FormView):
    template_name = 'users/pages/users_account.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    success_message = "Account created successfully, please login!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign to BarberShop'
        context['btn_action'] = 'Sign up'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginViewSet(SuccessMessageMixin, LoginView):
    template_name = 'users/pages/users_account.html'
    form_class = LoginForm
    success_message = "Welcome back %(username)s!"
    next_page = reverse_lazy('home')
    extra_context = {
        'title': 'Sign in to BarberShop',
        'btn_action': 'Sign in',
    }
    