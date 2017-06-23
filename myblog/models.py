# -*- coding: utf-8 -*-
from django.db import models

class card(models.Model):
    recto = models.TextField()
    verso = models.TextField()

class icard(models.Model):
    id_card=models.IntegerField()
    n=models.IntegerField()
    EF=models.IntegerField()
    I=models.IntegerField()
    date=models.DateField()

class deck(models.Model):
    name=models.CharField(max_length=64)
    cards=models.CommaSeparatedIntegerField(max_length=255)