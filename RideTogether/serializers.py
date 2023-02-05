from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    def create(self, data):
        print(data)
        user = User.objects.create_user(**data)
        return user
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number','miles_traveled', 'sessions_hosted', 'sessions_joined', 'driver_rating', 'passenger_rating']

class UIDSerializier(serializers.Serializer):
    user_id = serializers.IntegerField()

class SessionSerializer(serializers.ModelSerializer):
    passengers = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Session
        fields = ['id', 'driver', 'passengers_max', 'start_dest', 'end_dest', 'original_route', 'route', 'passengers', 'timestamp']

class PublicSessionSerializer(serializers.ModelSerializer):
    passengers = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Session
        fields = ['id', 'driver', 'passengers_max', 'start_dest', 'end_dest', 'original_route', 'passengers', 'timestamp']


