from django.test import TestCase
from django.urls import resolve, reverse
from barber_shop.views import HomeViewSet
from barber_shop.urls import urlpatterns


class HomeUrlTests(TestCase):
    def test_barbershop_home_url_is_correct(self):
        response = self.client.get('/')
        url = response.request['PATH_INFO']
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func.view_class, HomeViewSet)

    def test_home_url_resolves_to_home_view(self):
        response = self.client.get('/')
        url = response.request['PATH_INFO']
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'barber_shop/home.html')

    def test_home_url_status_code_is_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)