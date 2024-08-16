from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from ..forms.register_form import RegisterForm
from ..models import User, Customer


class RegisterView(SuccessMessageMixin, FormView):
    template_name = 'users/pages/register.html'
    form_class = RegisterForm
    success_url = '/'
    success_message = "Account created successfully, please login!"

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email').lower()
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        Customer.objects.create(
            user=user,
            phone_number=form.cleaned_data.get('phone_number'),
            profile_photo=form.cleaned_data.get('profile_photo'),
        )

        return super().form_valid(form)
