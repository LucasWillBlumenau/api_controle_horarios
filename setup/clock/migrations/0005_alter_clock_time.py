# Generated by Django 4.1.3 on 2022-12-12 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0004_alter_clock_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clock',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 0, 54, 1, 725543)),
        ),
    ]
