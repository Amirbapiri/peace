from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Coach, Client
from sizes.models import Size

FOOD_NATURE_CHOICES = (
    ("VEGETARIAN", "گیاه‌خوار"),
    ("NONVEGETARIAN",  "با خوردن گوشت مشکلی ندارم.")
)


class Plan(models.Model):
    client = models.OneToOneField(
        Client, on_delete=models.DO_NOTHING, related_name="client")
    coach = models.OneToOneField(
        Coach, on_delete=models.DO_NOTHING, related_name="coach")
    size = models.OneToOneField(Size, on_delete=models.DO_NOTHING, null=True)
    food_nature = models.CharField(
        max_length=13, choices=FOOD_NATURE_CHOICES, default="NONVEGETARIAN")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.email
