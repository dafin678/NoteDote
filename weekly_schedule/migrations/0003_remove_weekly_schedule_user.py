# Generated by Django 3.2.8 on 2021-11-04 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekly_schedule', '0002_auto_20211029_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekly_schedule',
            name='user',
        ),
    ]
