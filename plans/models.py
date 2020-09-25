from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Coach, Client
from sizes.models import Size


class Plan(models.Model):
    client = models.OneToOneField(
        Client, on_delete=models.DO_NOTHING, related_name="client")
    coach = models.OneToOneField(
        Coach, on_delete=models.DO_NOTHING, related_name="coach")
    size = models.OneToOneField(Size, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.email
