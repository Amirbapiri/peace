from django.db import models

from accounts.models import Client


class Size(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE
    )
    height = models.CharField(max_length=30, blank=False, null=False)
    weight = models.CharField(max_length=30, blank=False, null=False)
    chest = models.CharField(max_length=30, blank=False, null=False)
    neck = models.CharField(max_length=30, blank=False, null=False)
    arm = models.CharField(max_length=30, blank=False, null=False)
    wrist = models.CharField(max_length=30, blank=False, null=False)
    waist = models.CharField(max_length=30, blank=False, null=False)
    hamstring = models.CharField(max_length=30, blank=False, null=False)
    calf = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.client.email + self.client.username
