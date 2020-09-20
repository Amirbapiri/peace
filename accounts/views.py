from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import LoginForm, RegistrationForm


def login(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request)
                return redirect("accounts:login")
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
            # first_name = form.cleaned_data.get("first_name")
            # last_name = form.cleaned_data.get("last_name")
            # email = form.cleaned_data.get("email")
            # username = form.cleaned_data.get("username")
            form.save()
            return redirect("accounts:login")
        else:
            context["form"] = form
    else:
        form = RegistrationForm()
        context["form"] = form
    return render(request, "accounts/register.html", context)
