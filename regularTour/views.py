from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .forms import CreateRegularTourForm, UpdateRegularTourForm
from .models import RegularTourModel
from django.db.models import Q
from datetime import datetime

def listRegularTour(request):
    lists = RegularTourModel.objects.all()
    response = {
        'lists': lists
    }
    return render(request, 'regularTour/listRegularTour.html', response)

def readRegularTour(request, id):
    regTourObj = RegularTourModel.objects.get(id=id)
    idRegTour = RegularTourModel.objects.filter(id=id)

    listSchedule = regTourObj.regtourschedulemodel_set.all()
    now = datetime.now()
    listSchedule = listSchedule.filter(
        Q(date=now.date(),startTime__gte=now.time())|
        Q(date__gt=now.date())).order_by('date','-startTime')

    response = {
        'idRegTour': idRegTour,
        'listSchedule': listSchedule
    }
    return render(request, 'regularTour/readRegularTour.html', response)

def createRegularTour(request):
    if request.method == 'POST':
        form = CreateRegularTourForm(request.POST)
        
        if form.is_valid():
            createRegularTour = RegularTourModel(
                destination = form.data['destination'],
                description = form.data['description'],
                distance = form.data['distance'],
                duration = form.data['duration'],
                meeting_point = form.data['meeting_point'],
                route = form.data['route'],
                photo = form.data['photo'],
                location_map = form.data['location_map']
            )
            createRegularTour.save()
            return redirect('../listRegularTour/')
    
    else:
        form = CreateRegularTourForm()
    
    create_content = {
        'form': form
    }
    return render(request, 'regularTour/createRegularTour.html', create_content)

def updateRegularTour(request, id):
    regTour = RegularTourModel.objects.get(id=id)

    if request.method == 'POST':
        form = UpdateRegularTourForm(request.POST)
        
        if form.is_valid():
            regTour.destination = form.data['destination']
            regTour.description = form.data['description']
            regTour.distance = form.data['distance']
            regTour.duration = form.data['duration']
            regTour.meeting_point = form.data['meeting_point']
            regTour.route = form.data['route']
            regTour.photo = form.data['photo']
            regTour.location_map = form.data['location_map']
            regTour.save()
            return redirect('../listRegularTour/')
    
    form = UpdateRegularTourForm({
        'destination': regTour.destination,
        'description': regTour.description,
        'distance': regTour.distance,
        'duration': regTour.duration,
        'meeting_point': regTour.meeting_point,
        'route': regTour.route,
        'photo': regTour.photo,
        'location_map': regTour.location_map
    })
    
    update_content = {
        'regTour': regTour,
        'form': form
    }
    return render(request, 'regularTour/updateRegularTour.html', update_content)

def deleteRegularTour(request, id):
    regTour = RegularTourModel.objects.get(id=id)
    regTour.delete()
    return redirect('../listRegularTour/')