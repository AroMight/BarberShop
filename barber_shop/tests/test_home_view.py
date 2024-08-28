from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from reservations.forms.reservations_forms import ReservationForm


class HomeViewTets(TestCase):

    def test_home_view_returns_200(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'barber_shop/home.html')

    def test_home_view_contains_all_context_data(self):
        url = reverse("home")
        response = self.client.get(url)
        context = response.context
        self.assertIn('btn_action', context)
        self.assertIn('form', context)

    def test_home_view_contains_reservation_form(self):
        url = reverse("home")
        response = self.client.get(url)
        context = response.context
        self.assertIsInstance(context['form'], ReservationForm)

    def test_home_template_do_not_show_login_button_if_user_is_authenticated(self):
        user = User.objects.create_user(
            username='test_user', password='test_pass')
        self.client.force_login(user)
        url = reverse("home")
        response = self.client.get(url)
        content = response.content.decode('utf-8')
        self.assertNotIn('Login', content)

    def test_home_template_shows_reservations_if_user_is_authenticated(self):
        user = User.objects.create_user(
            username='test_user', password='test_pass')
        self.client.force_login(user)
        url = reverse("home")
        response = self.client.get(url)
        content = response.content.decode('utf-8')
        self.assertIn('My reservations', content)
