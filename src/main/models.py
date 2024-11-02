import uuid
from django.db import models

from consts import CARS_BRANDS, TRANSMISSION_OPTIONS
from users.models import Profile, Location




class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=24, choices=CARS_BRANDS, default=None)
    model = models.CharField(max_length=64,)
    vin = models.CharField(max_length=17,)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24)
    description = models.TextField()
    engine = models.CharField(max_length=24,)
    transmission = models.CharField(
        max_length=24, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL)
    image = models.ImageField()