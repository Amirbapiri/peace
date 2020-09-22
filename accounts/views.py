from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .forms import LoginForm, RegistrationForm, UpdateClientInformation


def login(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user:
                auth_login(request, user)
                return redirect("accounts:dashboard")
            else:
                print("Invalid credentials")
                return redirect("accounts:register")
        else:
            context["form"] = form
    else:
        form = LoginForm()
        context["form"] = form
    return render(request, "accounts/login.html", context)


def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.type = "CLIENT"
            form.save()
            return redirect("accounts:login")
        else:
            context["form"] = form
    else:
        form = RegistrationForm()
        context["form"] = form
    return render(request, "accounts/register.html", context)


def dashboard(request):
    context = {}
    if request.user.is_authenticated:
        coaches = get_user_model().objects.coaches()
        context["coaches"] = coaches
    else:
        return redirect("accounts:login")
    return render(request, "accounts/dashboard.html", context)


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    context = {}
    if request.user.profile and request.user.type == "CLIENT":
        context["profile"] = request.user.profile
    return render(request, "accounts/user_profile.html", context)
