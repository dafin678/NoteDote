<<<<<<< HEAD
# Generated by Django 3.2.8 on 2021-11-04 14:04
=======
# Generated by Django 3.2.8 on 2021-11-04 16:01
>>>>>>> 449bdb74c0da589a4a264cc37236cad9b9801e4e

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekly_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('day', models.CharField(max_length=15)),
                ('start_time', models.TimeField(null=True)),
                ('due_time', models.TimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
