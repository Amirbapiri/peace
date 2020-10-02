from django.forms import ModelForm

from accounts.models import Account, CoachExtra


class UpdateCoachInformation(ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "last_name"]


class UpdateCoachExtraInformation(ModelForm):
    class Meta:
        model = CoachExtra
        fields = ["workout_price", "meal_price"]
