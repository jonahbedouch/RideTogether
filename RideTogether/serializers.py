from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'miles-traveled', 'sessions-hosted', 'sessions-joined', 'driver-rating', 'passenger-rating']

class UIDSerializier(serializers.Serializer):
    user_id = serializers.IntegerField()

class TestSerializer(serializers.Serializer):
    message = serializers.CharField()