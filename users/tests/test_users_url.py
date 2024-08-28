from django.test import TestCase
from django.urls import reverse, resolve
from ..views import RegisterView, LoginView


class TestUsersUrls(TestCase):

    def test_users_register_url_loads_correct_view(self):
        url = reverse('users:register')
        response = resolve(url)
        self.assertEqual(response.func.view_class, RegisterView)

    def test_users_register_url_namespace(self):
        url = reverse('users:register')
        self.assertEqual(url, '/users/register/')

    def test_users_login_url_return_200(self):
        url = reverse('users:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_users_login_url_loads_correct_view(self):
        url = reverse('users:login')
        response = resolve(url)
        self.assertEqual(response.func.view_class, LoginView)

    def test_users_login_url_namespace(self):
        url = reverse('users:login')
        self.assertEqual(url, '/users/login/')