from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
]