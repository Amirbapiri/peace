from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Coach
from .forms import PlanNatureFoodForm
from sizes.forms import SizesForm
from client_images.forms import ClientImageForm


@login_required(login_url="accounts:login")
def create_plan(request, coach_id):
    size_form = SizesForm(request.POST or None)
    plan_form = PlanNatureFoodForm(request.POST or None)
    image_form = ClientImageForm(request.POST or None, request.FILES or None)
    coach = get_object_or_404(Coach, pk=coach_id)
    if request.POST:
        if size_form.is_valid() and plan_form.is_valid() and image_form.is_valid():
            size = size_form.save(commit=False)
            size.client = request.user
            size.save()

            plan = plan_form.save(commit=False)
            image = image_form.save(commit=False)
            image.plan = plan

            plan.client = request.user
            plan.coach = coach
            plan.size = size
            plan.image = image

            image.save()
            plan.save()

        else:
            print("ERRORS IN FORMS")
    context = {
        "size_form": size_form,
        "plan_form": plan_form,
        "image_form": image_form,
        "coach": coach
    }
    return render(request, "plans/index.html", context)
