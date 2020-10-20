from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from accounts.models import CoachExtra
from .models import Profile, CoachProfile
from .forms import UpdateUserProfile
from accounts.forms import UpdateClientInformation
from coaches.forms import (UpdateCoachInformation,
                           UpdateCoachExtraInformation,
                           UpdateCoachProfile,
                           UpdateCoachProfileExtra)

from accounts.decorators import authorized_user, client_required, coach_required


@login_required(login_url="accounts:login")
@client_required
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


@login_required(login_url="accounts:login")
@coach_required
def update_coach_information(request):
    user = request.user
    if user.is_authenticated and user.profile:
        coach_instance = get_object_or_404(
            get_user_model(), pk=request.user.pk)
        profile_instance = get_object_or_404(Profile, account=user)

        coach_form = UpdateCoachInformation(
            request.POST or None, instance=coach_instance)
        coach_extra_form = UpdateCoachExtraInformation(
            request.POST or None, instance=coach_instance.coachextra)
        profile_form = UpdateCoachProfile(
            request.POST or None, instance=profile_instance)
        coach_profile_extra_form = UpdateCoachProfileExtra(
            request.POST or None, request.FILES or None, instance=profile_instance.coachprofileextra)
        if coach_form.is_valid() and coach_extra_form.is_valid() and profile_form.is_valid() and coach_profile_extra_form.is_valid():
            coach_extra_form.save()
            profile_form.save()
            coach_form.save()
            coach_profile_extra_form.save()
            return redirect("coaches:dashboard")
        # form is not valid so return flash message to notify user.
        return redirect("coaches:dashboard")
    return redirect("accounts:login")
