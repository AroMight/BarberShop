from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Customer
from ..forms import RegisterForm


class TestUserRegisterViewSet(TestCase):

    def test_users_register_url_return_200(self):
        url = reverse('users:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_viewset_loads_correct_template(self):
        url = reverse('users:register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'users/pages/users_account.html')

    def test_users_register_view_contains_all_context_data(self):
        url = reverse('users:register')
        response = self.client.get(url)
        context = response.context
        self.assertIn('btn_action', context)
        self.assertIn('form', context)

    def test_register_viewset_contains_form(self):
        url = reverse('users:register')
        response = self.client.get(url)
        context = response.context
        self.assertIsInstance(context['form'], RegisterForm)

    def test_users_register_view_redirects_to_home_if_user_is_authenticated(self):
        url = reverse('users:register')
        user = User.objects.create_user(
            username='test_user', password='test_pass')
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertRedirects(response, reverse('home'))

    def test_register_view_create_a_customer(self):

        data = {
            'username': "johndoe",
            'email': 'jhon@doe.com',
            'password': 'Abc@123456',
            'password2': 'Abc@123456',
        }

        login_url = reverse('users:login')

        response = self.client.post('/users/register/', data=data)

        self.assertTrue(Customer.objects.filter(
            user__username='johndoe').exists())
        self.assertRedirects(response, login_url)

    def test_users_register_view_show_error_message(self):

        data = {
            'username': "johndoe",
            'email': 'jhon@doe.com',
            'password': 'weakpassword',
            'password2': 'wrongpassword',
        }

        login_url = reverse('users:login')
        response = self.client.post(login_url, data=data, follow=True)
        content = response.content.decode('utf-8')
        self.assertIn('Please, enter a stronger password.', content)