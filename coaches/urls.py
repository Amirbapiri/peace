from django.urls import path

from .views import dashboard, new_requests, create_plan, create_pdf
from profiles.views import update_coach_information


app_name = "coaches"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("requests/list/", new_requests, name="new_requests"),
    path("requests/create/<int:request_id>/", create_plan, name="create_plan"),
    path("requests/create/pdf/", create_pdf, name="create_pdf"),
    path("update/", update_coach_information, name="update_coach_information"),
]
