from django.test import TestCase
from django.urls import reverse, resolve
from ..views import UserReservationsView


class TestUserReservationViews(TestCase):

    url = reverse("users:reservations")

    def test_user_reservations_url_loads_correct_view(self):
        response = resolve(self.url)
        func = response.func.view_class
        self.assertEqual(func, UserReservationsView)

    def test_user_reservations_url_returns_status_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_user_reservations_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "users/pages/users_reservations.html")

