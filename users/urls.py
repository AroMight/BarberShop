from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("reservations/", views.UserReservationsView.as_view(), name="reservations"),
    path(
        "reservations/<int:id>/",
        views.UserDeleteView.as_view(),
        name="reservations_delete",
    ),
]
