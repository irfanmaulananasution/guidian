from django.db import models
from regularTour.models import RegularTourModel
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class RegTourScheduleModel(models.Model):
    date = models.DateField()
    startTime = models.TimeField()
    slot = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(20)])
    language = models.CharField(max_length=50)
    tourGuide = models.CharField(max_length=50)
    regularTour = models.ForeignKey(
        RegularTourModel, 
        on_delete=models.CASCADE
    )
