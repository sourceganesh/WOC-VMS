from django.db import models
from accounts.models import Account
from datetime import datetime

# Create your models here.

class Vehicle(models.Model):
    vehicle_number      = models.CharField(max_length=15)
    vehicle_owner       = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_number

class VehicleLogs(models.Model):
    entry_time          = models.DateTimeField(default=datetime.now)
    exit_time           = models.DateTimeField(blank=True)
    has_exited          = models.BooleanField(default=False)
    vehicle             = models.ForeignKey(Vehicle, on_delete=models.PROTECT)

    def __str__(self):
        return self.vehicle.vehicle_number + str(self.entry_time)