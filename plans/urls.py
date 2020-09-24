from django.urls import path

from .views import create_plan


app_name = "plans"

urlpatterns = [
    path("", create_plan, name="create_plan"),
]
