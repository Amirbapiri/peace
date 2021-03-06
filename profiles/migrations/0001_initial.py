# Generated by Django 3.1.1 on 2020-09-18 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('COACH', 'Coach'), ('CLIENT', 'Client')], default='CLIENT', max_length=10, verbose_name='Type')),
                ('location', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoachExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=20)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profiles.profile',),
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
            bases=('profiles.profile',),
        ),
    ]
