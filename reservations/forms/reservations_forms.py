from django import forms
from ..models import Reservation


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    available_times = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
    ]

    time = forms.ChoiceField(label='Selecione um horário',choices=available_times, widget=forms.RadioSelect(attrs={'class': 'row row-cols-2 row-cols-sm-3 row-cols-md-3 row-cols-lg-5'}))

    class Meta:
        model = Reservation
        fields = [
            'service',
            'date',
            'time',
            'branch',
        ]
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
        }