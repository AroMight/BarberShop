from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ..models import Customer
from utils.forms_utils import strong_password


class RegisterForm(forms.ModelForm):

    username = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Enter your username.')}
        ),
        help_text=_(
            'Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    )

    # first_name = forms.CharField(
    #     max_length=30,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': _('Enter your first name.')}
    #     ),
    # )

    # last_name = forms.CharField(
    #     max_length=30,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': _('Enter your last name.')}
    #     ),
    # )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Enter your email.')}
        ),
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Enter your password.')}
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

    phone_number = forms.CharField(
        max_length=11,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Enter your phone number.')}
        ),
    )

    profile_photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'form-control', 'accept': 'image/*'}
        ),
    )

    class Meta:
        model = Customer

        fields = [
            'username',
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

        return cleaned_data

    def clean_username(self):
        """Check if email is already registred"""
        cleaned_data = super().clean()
        username = cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError(
                _('username already registred.'), code='username_invalid')

        return username

    def clean_email(self):
        """Check if email is already registred"""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                _('Email already registred.'), code='email_invalid')

        return email

    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')

        if not strong_password(password):
            raise ValidationError(
                _("Please, enter a stronger password."), code='password_invalid'
            )

        return password

    def save(self, commit: bool = True):
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate."
                % (
                    self.instance._meta.object_name,
                    "created" if self.instance._state.adding else "changed",
                )
            )
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data.get('username'),
                email=self.cleaned_data.get('email'),
                password=self.cleaned_data.get('password'),
            )

            Customer.objects.create(
                user=user,
                phone_number=self.cleaned_data.get('phone_number'),
                profile_photo=self.cleaned_data.get('profile_photo'),
            )
        else:
            self.save_m2m = self._save_m2m
        return self.instance
