'''
File:
Author:

This file defines
'''

from django.db import models
from django.contrib.auth.models import User

class Bunk(models.Model):
    '''
    '''
    from_user = models.CharField(max_length=200)
    to_user   = models.CharField(max_length=200)
    time      = models.DateTimeField('date published')

    def __str__(self):
        return self.from_user + " to " + self.to_user


class UserProfile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
