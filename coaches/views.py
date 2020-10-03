import datetime

from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required

from plans.models import Plan


@login_required(login_url="accounts:login")
def dashboard(request):
    plans_num = Plan.objects.filter(coach=request.user).count()
    context = {
        "plans_num": plans_num
    }
    return render(request, "coaches/dashboard.html", context)


def new_requests(request):
    coach = request.user
    new_requests = get_list_or_404(Plan, coach=coach, status=False)
    context = {
        "new_requests": new_requests
    }
    return render(request, "coaches/new_requests.html", context)
