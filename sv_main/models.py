from django.db import models

class VesselCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels_cats/" ,blank=True)
    description = models.TextField()

class Vessel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels/" , blank=True)
    description = models.TextField()
    # category = 