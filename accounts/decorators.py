from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect

from accounts.models import Account


def authorized_user(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == "CLIENT":
                # redirect to client's dashboard
                return redirect("accounts:dashboard")
            elif request.user.type == "COACH":
                # redirect to coache's dashboard
                return redirect("coaches:dashboard")
        else:
            return view(request, *args, **kwargs)
    return wrapper


def client_required(view):
    def wrapper(request, *args, **kwargs):
        print("client_required")
        if request.user.type == Account.Types.CLIENT:
            return view(request, *args, **kwargs)
        else:
            return redirect("accounts:dashboard")
    return wrapper


def coach_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == Account.Types.COACH:
                return view(request, *args, **kwargs)
            else:
                return redirect("accounts:dashboard")
    return wrapper
