from django.shortcuts import render, get_list_or_404, get_object_or_404

from workoutbank.models import WorkoutItem


def workout_list(request):
    workouts = get_list_or_404(WorkoutItem)
    context = {
        "workouts": workouts,
    }
    return render(request, "workoutbank/workoutlist.html", context)


def workout_detail(request, workout_id):
    workout = get_object_or_404(WorkoutItem, pk=workout_id)
    context = {
        "workout": workout
    }
    return render(request, "workoutbank/workoutdetail.html", context)
