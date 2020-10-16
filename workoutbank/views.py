from django.shortcuts import render, get_list_or_404

from workoutbank.models import WorkoutItem


def workout_list(request):
    workouts = get_list_or_404(WorkoutItem)
    context = {
        "workouts": workouts,
    }
    return render(request, "workoutbank/workoutlist.html", context)
