from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save();
                messages.info(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching...")
            return redirect('registration')
        return redirect('/')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')



