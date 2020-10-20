from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect

from accounts.models import Account


def coach_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == Account.Types.COACH:
                return view(request, *args, **kwargs)
            else:
                return redirect("accounts:dashboard")
        else:
            return redirect("accounts:login")
    return wrapper
