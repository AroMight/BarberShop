from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

import pytest
from users.forms import LoginForm


class TestUserLoginView(TestCase):

    login_url = reverse_lazy("users:login")

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

        data = {
            "username": "testuser",
            "password": "Abc@123456",
        }
        user = User.objects.create_user(**data)
        self.client.force_login(user)

        response = self.client.get(self.login_url, follow=True)
        self.assertRedirects(response, reverse("home"))

    def test_users_login_view_successfully_login_a_user(self):
        data = {
            "username": "testuser",
            "password": "Abc@123456",
        }

        user = User.objects.create_user(**data)
        response = self.client.post(self.login_url, data=data, follow=True)
        context = response.context
        user_logged = context["user"]

        self.assertEqual(user_logged, user)

    @pytest.mark.skip(reason="Not implemented yet")
    def test_users_login_view_do_not_login_invalid_user(self):

        data = {
            "username": "test_user",
            "password": "Abc@123456",
        }
        self.client.post(self.login_url, data=data)

        self.assertIsNone(self.client.session.get("_auth_user_id"))

    @pytest.mark.skip(reason="Not implemented yet")
    def test_login_view_show_error_message(self):
        pass
