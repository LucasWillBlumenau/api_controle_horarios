from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from .models import Clock


class ClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = ['punch_type']

        
class PunchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance=instance.user).data
        for x in instance.CHOICES:
            if x[0] == instance.punch_type: 
                representation['punch_type'] = x[1] 
                break   
        return representation
