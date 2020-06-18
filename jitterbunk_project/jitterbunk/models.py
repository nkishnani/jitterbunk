'''
File: jitterbunk/models.py
Author: Neel Kishnani

This file defines the database models for the
jitterbug project. Here we define a Bunk and a
UserProfile. A Bunk is the poking mechanism
and the UserProfile is an abstraction above the
default Django User.
'''

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''
    A single UserProfile object. Here we map the user
    one to one with the default Django user. We specify
    the photo as a string (URL of the photo).
    '''
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200)


class Bunk(models.Model):
    '''
    A single Bunk object. Here we define the metadata
    for the object, denoting who the Bunk is coming from,
    who it's going to, and what time it was sent.
    '''
    from_user = models.ForeignKey(UserProfile, related_name='bunks_sent')
    to_user   = models.ForeignKey(UserProfile, related_name='bunks_received')
    time      = models.DateTimeField('date published')

