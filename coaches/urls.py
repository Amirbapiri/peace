from django.urls import path

from .views import dashboard, new_requests
from profiles.views import update_coach_information


app_name = "coaches"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("requests/list/", new_requests, name="new_requests"),
    path("update/", update_coach_information, name="update_coach_information"),
]
