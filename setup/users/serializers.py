from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job, Collaborator


class CollaboratorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collaborator
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', ]
