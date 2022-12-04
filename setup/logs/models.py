from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    CHOICES = (
        (0, 'Create'),
        (1, 'Update'),
        (2, 'Delete'),
    )
    log_type = models.IntegerField(choices=CHOICES)
    user = models.ForeignKey(User, models.CASCADE)
    collaborator = models.CharField(max_length=200)
