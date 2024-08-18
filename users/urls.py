from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterViewSet.as_view(), name='register'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
]
