from django.shortcuts import render


def workout_list(request):
    return render(request, "workoutbank/workoutlist.html", {})
