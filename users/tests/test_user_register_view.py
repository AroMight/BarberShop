from django.test import TestCase
from django.urls import reverse
from users.models import Customer


class TestUserRegisterViewSet(TestCase):
    def test_register_viewset_loads_correct_template(self):
        response = self.client.get('/users/register/')
        self.assertTemplateUsed(response, 'users/pages/register.html')

    def test_register_viewset_create_a_customer(self):
        data = {
            'username': "johndoe",
            'first_name': 'John',
            'last_name': 'Doemi',
            'email': 'jhon@doe.com',
            'password': 'Abc@123456',
            'password2': 'Abc@123456',
        }

        response = self.client.post('/users/register/', data=data)

        self.assertTrue(Customer.objects.filter(
            user__username='johndoe').exists())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
