import datetime

from django.shortcuts import render, get_list_or_404, get_object_or_404
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


def create_plan(request, request_id):
    plan_obj = get_object_or_404(Plan, pk=request_id, coach=request.user)
    context = {
        "plan_size": plan_obj.size,
        "plan_client": plan_obj.client,
        "plan_images": plan_obj.image,
        "plan_created_at": plan_obj.created_at
    }
    return render(request, "coaches/design_plan.html", context)
