from django.shortcuts import render

from sizes.forms import SizesForm

def create_plan(request):
    sizes_form = SizesForm()
    context = {
        "sizes_form": sizes_form
    }
    return render(request, "plans/index.html", context)
