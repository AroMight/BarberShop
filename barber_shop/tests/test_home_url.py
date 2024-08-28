from django.test import TestCase
from django.urls import resolve, reverse
from barber_shop.views import HomeView


class HomeUrlTests(TestCase):

    def test_home_url_status_code_is_200(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_barbershop_home_url_loads_correct_view(self):
        url = reverse('home')
        response = self.client.get(url)
        view = response.request.get('PATH_INFO')
        resolved_view = resolve(view)
        self.assertEqual(resolved_view.func.view_class, HomeView)

    def test_barber_shop_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')
