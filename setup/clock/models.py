from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Clock(models.Model):
    CHOICES = (
        (0, 'Entrada'),
        (1, 'Almoço'),
        (2, 'Retorno'),
        (3, 'Saída')
    )
    time = models.DateTimeField(default=datetime.now())
    punch_type = models.IntegerField(choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


