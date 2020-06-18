'''
File: jitterbunk/views.py
Author: Neel Kishnani

This file defines the different views of the jitterbunk
application. Here we're able to pull up a feed of all
jitterbunks, send a bunk from one user to another, and
pull up the jitterbunk feed for a specific user.
'''

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile, Bunk
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q

def index(request):
    '''
    Landing page for jitterbunk. Here we
    display a full history of bunks.
    '''
    bunks = Bunk.objects.all()
    context = {'bunks': bunks}
    return render(request, 'jitterbunk/index.html', context)


def send_bunk(request):
    '''
    Here we will have a form through which
    people can specify who to send a bunk to/
    from.
    '''
    if request.POST:
        try:
            from_username = request.POST['from_user']
            to_username   = request.POST['to_user']

            from_user = User.objects.get(username=from_username)
            to_user   = User.objects.get(username=to_username)

            from_up = UserProfile.objects.get(user=from_user)
            to_up   = UserProfile.objects.get(user=to_user)

            bunk = Bunk(from_user=from_up, to_user=to_up, time=timezone.now())
            bunk.save()
            return HttpResponseRedirect('/jitterbunk/')

        except (KeyError, User.DoesNotExist):
            return render(request, 'jitterbunk/send_bunk.html', {
                'error_message':"Username not found."
            })

    return render(request, 'jitterbunk/send_bunk.html')


def view_individual_bunks(request, username):
    '''
    Given a specific username, we display the bunks sent
    to or sent from that user.
    '''
    u  = User.objects.get(username=username)
    up = UserProfile.objects.get(user=u)
    individual_bunks = Bunk.objects.filter(Q(from_user=up) | Q(to_user=up))
    context = {'individual_bunks':individual_bunks, 'username':username}
    return render(request, 'jitterbunk/individual.html', context)

