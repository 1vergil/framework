# -*- coding: utf-8 -*-

from django.db import models

class User (models.Model):
    account=models.CharField(max_length=50)
    age=models.IntegerField()



