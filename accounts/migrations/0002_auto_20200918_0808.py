# Generated by Django 3.1.1 on 2020-09-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.account',),
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.account',),
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('COACH', 'Coach'), ('CLIENT', 'Client')], default='CLIENT', max_length=10, verbose_name='Type'),
        ),
    ]
