import random
import string
import datetime

from django.db import models

from django.contrib.postgres.fields import ArrayField


def get_random_string():
    letters = string.ascii_letters + string.digits + \
        str(datetime.datetime.now().timestamp())
    result = ''.join(random.choice(letters) for i in range(15))
    return result


def workout_image_upload_path(instance, filename):
    random_str = get_random_string()
    file_path = "workouts/{category}/{title}-{random_str}-{filename}".format(
        category=instance.category.title,
        title=instance.title,
        random_str=random_str,
        filename=filename
    )
    return file_path


def workout_cat_image_path(instance, filename):
    random_str = get_random_string()
    file_path = "workouts/categories/{title}-{random_str}-{filename}".format(
        title=instance.title,
        random_str=random_str,
        filename=filename
    )
    return file_path


class WorkoutCategory(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        verbose_name="category image", upload_to=workout_cat_image_path, default="")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class WorkoutItem(models.Model):
    category = models.ForeignKey(WorkoutCategory, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=False, null=False)
    target_muscles = ArrayField(models.CharField(max_length=255), blank=False)
    description = models.TextField()
    image = models.ImageField(
        verbose_name="workout image", upload_to=workout_image_upload_path)

    def __str__(self):
        return self.title
