from datetime import datetime, timedelta
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from utils import IconDateField, IconModelChoiceField, IconTimeField
from ..models import Reservation
from ..models import Service, Branch


class ReservationForm(forms.ModelForm):

    service = IconModelChoiceField(
        icon="bi bi-bag-fill",
        queryset=Service.objects.filter(status=True),
        label="Choose a service",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    branch = IconModelChoiceField(
        icon="bi bi-shop-window",
        queryset=Branch.objects.all(),
        label="Choose a branch",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    date = IconDateField(
        icon="bi bi-calendar-check-fill",
        label="Choose a date",
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "min": datetime.now().strftime("%Y-%m-%d"),
                "max": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            }
        ),
    )

    time = IconTimeField(
        icon="bi bi-clock-fill",
        label="Choose the hour",
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "type": "time",
                "min": "09:00",
                "max": "17:00",
                "step": "3600",
            }
        ),
    )

    class Meta:
        model = Reservation
        fields = [
            "service",
            "branch",
            "date",
            "time",
        ]

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time:

            combined_datetime = datetime.combine(date, time)

            if combined_datetime < datetime.now():

                date_in_the_past_error = ValidationError(
                    _("The date and time cannot be in the past."),
                    code="date_in_the_past",
                )

                raise ValidationError(
                    {
                        "date": date_in_the_past_error,
                        "time": date_in_the_past_error,
                    }
                )

            if combined_datetime > datetime.now() + timedelta(days=30):

                date_in_the_future_error = ValidationError(
                    _("The date and time cannot be more than 30 days in the future."),
                    code="date_in_the_future",
                )

                raise ValidationError(
                    {
                        "date": date_in_the_future_error,
                        "time": date_in_the_future_error,
                    }
                )

        return cleaned_data

    def clean_time(self):
        cleaned_data = super().clean()
        time = cleaned_data.get("time")
        if (
            time < datetime.strptime("09:00", "%H:%M").time()
            or time > datetime.strptime("17:00", "%H:%M").time()
        ):
            raise ValidationError(
                _("The time must be between 09:00 and 17:00."), code="time_invalid"
            )
        return time
