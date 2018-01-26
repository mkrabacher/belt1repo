# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from datetime import datetime
import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

def index(request):
    context = {
        'users':User.objects.all(),
        'regForm':RegistrationForm(),
        'loginForm':LoginForm()
    }
    return render(request, 'users/index.html', context)

def registerUser(request):
    if request.method == "POST":
        response_form = RegistrationForm(request.POST)
        if response_form.is_valid():
            username = response_form.cleaned_data['username']
            name = response_form.cleaned_data['name']

        password =response_form.cleaned_data['password']
        pw_conf = response_form.cleaned_data['confirm_password']
        if password != pw_conf:
            response_form.errors['password_match'] = "Your passwords don't match."
        try:
            User.objects.get(username=username)
            response_form.errors['password_match'] = "username is already taken."
        except:
            pass
        if len(response_form.errors) > 0:
            for tag, error in response_form.errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')

        else:
            User.objects.create(username=username, name=name, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
            messages.add_message(request, messages.INFO, 'Success. Now log in.')
            return redirect('/')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.add_message(request, messages.INFO, 'username does not exist.')
            return redirect('/')

        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['curr_user_id'] = user.id
            return redirect('/travel')

def logout(request):
    request.session.clear()
    return redirect('/')