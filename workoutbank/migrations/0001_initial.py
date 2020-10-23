# Generated by Django 3.1.2 on 2020-10-15 16:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import workoutbank.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('target_muscles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=workoutbank.models.workout_image_upload_path, verbose_name='workout image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='workoutbank.workoutcategory')),
            ],
        ),
    ]