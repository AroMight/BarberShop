from django import forms
from forms.icon_fields import IconDateField, IconModelChoiceField, IconTimeField
from ..models import Reservation
from ..models import Service, Branch


class ReservationForm(forms.ModelForm):

    service = IconModelChoiceField(
        icon='bi bi-bag-fill',
        queryset=Service.objects.all(),
        label="Choose a service",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    date = IconDateField(
        icon='bi bi-calendar-check-fill',
        label="Choose a date",
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        )
    )

    branch = IconModelChoiceField(
        icon='bi bi-shop-window',
        queryset=Branch.objects.all(),
        label="Choose a branch",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    time = IconTimeField(
        icon='bi bi-clock-fill',
        label="Choose the hour",
        widget=forms.TimeInput(
            attrs={
                'class': 'row form-control row-cols-2 row-cols-sm-3 row-cols-md-3 row-cols-lg-5',
                'type': 'time',
                'min': '09:00',
                'max': '17:00',
                'step': '3600'
            }
        )
    )

    class Meta:
        model = Reservation
        fields = [
            'service',
            'date',
            'branch',
            'time',
        ]
