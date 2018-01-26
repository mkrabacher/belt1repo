from __future__ import unicode_literals
from django.db import models
from .models import User
from django import forms
from datetime import *

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=3)
    name = forms.CharField(max_length=255, min_length=2)
    password = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=3)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)