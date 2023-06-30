from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "POST":
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('todolist:main')
        else:
            return render(request, 'login.html')
    else: 
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return render(request, 'login.html')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('todolist:main')