from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from profiles.models import Profile


def user_profile(sender, instance, created, **kwargs):
    if created:
        print("user_profile called")
        print("instance: ", instance, instance.username, instance.type)
        if instance.type == Profile.Types.CLIENT:
            profile = Profile.objects.create(
                location="تهران", job="", type=Profile.Types.CLIENT)
            instance.profile = profile
            instance.save()
            print("instance is client and profile created for that.")
        elif instance.type == Profile.Types.COACH:
            profile = Profile.objects.create(
                location="", job="", type=Profile.Types.COACH)
            instance.profile = profile
            CoachProfileExtra.objects.create(profile=profile, education="")


post_save.connect(user_profile, sender=get_user_model())
