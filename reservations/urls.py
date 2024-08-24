from django.urls import path
from . import views
app_name = 'reservations'

urlpatterns = [
    path('', views.ReservationForm, name='list'),
]