from django.db import models
from django.contrib.auth.models import User
import os

def get_image_path(instance, filename):
    fileExtension = filename.split(".")[-1]
    newFileName = str(instance.user.email) + "." + fileExtension
    return os.path.join('profilePicture', newFileName)

class GuideModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullName = models.CharField(max_length=30)
    language = models.CharField(max_length=150)
    scheduleAvailable = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    profilePicture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    totalTour = models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return self.user.email
    
# Create your models here.
