# Generated by Django 3.2.8 on 2021-10-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
