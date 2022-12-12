from django.db import models
from django.contrib.auth.models import User
   

class Job(models.Model):

    name = models.CharField(max_length=60, null=False)
    description = models.TextField(null=False)


    def __str__(self):
        return self.name


class Collaborator(models.Model):

    firstname = models.CharField(max_length=45, null=False)
    lastname = models.CharField(max_length=60, null=False)
    age = models.IntegerField(null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    date_of_birth = models.DateField(null=False)
    working_hours = models.CharField(max_length=15, null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)

