from django.shortcuts import render, redirect
from .forms import CreateScheduleForm, UpdateScheduleForm
from .models import RegTourScheduleModel, RegularTourModel
from daftarGuide.models import GuideModel
from django.db.models import Q
from datetime import datetime
from django.db.models import F
from django.contrib.auth.models import User, auth

def manage(request, id_reg_tour):
    if request.user.is_authenticated == False:
        return redirect('/auth/login')
        
    this_reg_tour = RegularTourModel.objects.get(id=id_reg_tour)
    list_schedule = this_reg_tour.regtourschedulemodel_set.all()
    
    now = datetime.now()
    list_schedule = list_schedule.filter(
        Q(date=now.date(),startTime__gte=now.time())|
        Q(date__gt=now.date())).order_by('date','-startTime')

    context = {
        'id_reg_tour' : id_reg_tour,
        'destination' : this_reg_tour.destination,
        'list_schedule' : list_schedule
    }
    return render(request, 'schedule/manage_schedule.html', context)

def create(request, id_reg_tour):
    if request.user.is_authenticated == False:
        return redirect('/auth/login')

    this_reg_tour = RegularTourModel.objects.get(id=id_reg_tour)
    if request.method == "POST":
        form = CreateScheduleForm(request.POST)
        if form.is_valid(): 
            tourGuide="-"
            if form.data['tourGuide'] != "" :
                tourGuide = str(GuideModel.objects.all()[int(form.data['tourGuide'])-2])
        
            sched = RegTourScheduleModel(
                date = form.data['date'],
                startTime = form.data['startTime'],
                slot = form.data['slot'],
                language = form.data['language'],
                tourGuide = tourGuide,
                regularTour = this_reg_tour
            )
            if str(sched.tourGuide).find('@') > 0 :
                guideUser = User.objects.get(username=str(sched.tourGuide))
                GuideModel.objects.filter(user = guideUser).update(totalTour = F('totalTour')+1)
            sched.save()
            return redirect('/manageSchedule/{}'.format(id_reg_tour))

    form = CreateScheduleForm()
    context = {
        'id_reg_tour' : id_reg_tour,
        'destination' : this_reg_tour.destination,
        'form' : form
    }
    return render(request, 'schedule/create_schedule.html', context)

def update(request, id_reg_tour, id_schedule):
    if request.user.is_authenticated == False:
        return redirect('/auth/login')

    this_reg_tour = RegularTourModel.objects.get(id=id_reg_tour)
    current_schedule = RegTourScheduleModel.objects.get(id=id_schedule)
    if request.method == "POST":
        form = UpdateScheduleForm(request.POST)
        if form.is_valid():
            tourGuide="-"
            if form.data['tourGuide'] != "" :
                tourGuide = str(GuideModel.objects.all()[int(form.data['tourGuide'])-2])
            if str(current_schedule.tourGuide).find('@') > 0 :
                guideUser = User.objects.get(username=str(current_schedule.tourGuide))
                GuideModel.objects.filter(user = guideUser).update(totalTour = F('totalTour')-1)
            current_schedule.date = form.data['date']
            current_schedule.startTime = form.data['startTime']
            current_schedule.slot = form.data['slot']
            current_schedule.language = form.data['language']
            current_schedule.tourGuide = tourGuide
            current_schedule.regularTour = this_reg_tour
            
            if str(current_schedule.tourGuide).find('@') > 0 :
                guideUser = User.objects.get(username=str(current_schedule.tourGuide))
                GuideModel.objects.filter(user = guideUser).update(totalTour = F('totalTour')+1)
            current_schedule.save()
            

            return redirect('/manageSchedule/{}'.format(id_reg_tour))

    form = UpdateScheduleForm({
        'date' : current_schedule.date,
        'startTime' : current_schedule.startTime,
        'slot' : current_schedule.slot,
        'language' : current_schedule.language,
        'tourGuide' : current_schedule.tourGuide
    })
    context = {
        'id_reg_tour' : id_reg_tour,
        'destination' : this_reg_tour.destination,
        'form' : form
    }
    return render(request, 'schedule/update_schedule.html', context)

def delete(request, id_reg_tour, id_schedule):
    if request.user.is_authenticated == False | request.user.is_superuser == False:
        return redirect('/auth/login')

    current_schedule = RegTourScheduleModel.objects.get(id=id_schedule)
    current_schedule.delete()
    if str(current_schedule.tourGuide).find('@') > 0 :
        guideUser = User.objects.get(username=str(current_schedule.tourGuide))
        GuideModel.objects.filter(user = guideUser).update(totalTour = F('totalTour')-1)
    return redirect('/manageSchedule/{}'.format(id_reg_tour)) 