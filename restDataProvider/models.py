from django.db import models

# Create your models here.

class PointOfInterest(models.Model):
    title = models.CharField(max_length=200)
    lon = models.FloatField('Longitude', blank=True, null=True)
    lat = models.FloatField('Latitude', blank=True, null=True)
    description = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    deleted = models.BooleanField(default=True)
    mapsLink = models.URLField(null=True)


class Comments(models.Model):
    poi = models.ForeignKey(PointOfInterest)
    text = models.CharField(max_length=500)


