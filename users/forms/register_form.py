from django import forms
from ..models import Customer
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RegisterForm(forms.ModelForm):

    username = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter your username.')}
        ),
        help_text=_(
            'Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    )

    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter your first name.')}
        ),
    )

    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter your last name.')}
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter your email.')}
        ),
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter your password.')}
        ),
        help_text=_(
            'Your password must contain at least 8 characters, 1 number and 1 special character.'
        ),
    )

    password2 = forms.CharField(
        label=_('Confirm Password'),
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Repeat your password.')}),
        help_text=_('Passwords must match.'),
    )

    class Meta:
        model = Customer

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2',
            'phone_number',
            'profile_photo',
        ]

    def clean(self):
        """Check if password and password2 are equal"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_mismatch_error = ValidationError(
                _("Passwords didn't match."), code='password_mismatch'
            )

            raise ValidationError({
                'password': password_mismatch_error,
                'password2': password_mismatch_error,
            })

    def clean_email(self):
        """Check if email is already registred"""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if Customer.objects.filter(email=email).exists():
            raise ValidationError(
                _('Email already registred.'), code='email_invalid')

        return email
