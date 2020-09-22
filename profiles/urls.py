from django.urls import path

from .views import update_client_information

app_name = "profiles"

urlpatterns = [
    path("update/", update_client_information, name="update_client_information")
]
