from django.urls import path

from .views import create_plan, plan_list, plan_detail


app_name = "plans"

urlpatterns = [
    path("new/<int:coach_id>/", create_plan, name="create_plan"),
    path("list/", plan_list, name="list"),
    path("detail/<int:plan_id>/", plan_detail, name="detail")
]
