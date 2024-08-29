from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from utils import IconCharField, IconUsernameField


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Username')})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Password')})

    username = IconUsernameField(
        icon="bi bi-person-fill",
        widget=forms.TextInput(
            attrs={"autofocus": True}
        )
    )

    password = IconCharField(
        icon="bi bi-lock-fill",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Enter your password.')}
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'password']
