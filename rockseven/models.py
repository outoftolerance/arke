from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Received(models.Model):
    imei = models.CharField(max_length=16, validators=[MinLengthValidator(15)], default = '')
    sequence_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    timestamp_transmit = models.DateTimeField()
    latitude = models.DecimalField(max_digits = 11, decimal_places = 8)
    longitude = models.DecimalField(max_digits = 11, decimal_places = 8)
    circular_error_probable = models.DecimalField(max_digits=12, decimal_places = 4)
    data = models.TextField(2048)
