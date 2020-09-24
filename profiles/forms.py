from django.forms import ModelForm

from .models import Profile


class UpdateUserProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ["location", "job", "image"]
