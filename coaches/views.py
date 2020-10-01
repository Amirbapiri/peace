import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from plans.models import Plan

@login_required(login_url="accounts:login")
def dashboard(request):
    plans_num = Plan.objects.filter(coach=request.user).count()
    context = {
        "plans_num": plans_num
    }
    return render(request, "coaches/dashboard.html", context)
