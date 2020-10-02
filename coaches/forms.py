from django.forms import ModelForm

from accounts.models import Account, CoachExtra
from profiles.models import Profile, CoachProfile, CoachProfileExtra


class UpdateCoachInformation(ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "last_name"]


class UpdateCoachExtraInformation(ModelForm):
    class Meta:
        model = CoachExtra
        fields = ["workout_price", "meal_price"]


class UpdateCoachProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ["location", "job"]


class UpdateCoachProfileExtra(ModelForm):
    class Meta:
        model = CoachProfileExtra
        fields = ["education", "image", "panel_image"]
