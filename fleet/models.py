from django.db import models
from django.core.validators import MinLengthValidator

class VehicleManager(models.Manager):
    def create_vehicle(self, name):
        vehicle = self.create(name = name)
        return vehicle

class Vehicle(models.Model):
    BALLOON = 'balloon'
    BUOY = 'buoy'
    
    VEHICLE_TYPE_CHOICES = [
        (BALLOON, 'Balloon'),
        (BUOY,'Buoy'),
    ]
    
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32, choices = VEHICLE_TYPE_CHOICES, default = BALLOON)
    callsign = models.CharField(max_length=32, default = '')
    imei = models.CharField(max_length=16, validators=[MinLengthValidator(15)], default = '')
    
    objects = VehicleManager()
    
    def __str__(self):
        return self.name
