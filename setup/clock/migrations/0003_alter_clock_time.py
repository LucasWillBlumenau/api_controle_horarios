# Generated by Django 4.1.3 on 2022-12-07 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0002_alter_clock_punch_type_alter_clock_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clock',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 0, 43, 0, 637711)),
        ),
    ]