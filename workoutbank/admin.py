from django.contrib import admin

from .models import WorkoutCategory, WorkoutItem


admin.site.register(WorkoutCategory)
admin.site.register(WorkoutItem)
