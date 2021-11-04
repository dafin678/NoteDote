# Generated by Django 3.2.8 on 2021-11-04 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weekly_schedule', '0004_weekly_schedule_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_schedule',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
