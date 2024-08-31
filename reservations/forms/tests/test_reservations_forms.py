from datetime import date, timedelta, datetime
from django.test import TestCase
from django.contrib.auth.models import User
from parameterized import parameterized
from reservations.forms import ReservationForm
from reservations.models import Service, Branch, Reservation, Customer


class ReservationFormTest(TestCase):

    def setUp(self) -> None:
        branch = Branch.objects.create(district="Branch 1", address="Address 1")
        service = Service.objects.create(name="Service 1", price=10.0)

        self.data = {
            "service": service,
            "branch": branch,
            "time": "12:00",
            "date": (date.today() + timedelta(days=1)).isoformat(),
        }

        return super().setUp()

    @parameterized.expand(
        [
            ("service", "Choose a service"),
            ("date", "Choose a date"),
            ("branch", "Choose a branch"),
            ("time", "Choose the hour"),
        ]
    )
    def test_form_field_label(self, field_name, expected_label):
        form = ReservationForm()
        actual_label = form.fields[field_name].label
        self.assertEqual(actual_label, expected_label)

    @parameterized.expand(
        [
            ("service", "form-control"),
            ("date", "form-control"),
            ("branch", "form-control"),
            ("time", "form-control"),
        ]
    )
    def test_form_field_widget_class(self, field_name, expected_widget_class):
        form = ReservationForm()
        actual_widget_class = form.fields[field_name].widget.attrs["class"]
        self.assertEqual(actual_widget_class, expected_widget_class)

    @parameterized.expand(
        [
            ("service", "bi bi-bag-fill"),
            ("date", "bi bi-calendar-check-fill"),
            ("branch", "bi bi-shop-window"),
            ("time", "bi bi-clock-fill"),
        ]
    )
    def test_form_field_icon(self, field_name, expected_icon):
        form = ReservationForm()
        actual_icon = form.fields[field_name].icon
        self.assertEqual(actual_icon, expected_icon)

    def test_reservation_form_successfully_save_the_reservation(self):

        user = User.objects.create_user(username="user", password="123456")
        customer = Customer.objects.create(user=user)

        form = ReservationForm(data=self.data)
        form.is_valid()
        reservation = form.save(commit=False)
        reservation.customer = customer
        reservation.save()

        self.assertTrue(Reservation.objects.filter(pk=reservation.pk).exists())

    def test_reservation_form_date_field_can_not_be_in_the_past(self):

        self.data["date"] = (date.today() - timedelta(days=1)).isoformat()
        form = ReservationForm(data=self.data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "The date and time cannot be in the past.", form.errors.get("date")
        )

    def test_reservation_form_time_can_not_be_in_the_past(self):

        self.data.update(
            {
                "date": (date.today() - timedelta(days=1)).isoformat(),
                "time": "09:00",
            }
        )

        form = ReservationForm(data=self.data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            "The date and time cannot be in the past.", form.errors.get("time")
        )

    def test_reservation_form_date_field_can_not_be_more_than_30_days_ahead(self):

        self.data["date"] = (date.today() + timedelta(days=31)).isoformat()

        form = ReservationForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "The date and time cannot be more than 30 days in the future.",
            form.errors.get("date"),
        )

    def test_reservation_form_time_must_be_between_09_and_17(self):

        self.data["time"] = "08:00"

        form = ReservationForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "The time must be between 09:00 and 17:00.", form.errors.get("time")
        )

        self.data["time"] = "18:00"

        form = ReservationForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "The time must be between 09:00 and 17:00.", form.errors.get("time")
        )
