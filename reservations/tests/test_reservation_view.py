from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.views import ReservationView
from reservations.models import Service, Branch, Customer, Reservation


class TestReservationView(TestCase):

    def setUp(self) -> None:
        user = User.objects.create_user(username="test", password="test")
        customer = Customer.objects.create(user=user)
        self.client.force_login(user)

        branch = Branch.objects.create(district="Branch 1", address="Address 1")
        service = Service.objects.create(name="Service 1", price=10.0)

        self.data = {
            "service": 1,
            "branch": 1,
            "date": (date.today() + timedelta(days=1)).isoformat(),
            "time": "12:00",
        }

        return super().setUp()

    def test_reservation_view_successfully_create_reservation(self):

        url = reverse("reservations:create")
        response = self.client.post(url, data=self.data, follow=True)
        content = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Reservation.objects.filter(id=1).exists())

    def test_reservation_view_add_message_on_success(self):
        url = reverse("reservations:create")
        response = self.client.post(url, data=self.data, follow=True)
        content = response.content.decode("utf-8")
        self.assertIn("Reservation made successfully!", content)

    def test_reservation_view_add_message_if_form_is_invalid(self):
        self.data["time"] = "00:00"

        url = reverse("reservations:create")
        response = self.client.post(url, data=self.data, follow=True)
        content = response.content.decode("utf-8")
        self.assertIn("There&#x27;s an error in the form, please check it!", content)

    def test_reservation_view_redirect_on_success(self):
        url = reverse("reservations:create")
        response = self.client.post(url, data=self.data, follow=True)
        self.assertRedirects(response, reverse("home"))

    def test_reservation_view_redirect_if_form_is_invalid(self):
        self.data["time"] = "00:00"

        url = reverse("reservations:create")
        response = self.client.post(url, data=self.data, follow=True)
        self.assertRedirects(response, reverse("home"))
