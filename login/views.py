from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return render(request, 'homepage/index.html')
    else :
        return redirect('login')

def loginUser(request):
    user = None

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('homepage')
        else :
            return render(request, 'login/login.html')

    if request.method == "POST":

        username_ = request.POST['username']
        password_ = request.POST['password']

        user = authenticate(request, username = username_, password = password_)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        else :
            return redirect('login')


    return render(request, 'login/login.html')

def logoutUser(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'login/logout.html')
        else :
            return redirect('login')

    if request.method == 'POST':
        if (request.POST['logout'] == 'Logout'):
            logout(request)

        return redirect('login')

    return render(request, 'login/logout.html')
