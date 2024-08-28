from django.test import TestCase
from django.urls import resolve, reverse
from barber_shop.views import HomeView


class HomeUrlTests(TestCase):

    def test_barbershop_home_url_loads_correct_view(self):
        url = reverse('home')
        response = resolve(url)
        self.assertIs(response.func.view_class, HomeView)

    def test_barber_shop_home_url_namespace(self):
        url = reverse('home')
        self.assertEqual(url, '/')
