"""Определяет схемы URL для пользователей"""

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # Включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('register/', views.register, name='register'),
    # Страница выхода
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]
