# Generated by Django 3.1.1 on 2020-09-26 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sizes', '0003_auto_20200926_1421'),
        ('plans', '0008_auto_20200926_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sizes.size'),
        ),
    ]
