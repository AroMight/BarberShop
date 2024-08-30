from datetime import date
from django.test import TestCase
from parameterized import parameterized
from reservations.forms import ReservationForm
from reservations.models import Reservation, Service, Branch


class ReservationFormTest(TestCase):

    def setUp(self):
        self.form = ReservationForm()

    @parameterized.expand([
        ('service', 'Choose a service'),
        ('date', 'Choose a date'),
        ('branch', 'Choose a branch'),
        ('time', 'Choose the hour'),
    ])
    def test_form_field_label(self, field_name, expected_label):
        actual_label = self.form.fields[field_name].label
        self.assertEqual(actual_label, expected_label)

    @parameterized.expand([
        ('service', 'form-control'),
        ('date', 'form-control'),
        ('branch', 'form-control'),
        ('time', 'form-control'),
    ])
    def test_form_field_widget_class(self, field_name, expected_widget_class):
        actual_widget_class = self.form.fields[field_name].widget.attrs['class']
        self.assertEqual(actual_widget_class, expected_widget_class)

    @parameterized.expand([
        ('service', 'bi bi-bag-fill'),
        ('date', 'bi bi-calendar-check-fill'),
        ('branch', 'bi bi-shop-window'),
        ('time', 'bi bi-clock-fill'),
    ])
    def test_form_field_icon(self, field_name, expected_icon):
        actual_icon = self.form.fields[field_name].icon
        self.assertEqual(actual_icon, expected_icon)

    def test_reservation_form_date_field_can_not_be_in_the_past(self):

        branch = Branch.objects.create(
            district='Branch 1', address='Address 1')
        service = Service.objects.create(name='Service 1', price=10.0)

        data = {
            'service': service,
            'branch': branch,
            'time': '12:00',
            'date': '2022-12-12',
        }

        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_reservation_form_time_field_can_not_be_out_of_range(self):

        branch = Branch.objects.create(
            district='Branch 1',
            address='Address 1',
        )

        service = Service.objects.create(
            name='Service 1',
            price=10.0,
        )

    
        data = {
            'service': service,
            'branch': branch,
            'time': '07:00',
            'date': date.today().isoformat(),
        }

        form = ReservationForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors)
