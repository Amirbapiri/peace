# Generated by Django 3.1.1 on 2020-09-18 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200918_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('meal_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
