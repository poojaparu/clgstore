from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newapp:add')
        else:
            messages.info(request,"invalid login")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
