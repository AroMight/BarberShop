from django.test import TestCase
from django.urls import reverse, resolve
import pytest
from ..views import ReservationView


class TestUsersUrls(TestCase):

    def test_users_register_url_loads_correct_view(self):
        url = reverse("reservations:create")
        response = resolve(url)
        self.assertEqual(response.func.view_class, ReservationView)

    def test_users_register_url_namespace(self):
        url = reverse("reservations:create")
        self.assertEqual(url, "/reservations/")
