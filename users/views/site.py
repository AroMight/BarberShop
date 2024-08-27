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
    extra_context = {
        'title':'Sign to BarberShop',
        'btn_action':'Sign up',
    }

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['title'] = 'Sign to BarberShop'
        # context['btn_action'] = 'Sign up'
        # return context

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
    redirect_authenticated_user = True

    """
    If you enable redirect_authenticated_user, other websites will be able to             determine if their visitors are authenticated on your site by requesting redirect URLs to image files on your website. To avoid this “social media fingerprinting” information leakage, host all images and your favicon on a separate domain.

    Enabling redirect_authenticated_user can also result in a redirect loop when using the permission_required() decorator unless the raise_exception parameter is used.
    """