# Generated by Django 4.2.7 on 2023-12-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_id', models.IntegerField(primary_key=True, serialize=False)),
                ('std_name', models.CharField(max_length=5)),
            ],
        ),
    ]
