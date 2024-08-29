from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Customer
from ..forms import RegisterForm


class TestUserRegisterView(TestCase):

    data = {
        "username": "johndoe",
        "email": "jhon@doe.com",
        "password": "Abc@123456",
        "password2": "Abc@123456",
    }

    def setUp(self):
        self.register_url = reverse("users:register")
        self.response = self.client.get(self.register_url)
        return super().setUp()

    def test_users_register_url_return_200(self):

        self.assertEqual(self.response.status_code, 200)

    def test_register_viewset_loads_correct_template(self):

        self.assertTemplateUsed(
            self.response, "users/pages/users_account.html")

    def test_users_register_view_contains_all_context_data(self):
        context = self.response.context

        self.assertIn("btn_action", context)
        self.assertIn("form", context)

    def test_register_viewset_contains_form(self):
        context = self.response.context

        self.assertIsInstance(context["form"], RegisterForm)

    def test_users_register_view_redirects_to_home_if_user_is_authenticated(self):
        user = User.objects.create_user(
            username="test_user", password="test_pass")
        self.client.force_login(user)
        response = self.client.get(self.register_url)

        self.assertRedirects(response, reverse("home"))

    def test_register_view_create_a_customer(self):
        response = self.client.post(self.register_url, data=self.data)

        self.assertTrue(Customer.objects.filter(
            user__username="johndoe").exists())

    def test_users_register_view_show_error_message(self):
        self.data.update(
            {
                "password": "weakpassword",
                "password2": "wrongpassword",
            }
        )

        response = self.client.post(self.register_url, data=self.data, follow=True)
        content = response.content.decode("utf-8")

        self.assertIn("Please, enter a stronger password.", content)
        self.assertIn("Passwords didn&#x27;t match.", content)
