from django.shortcuts import render, redirect
from django.http import HttpResponse
from booking import forms, models
from .models import BookingModel
from schedule.models import RegTourScheduleModel
from regularTour.models import RegularTourModel
import random, string
from django.core.mail import send_mail
from django.contrib import messages

def get_token():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(64)))
    return result_str

def booking_form(request, regTourID, scheduleID):
    limit = False
    
    if request.method=="POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            tok = get_token()
            sched = RegTourScheduleModel.objects.get(id=scheduleID)
            
            if sched.slot>= int(form.data['participants']):
                book = models.BookingModel(
                    fullName = form.data['fullName'],
                    mail = form.data['mail'],
                    participants = form.data['participants'],
                    country = form.data['country'],
                    phone = form.data['phone'],
                    confirmed = False,
                    token = tok,
                    schedule = sched,
                )

                name = form.data['fullName']
                time = str(sched.startTime)
                destination = RegularTourModel.objects.get(id=regTourID).destination
                language = sched.language
                participants = str(form.data['participants'])

                message = 'Hello, ' + name + '! Thank you for registering to our tour. Here is your booking detail: \nName          : ' + name + '\nParticipants    : ' + participants + '\nDestination     : ' + destination + '\nStart Time       : ' + time + '\nLanguage        : ' + language + '\nPlease confirm your attendance by clicking the link below: \nhttp://guidian.herokuapp.com/confirmation/' + tok + '\n\nWe are looking forward to seeing you and adventuring together~ See ya! ヾ(•ω•`)o \nRegards, \n\nGuidian.'

                send_mail( 'Attendance Confirmation',
                message, 
                'guidian.rpl@gmail.com', 
                [form.data['mail']], 
                fail_silently=False, )

                sched.save()
                book.save()
                return render(request, 'booking/booking_success.html')
            else:
                limit = True
    else:
        form = forms.BookingForm()

    destination = RegularTourModel.objects.get(id=regTourID).destination
    sched = RegTourScheduleModel.objects.get(id=scheduleID)
    slot = sched.slot
    context = {
        'form' : form,
        'limit' : limit,
        'destination' : destination,
        'slot' : slot
    }
    return render(request, 'booking/booking_form.html', context)

def confirmation(request, token):
    book = BookingModel.objects.get(token=token)
    sched = book.schedule
    destination = sched.regularTour.destination
    date = sched.date
    time = sched.startTime
    if (book.confirmed==False):
        if request.method=="POST":
            book.confirmed = True
            sched.slot -= book.participants
            book.save()
            sched.save()
            return render(request, 'booking/success.html')
        
        context = {
            'book' : book,
            'destination' : destination,
            'date' : date,
            'time' : time
        }

        return render(request, 'booking/confirmation.html', context)
    else:
        return render(request, 'booking/success.html')

def readBooking(request, regTourID, scheduleID):
    sched = RegTourScheduleModel.objects.get(id=scheduleID)
    regTour = RegularTourModel.objects.get(id=regTourID)
    participants = BookingModel.objects.filter(schedule=sched)
    confirmed_participants = list()

    for i in participants:
        if i.confirmed:
            confirmed_participants.append(i)
    empty = False
    if (len(confirmed_participants)==0):
        empty = True
    
    context = {
        'confirmed_participants' : tuple(confirmed_participants),
        'time' : sched.startTime,
        'destination' : regTour.destination,
        'language' : sched.language,
        'slot' : sched.slot,
        'empty' : empty
    }
    return render(request, 'booking/read_booking.html', context)

def deleteBooking(request, bookingID):
    book = BookingModel.objects.get(id=bookingID)
    regTourID = book.schedule.regularTour.id
    schedID = book.schedule.id

    sched = RegTourScheduleModel.objects.get(id=schedID)
    participants = book.participants

    sched.slot += participants
    sched.save()
    book.delete()
    
    path = '/booking/'+str(regTourID)+'/'+str(schedID)
    return redirect(path)