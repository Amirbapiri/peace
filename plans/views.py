from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Coach
from .forms import PlanNatureFoodForm
from sizes.forms import SizesForm
from client_images.forms import ClientImageForm


@login_required(login_url="accounts:login")
def create_plan(request, coach_id):
    sizes_form = SizesForm()
    plans_form = PlanNatureFoodForm()
    client_image_form = ClientImageForm()
    context = {
        "sizes_form": sizes_form,
        "plans_form": plans_form,
        "image_form": image_form
    }
    return render(request, "plans/index.html", context)
