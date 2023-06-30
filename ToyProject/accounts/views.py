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
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': '이미 존재하는 아이디입니다.'})
        
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'error': '비밀번호가 일치하지 않습니다.'})
    
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('todolist:main')