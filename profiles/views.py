from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UpdateUserProfile
from accounts.forms import UpdateClientInformation


@login_required(login_url="accounts:login")
def update_client_information(request):
    user = request.user
    if user.is_authenticated and user.profile:
        client_instance = get_object_or_404(
            get_user_model(), pk=request.user.pk)
        profile_instance = get_object_or_404(Profile, account=user)

        client_form = UpdateClientInformation(
            request.POST or None, instance=client_instance)
        profile_form = UpdateUserProfile(
            request.POST or None, request.FILES or None, instance=profile_instance)

        if client_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            client_form.save()
            return redirect("accounts:user_profile")
        # form is not valid so return flash message to notify user.
        return redirect("accounts:user_profile")
    return redirect("accounts:login")
