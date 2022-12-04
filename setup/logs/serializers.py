from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ['log_type', 'user', 'collaborator']