# Generated by Django 4.2.7 on 2023-12-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='std_info',
            field=models.URLField(default='https://tec.com'),
        ),
    ]
