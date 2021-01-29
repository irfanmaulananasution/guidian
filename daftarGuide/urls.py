from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftarGuide, name='daftarGuide'),
    path('createGuide', views.createGuide, name='createGuide'),
    path('readGuide/<username>/', views.readGuide, name='readGuide'),
    path('editGuide/', views.editGuide, name='editGuide'),
    path('editGuide/<username>/', views.editGuide),
]
