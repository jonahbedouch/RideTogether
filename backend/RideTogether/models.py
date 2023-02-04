from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    miles_traveled = models.DecimalField(default=0)
    sessions_hosted = models.IntegerField(default=0)
    sessions_joined = models.IntegerField(default=0)
    driver_rating = models.DecimalField(default=0)
    passenger_rating = models.DecimalField(default=0)

class Conversation(models.Model):
    users = models.ManyToManyField(User)

class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    user = models.ForeignKey(User)
    chat = models.ForeignKey(Conversation)

class Session(models.Model):
    passengers_max = models.IntegerField()
    start_dest = models.JSONField()
    end_dest = models.JSONField()
    route = models.JSONField()
    passengers = models.ManyToManyField(User)
    timestamp = models.DateTimeField()