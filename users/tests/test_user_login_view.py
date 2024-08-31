from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

import pytest
from users.forms import LoginForm


class TestUserLoginView(TestCase):

    def setUp(self) -> None:
        self.login_url = reverse("users:login")

        self.data = {
            "username": "testuser",
            "password": "Abc@123456",
        }
        return super().setUp()

    def test_users_login_url_return_200(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_login_viewset_loads_correct_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, "users/pages/users_account.html")

    def test_users_login_view_contains_all_context_data(self):
        response = self.client.get(self.login_url)
        context = response.context
        self.assertIn("btn_action", context)
        self.assertIn("form", context)

    def test_login_view_contains_login_form(self):
        response = self.client.get(self.login_url)
        context = response.context
        self.assertIsInstance(context["form"], LoginForm)

    def test_users_login_view_redirects_to_home_if_user_is_authenticated(self):

        user = User.objects.create_user(**self.data)
        self.client.force_login(user)

        response = self.client.get(self.login_url, follow=True)
        self.assertRedirects(response, reverse("home"))

    def test_users_login_view_successfully_login_a_user(self):

        user = User.objects.create_user(**self.data)
        response = self.client.post(self.login_url, data=self.data, follow=True)
        context = response.context
        user_logged = context["user"]

        self.assertEqual(user_logged, user)

    def test_users_login_view_do_not_login_invalid_user(self):

        response = self.client.post(self.login_url, data=self.data)
        context = response.context
        user = context["user"]

        self.assertEqual(user.username, "")

    @pytest.mark.skip(reason="Not implemented yet")
    def test_login_view_show_error_message(self):
        pass
