# Generated by Django 4.1.3 on 2022-11-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
