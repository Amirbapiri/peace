# Generated by Django 3.1.1 on 2020-10-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0011_auto_20200926_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Sent'),
        ),
    ]