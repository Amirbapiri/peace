from django.urls import path

from .views import workout_list, workout_detail


app_name = "workoutbank"

urlpatterns = [
    path("list/", workout_list, name="list"),
    path("detail/<int:workout_id>/", workout_detail, name="detail")
]
