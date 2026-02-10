from django.db import models

class Country(models.Model):
    cca3 = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    population = models.BigIntegerField(default=0)
    area = models.FloatField(default=0)
    flag_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
