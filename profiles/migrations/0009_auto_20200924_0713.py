# Generated by Django 3.1.1 on 2020-09-24 07:13

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20200924_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to=profiles.models.upload_path),
        ),
    ]
