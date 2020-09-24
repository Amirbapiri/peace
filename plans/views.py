from django.shortcuts import render


def create_plan(request):
    return render(request, "plans/index.html", {})
