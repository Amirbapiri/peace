from django.shortcuts import render

from .forms import PlanNatureFoodForm
from sizes.forms import SizesForm


def create_plan(request):
    sizes_form = SizesForm()
    plans_form = PlanNatureFoodForm()
    context = {
        "sizes_form": sizes_form,
        "plans_form": plans_form
    }
    return render(request, "plans/index.html", context)
