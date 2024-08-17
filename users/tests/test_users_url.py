from django.test import TestCase
from django.urls import reverse, resolve
from users.views.site import RegisterViewSet


class TestUsersUrls(TestCase):
    def test_users_register_url_return_200(self):
        url = reverse('users:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_users_register_url_loads_correct_view(self):
        url = reverse('users:register')
        response = self.client.get(url)
        view = response.request.get('PATH_INFO')
        resolved_view = resolve(view)
        self.assertEqual(resolved_view.func.view_class, RegisterViewSet)

    def test_users_register_url_is_correct(self):
        url = reverse('users:register')
        self.assertEqual(url, '/users/register/')
