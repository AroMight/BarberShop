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
                'class': 'form-control',
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

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < date.today():
            raise forms.ValidationError('The date cannot be in the past.')
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time < time.now():
            raise forms.ValidationError('The time cannot be in the past.')
        return time
