from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', Register, name="register"),
    path('profile', Profile, name="profile"),
    path('profile_update', Profile_update, name="profile_update"),
    path('login', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name="logout"),
]
