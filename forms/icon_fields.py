from django import forms
from django.contrib.auth.forms import UsernameField

"""Adds an icon to a CharField, EmailField, or UsernameField"""


class IconCharField(forms.CharField):
    def __init__(self, *args, icon=None, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)


class IconEmailField(forms.EmailField):
    def __init__(self, *args, icon=None, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)


class IconUsernameField(UsernameField):
    def __init__(self, *args, icon=None, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)


class IconDateField(forms.DateField):
    def __init__(self, *args, icon=None, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)


class IconModelChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, icon=None, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)


class IconTimeField(forms.TimeField):
    def __init__(self, *args, icon=None, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)
