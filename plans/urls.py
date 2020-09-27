from django.urls import path

from .views import create_plan, plan_list


app_name = "plans"

urlpatterns = [
    path("new/<int:coach_id>/", create_plan, name="create_plan"),
    path("list/", plan_list, name="create_plan"),
]
