from django.urls import path

from .views import login, logout, register, dashboard, user_profile

app_name = "accounts"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", user_profile, name="user_profile")
]
