from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from profiles.models import Profile, CoachProfileExtra
from accounts.models import CoachExtra


def user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.type == Profile.Types.CLIENT:
            profile = Profile.objects.create(
                location="تهران", job="", type=Profile.Types.CLIENT)
            instance.profile = profile
            instance.save()
        elif instance.type == Profile.Types.COACH:
            profile = Profile.objects.create(
                location="", job="", type=Profile.Types.COACH)
            instance.profile = profile
            CoachExtra.objects.create(user=instance)
            CoachProfileExtra.objects.create(profile=profile, education="")
            instance.save()


post_save.connect(user_profile, sender=get_user_model())
