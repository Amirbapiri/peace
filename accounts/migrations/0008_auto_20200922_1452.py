# Generated by Django 3.1.1 on 2020-09-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200921_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('COACH', 'Coach'), ('CLIENT', 'Client')], max_length=10, verbose_name='Type'),
        ),
    ]
