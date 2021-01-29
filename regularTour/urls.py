from django.urls import path
from .views import *

app_name = "regularTour"

urlpatterns = [
    path('listRegularTour/', listRegularTour, name='listRegularTour'),
    path('createRegularTour/', createRegularTour, name='createRegularTour'),
    path('updateRegularTour/<int:id>', updateRegularTour, name='updateRegularTour'),
    path('readRegularTour/<int:id>', readRegularTour, name='readRegularTour'),
    path('deleteRegularTour/<int:id>', deleteRegularTour, name='deleteRegularTour')
]
