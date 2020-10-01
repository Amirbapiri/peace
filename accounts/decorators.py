from django.http import HttpResponse
from django.shortcuts import redirect


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
