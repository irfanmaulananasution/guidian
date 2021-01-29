from django.urls import path
from . import views

urlpatterns = [
    path('regTour/<int:regTourID>/<int:scheduleID>/booking', views.booking_form, name='booktour'),
    path('confirmation/<str:token>', views.confirmation, name='confirmation'),
    path('booking/<int:regTourID>/<int:scheduleID>', views.readBooking, name='readBooking'),
    path('booking/<int:bookingID>/delete', views.deleteBooking, name='deleteBooking')
]