from django.db import models

class VesselCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

class Vessel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()