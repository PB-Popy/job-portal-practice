from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def jobfeedPage(request):
    return render(request,'common/jobfeedPage.html')

def loginPage(request):
    if request.method=='POST':
        
        return render(request,'common/loginPage.html')

def signupPage(request):
    return render(request,'common/signupPage.html')

def logoutPage(request):
    return render(request,'common/logoutPage.html')
