from dbm import error

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from hospital.views import *


def About(request):
    return render(request,"about.html")

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,"index.html")

def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
    try:
        if user.is_staff:
            login(request, user)
            redirect('home')
            error="no"
        else:
            error="yes"
    except:
        error="yes"
    d={'error':error}
    return render(request,"login.html",d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return render(request,"login.html")

def Contact(request):
    return render(request,"contact.html")

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc': doc}
    return render(request,"view_doctor.html",d)

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['mobile']
        sp = request.POST['special']
    try:
        Doctor.objects.create(name=n, mobiile=c, special=sp)
        error="no"
    except:
        error="yes"
    d={'error':error}
    return render(request,"view_doctor.html",d)

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor.html')
