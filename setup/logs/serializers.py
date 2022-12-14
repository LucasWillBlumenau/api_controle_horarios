from rest_framework import serializers
from .models import Log
from users.serializers import UserSerializer


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ['log_type', 'user', 'collaborator']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for x in instance.CHOICES:
            if x[0] == instance.log_type:
                representation['log_type'] = x[1]
                break
        representation['user'] = UserSerializer(instance.user).data
        return representation
