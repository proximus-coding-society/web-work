# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .conf import *

class user_profile(User):
    gender= models.CharField(max_length=10 , choices=GENDER)
    # email_regex=RegexValidator(email_regex=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    Stream = models.CharField(max_length= 100 , choices=STREAM)
    year = models.CharField(max_length=10 , choices=YEAR)

    #optional
    user_domain= models.CharField(max_length=200)















