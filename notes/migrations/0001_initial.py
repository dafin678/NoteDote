<<<<<<< HEAD
# Generated by Django 3.2.8 on 2021-11-04 05:37
=======
# Generated by Django 3.2.8 on 2021-11-04 08:50
>>>>>>> b1d73f9f6e47f784937506ac803563bf0ec98c3c

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, default='')),
            ],
        ),
    ]
