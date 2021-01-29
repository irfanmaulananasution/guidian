from django.db import models
from schedule.models import RegTourScheduleModel
# Create your models here.
class BookingModel(models.Model):
    fullName = models.CharField(max_length = 50)
    mail = models.EmailField(max_length=254)
    participants = models.IntegerField()
    country = models.CharField(max_length = 50)
    phone = models.IntegerField()
    confirmed = models.BooleanField()
    token = models.CharField(max_length=64)

    schedule = models.ForeignKey(
        RegTourScheduleModel,
        on_delete=models.CASCADE,
    )

    def getScheduleID(self):
        return self.schedule.id
    
    def getRegTourID(self):
        return self.schedule.regularTour.id