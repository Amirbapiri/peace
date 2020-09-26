import datetime
import random
import string

from django.db import models


def get_random_string():
    letters = string.ascii_letters + string.digits + \
        str(datetime.datetime.now().timestamp())
    result = ''.join(random.choice(letters) for i in range(15))
    return result


def plan_image_upload_path(instance, filename):
    random_str = get_random_string()
    file_path = 'plans/{client_username}/{client_username}-{random_str}-{filename}'.format(
        client_username=instance.plan.client.username, random_str=random_str, filename=filename
    )
    return file_path


class ClientImage(models.Model):
    front = models.ImageField(
        upload_to=plan_image_upload_path, verbose_name="front image")
    side = models.ImageField(
        upload_to=plan_image_upload_path, verbose_name="side image")
    back = models.ImageField(
        upload_to=plan_image_upload_path, verbose_name="back image")

    def __str__(self):
        return str(self.pk)
