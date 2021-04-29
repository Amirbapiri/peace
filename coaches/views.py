from io import BytesIO
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
from accounts.decorators import coach_required


@login_required(login_url="accounts:login")
@coach_required
def dashboard(request):
    plans_num = Plan.objects.filter(coach=request.user).count()
    context = {
        "plans_num": plans_num
    }
    return render(request, "coaches/dashboard.html", context)


@login_required(login_url="accounts:login")
@coach_required
def new_requests(request):
    coach = request.user
    new_requests = get_list_or_404(Plan, coach=coach, status=False)
    context = {
        "new_requests": new_requests
    }
    return render(request, "coaches/new_requests.html", context)


@login_required(login_url="accounts:login")
@coach_required
def create_plan(request, request_id):
    plan_obj = get_object_or_404(Plan, pk=request_id, coach=request.user)
    workouts = get_list_or_404(WorkoutItem)
    context = {
        "plan_id": plan_obj.pk,
        "plan_size": plan_obj.size,
        "plan_client": plan_obj.client,
        "plan_images": plan_obj.image,
        "plan_created_at": plan_obj.created_at,
        "workouts": workouts,
    }
    return render(request, "coaches/design_plan.html", context)


@csrf_exempt
# @coach_required
# def create_pdf(request):
#     # Data
#     data = json.loads(request.POST["workouts"])
#     plan_id = request.POST.get("plan_id")
#     plan_obj = get_object_or_404(Plan, pk=plan_id)
#     # Creating PDF file
#     html_string = render_to_string(
#         "coaches/workout_template.html", {"workouts": data})
#     print(html_string)
#     html = HTML(string=html_string)
#     result = html.write_pdf("report.pdf")
#     # Create http reponse
#     response = HttpResponse(content_type="application/pdf;")
#     response['Content-Disposition'] = 'attachment; filename="workout.pdf"'
#     # response["Content-Transfer-Encoding"] = "binary"
#     # with tempfile.NamedTemporaryFile(delete=True) as output:
#     #     output.write(result)
#     #     output.flush()
#     #     output = open(output.name, 'rb')
#     #     response.write(output.read())
#     return response
@csrf_exempt
def create_pdf(request):
    context = {
        "workouts": request.POST
    }
    print(request.POST)
    template = "coaches/workout_template.html"
    pdf = render_to_pdf(template, context)
    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        filename = "workout.pdf"
        content = "attachment; filename=%s" % filename
        # download = request.GET.get("download")
        # if download:
        content = "attachment; filename=%s" % filename
        response["Content-Disposition"] = content
        return response
    return HttpResponse("Not found.")


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("UTF-8")), result, encoding="UTF-8")
    return HttpResponse(result.getvalue(), content_type='application/pdf')
