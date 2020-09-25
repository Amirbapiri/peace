from django.forms import ModelForm

from .models import Plan


class PlanNatureFoodForm(ModelForm):
    class Meta:
        model = Plan
        fields = ("food_nature",)
