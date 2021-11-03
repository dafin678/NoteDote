# Generated by Django 3.2.7 on 2021-10-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
