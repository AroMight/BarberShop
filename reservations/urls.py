from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.ReservationView.as_view(), name='create'),
]
