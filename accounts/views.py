from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import Group


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('/')

    else:
        form = Signup()

    return render(request,'registration/sign_up.html',{'form':form})
