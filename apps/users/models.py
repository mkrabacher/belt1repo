# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from datetime import *


class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    # def registerValid(response_form):
    #     if response_form.is_valid():
    #         username = response_form.cleaned_data['username']
    #         name = response_form.cleaned_data['name']

    #     password =response_form.cleaned_data['password']
    #     pw_conf = response_form.cleaned_data['confirm_password']
    #     if password != pw_conf:
    #         response_form.errors['password_match'] = "Your passwords don't match."
    #         return False
    #     try:
    #         User.objects.get(username=username)
    #         response_form.errors['password_match'] = "username is already taken."
    #         return False
    #     except:
    #         pass

    #     return True