# Generated by Django 4.1.1 on 2022-12-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='collaborator',
            field=models.CharField(default=1998, max_length=200),
            preserve_default=False,
        ),
    ]
