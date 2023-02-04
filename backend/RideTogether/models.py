from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MapNode(models.Model):
    latitude = models.DecimalField()
    longitude = models.DecimalField()

class User(AbstractUser):
    miles_traveled = models.DecimalField(default=0)
    sessions_hosted = models.IntegerField(default=0)
    sessions_joined = models.IntegerField(default=0)
    driver_rating = models.DecimalField(default=0)
    passenger_rating = models.DecimalField(default=0)

class Conversation(models.Model):
    users = models.ManyToManyField(User)

class Message(models.Model):
    timestamp = models.DateTimeField()
    message = models.TextField()
    user = models.ForeignKey(User)
    chat = models.ForeignKey(Conversation)

class Session(models.Model):
    passengers_max = models.IntegerField()
    start_dest = models.ForeignKey(MapNode)
    end_dest = models.ForeignKey(MapNode)
    passengers = models.ManyToManyField(User)