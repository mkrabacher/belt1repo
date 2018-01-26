# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from ..users.models import *
# Create your models here.
class Trip(models.Model):
    desti = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    leader = models.ForeignKey(User, related_name='leading')
    travelers = models.ManyToManyField(User, related_name='trips')