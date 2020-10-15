from django.urls import path

from .views import workout_list


app_name = "workoutbank"

urlpatterns = [
    path("list/", workout_list, name="list"),
]
