from django.urls import path

from .views import dashboard


app_name = "coaches"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
]
