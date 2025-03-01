from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    api_id = models.IntegerField(unique=True)
    residents_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    type = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=50)
    origin_name = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    api_id = models.IntegerField(unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='characters')

    def __str__(self):
        return self.name