from django.urls import path

from .views import dashboard
from profiles.views import update_coach_information


app_name = "coaches"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("update/", update_coach_information, name="update_coach_information")
]
