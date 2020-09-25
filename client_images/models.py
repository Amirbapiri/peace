from django.db import models


class ClientImage(models.Model):
    front = models.ImageField(upload_to="")
    side = models.ImageField(upload_to="")
    back = models.ImageField(upload_to="")
