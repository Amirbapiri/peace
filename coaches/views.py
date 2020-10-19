import json
import tempfile

from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template, render_to_string
from django.views.generic import View

from workoutbank.models import WorkoutItem

from xhtml2pdf import pisa

from weasyprint import HTML

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
    workouts = get_list_or_404(WorkoutItem)
    context = {
        "plan_size": plan_obj.size,
        "plan_client": plan_obj.client,
        "plan_images": plan_obj.image,
        "plan_created_at": plan_obj.created_at,
        "workouts": workouts,
    }
    return render(request, "coaches/design_plan.html", context)


@csrf_exempt
def create_pdf(request):
    # Data
    data = json.loads(request.POST["workouts"])

    html_string = render_to_string(
        "coaches/workout_template.html", {"workouts": data})
    html = HTML(string=html_string)
    result = html.write_pdf("report.pdf")

    # Create http reponse
    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = "attachment; filename=report.pdf"
    response["Content-Transfer-Encoding"] = "binary"
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response
