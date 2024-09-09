from django.test import TestCase
from django.urls import reverse_lazy, resolve
from django.contrib.auth.models import User

from users.models import Customer
from ..views import UserReservationsView


class TestUserReservationViews(TestCase):

    url = reverse_lazy("users:reservations")

    def test_user_reservations_url_loads_correct_view(self):
        response = resolve(self.url)
        func = response.func.view_class
        self.assertEqual(func, UserReservationsView)

    def test_user_reservations_url_redirect_if_user_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login/?next=/users/reservations/")

    def test_user_reservations_url_returns_200_if_user_authenticated(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        user = User.objects.create_user(**data)
        customer = Customer.objects.create(user=user)

        self.client.force_login(user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_user_reservations_uses_correct_template(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        user = User.objects.create_user(**data)
        customer = Customer.objects.create(user=user)

        self.client.force_login(user)


        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "users/pages/users_reservations.html")
