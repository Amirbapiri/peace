# Generated by Django 3.1.1 on 2020-09-24 15:55

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20200924_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
    ]
