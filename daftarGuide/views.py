from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import GuideModel
from django.contrib import messages
# Create your views here.

def daftarGuide(request):
    response={
        'guides': GuideModel.objects.all()
    }
    return render(request, 'daftarGuide/daftarGuide.html', response)

def createGuide(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        fullName = request.POST['fullName']
        language = request.POST['language']
        scheduleAvailable = request.POST['scheduleAvailable']
        description = request.POST['description']
        profilePicture = request.FILES['profilePicture']
        if (password1==password2):
            if (User.objects.filter(email=email).exists()):
                messages.info(request, "email is registered")
                return redirect('createGuide')
            else:
                user = User.objects.create_user(username=email, password=password1, email=email, first_name=fullName)
                user.save()
                guide = GuideModel.objects.create(user=user, fullName=fullName, language=language, scheduleAvailable=scheduleAvailable, description=description, profilePicture=profilePicture)
                guide.save()
        else:
            messages.info(request, "Password is not matching")
            return redirect('createGuide')
        
        return redirect('readGuide', username=email)
        
    return render(request, 'daftarGuide/createGuide.html')
    
def readGuide(request, username=""):
    userObject = User.objects.get(username=username)
    editButtonPermission = False;
    if (str(request.user)==str(userObject.username)) | request.user.is_superuser :
        editButtonPermission = True;
    response={
        'guide': GuideModel.objects.get(user=userObject),
        'editButtonPermission': editButtonPermission
    }
    return render(request, 'daftarGuide/readGuide.html', response)
    
def editGuide(request, username=""):
    username=request.POST['username'] if username=="" else username
    user = User.objects.get(username=username)
    guide = GuideModel.objects.get(user=user)
    
    if request.method == 'POST':
        guide.fullName = request.POST['fullName']
        guide.language = request.POST['language']
        guide.scheduleAvailable = request.POST['scheduleAvailable']
        guide.description = request.POST['description']
        guide.profilePicture = request.FILES.get('profilePicture', guide.profilePicture)
        guide.save()
        
        return redirect('readGuide', username=username)
    
    
    response={
        'guide': guide
    }
    return render(request, 'daftarGuide/editGuide.html', response)