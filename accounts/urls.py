from django.urls import path

from .views import login, register, dashboard, user_profile

app_name = "accounts"

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", user_profile, name="user_profile")
]
