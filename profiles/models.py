from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class Profile(models.Model):

    class Types(models.TextChoices):
        COACH = "COACH", "Coach"
        CLIENT = "CLIENT", "Client"

    type = models.CharField(verbose_name="Type", max_length=10,
                            choices=Types.choices, default=Types.CLIENT)

    location = models.CharField(max_length=50)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.location


# CoachProfile type and manager
class CoachProfileManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Profile.Types.COACH)


# Extra fields for type COACH
class CoachProfileExtra(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    education = models.CharField(max_length=20)


class CoachProfile(Profile):
    objects = CoachProfileManager()

    @property
    def extra(self):
        return self.coachprofileextra

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.COACH
        return super().save(*args, **kwargs)

# ClientProfile type and manager


class ClientProfileManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Profile.Types.CLIENT)


class ClientProfile(Profile):
    objects = ClientProfileManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Profile.Types.CLIENT
        return super().save(*args, **kwargs)


# Signals to save profile for coach and client depending on instance type
@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, **kwargs):
    if instance.type == Profile.Types.CLIENT:
        profile = Profile.objects.create(
            location="", job="", type=Profile.Types.CLIENT)
        instance.profile = profile
    elif instance.type == Profile.Types.COACH:
        profile = Profile.objects.create(
            location="", job="", type=Profile.Types.COACH)
        instance.profile = profile
        CoachProfileExtra.objects.create(profile=profile, education="")
