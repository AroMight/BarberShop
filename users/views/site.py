from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views import View
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from reservations.models import Reservation
from ..forms import RegisterForm, LoginForm


class RegisterView(SuccessMessageMixin, FormView):
    template_name = "users/pages/users_account.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")
    success_message = "Account created successfully, please login!"
    extra_context = {
        "title": "Login",
        "btn_action": "Sign up",
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Mudar para a página de perfil do usuário
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(SuccessMessageMixin, LoginView):

    template_name = "users/pages/users_account.html"
    form_class = LoginForm
    success_message = "Welcome back %(username)s!"
    # Problema ao usar next (até agora conhecida em /reservations)
    next_page = reverse_lazy("home")
    redirect_authenticated_user = True
    extra_context = {
        "title": "Sign in to BarberShop",
        "btn_action": "Sign in",
    }

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        response = super().form_invalid(form)
        return response


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")


class UserReservationsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("users:login")
    model = Reservation
    template_name = "users/pages/users_reservations.html"
    paginate_by = 5
    context_object_name = "reservations"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = (
            qs.filter(customer=self.request.user.customer)
            .order_by("date", "time")
            .select_related("barber", "service")
        )
        return qs


class UserDeleteView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        reservation = Reservation.objects.get(pk=kwargs["id"])
        if reservation.customer == request.user.customer:
            reservation.delete()
            messages.success(request, "Reservation deleted successfully")
        else:
            messages.error(request, "You cannot delete this reservation")
        return redirect("users:reservations")


"""
    If you enable redirect_authenticated_user, other websites will be
    able to determine if their visitors are authenticated on your 
    site by requesting redirect URLs to image files on your website.
    To avoid this “social media fingerprinting” information leakage,
    host all images and your favicon on a separate domain.

    Enabling redirect_authenticated_user can also result in a
    redirect loop when using the permission_required()
    decorator unless the raise_exception parameter is used.
    """
