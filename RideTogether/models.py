from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    miles_traveled = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    sessions_hosted = models.IntegerField(default=0)
    sessions_joined = models.IntegerField(default=0)
    driver_rating = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    passenger_rating = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    phone_number = models.CharField(default="", max_length=20, blank=True, null=True)

class Session(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')
    passengers_max = models.IntegerField()
    start_dest = models.JSONField()
    end_dest = models.JSONField()
    original_route = models.JSONField()
    route = models.JSONField()
    passengers = models.JSONField(null=True, blank=True)
    timestamp = models.IntegerField()
    joinqueue = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.driver}: {self.start_dest}->{self.end_dest}, {self.timestamp}"

