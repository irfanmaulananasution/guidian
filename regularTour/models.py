from django.db import models

class RegularTourModel(models.Model):
    destination = models.CharField(max_length = 15)
    description = models.CharField(max_length = 300)
    distance = models.CharField(max_length = 5)
    duration = models.CharField(max_length = 10)
    meeting_point = models.CharField(max_length = 150)
    route = models.CharField(max_length = 100)
    photo = models.CharField(max_length=50)
    location_map = models.CharField(max_length=300)
