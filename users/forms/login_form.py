from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Username')})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Password')})

    class Meta:
        model = User
        fields = ['username', 'password']
