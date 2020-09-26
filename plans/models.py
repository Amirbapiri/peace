from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Coach, Client
from sizes.models import Size
from client_images.models import ClientImage

FOOD_NATURE_CHOICES = (
    ("VEGETARIAN", "گیاه‌خوار"),
    ("NONVEGETARIAN",  "با خوردن گوشت مشکلی ندارم.")
)


class Plan(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING, related_name="client")
    coach = models.ForeignKey(
        Coach, on_delete=models.DO_NOTHING, related_name="coach")
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, null=True)
    image = models.ForeignKey(
        ClientImage, on_delete=models.DO_NOTHING, null=True)
    food_nature = models.CharField(
        max_length=13, choices=FOOD_NATURE_CHOICES, default="NONVEGETARIAN")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.email
