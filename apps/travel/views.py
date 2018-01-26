# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import *
from django.contrib import messages
from datetime import datetime
from models import *
from django.shortcuts import render, redirect

# Create your views here.
def travel(request):
    if 'curr_user_id' not in request.session:
        return redirect('/')
    context = {
        'curr_user':User.objects.get(id=request.session['curr_user_id']),
        'userTrips':Trip.objects.filter(travelers__id=request.session['curr_user_id'])|Trip.objects.filter(leader__id=request.session['curr_user_id']),
        'otherTrips':Trip.objects.exclude(leader__id=request.session['curr_user_id']).exclude(travelers__id=request.session['curr_user_id']),
    }
    return render(request, 'travel/dashboard.html', context)

def newTrip(request):
    if 'curr_user_id' not in request.session:
        return redirect('/')
    return render(request, 'travel/newTrip.html')

def createTrip(request):
    if 'curr_user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        desti = request.POST['desti']
        descr = request.POST['descr']
        start = request.POST['start']
        end = request.POST['end']
        currDate = datetime.now().strftime("%Y-%m-%d")

        if start > end:
            messages.add_message(request, messages.INFO, 'Start date must be after today!')
            return redirect('newTrip/')
        elif currDate > start:
            messages.add_message(request, messages.INFO, 'You cannot end your trip before it starts! thats a defeatist attitude.')
            return redirect('newTrip/')

        user = User.objects.get(id=request.session['curr_user_id'])
        Trip.objects.create(desti=desti, descr=descr, start=start, end=end, leader=user)
        return redirect('/travel')

def destination(request, number):
    if 'curr_user_id' not in request.session:
        return redirect('/')
    context = {
        'trip':Trip.objects.get(id=number),
        'otherTravelers':User.objects.filter(trips__id=number)
    }
    return render(request, 'travel/destination.html', context)

def join(request, number):
    if 'curr_user_id' not in request.session:
        return redirect('/')
    trip = Trip.objects.get(id=number)
    user = User.objects.get(id=request.session['curr_user_id'])
    trip.travelers.add(user)

    return redirect('/travel')