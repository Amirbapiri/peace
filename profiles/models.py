import random
import string

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


def get_random_string():
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(10))
    return result


def upload_path(instance, filename):
    random_str = get_random_string()
    file_path = 'clients/{client_id}/{username}-{random_str}-{filename}'.format(
        client_id=instance.account.id, username=instance.account.username,  random_str=random_str, filename=filename
    )
    return file_path


def coach_image_path(instance, filename):
    random_str = get_random_string()
    file_path = "coaches/{coach_id}/{username}-{random_str}-{filename}".format(
        coach_id=instance.profile.account.id, username=instance.profile.account.username, random_str=random_str, filename=filename
    )
    return file_path


class Profile(models.Model):

    class Types(models.TextChoices):
        COACH = "COACH", "Coach"
        CLIENT = "CLIENT", "Client"

    type = models.CharField(verbose_name="Type", max_length=10,
                            choices=Types.choices, default=Types.CLIENT)

    location = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)

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
    image = models.ImageField(
        upload_to=coach_image_path, blank=True, null=True)
    panel_image = models.ImageField(
        upload_to=coach_image_path, blank=True, null=True)

    def __str__(self):
        return self.profile.account.email


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
