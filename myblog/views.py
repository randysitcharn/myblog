# -*- coding: utf-8 -*-
from .models import *
from django.shortcuts import render

#make a list of all decks from the database
def decks(request):
    decks=deck.objects.all()
    return(render(request,'decks.html',{'decks':decks}))

#display the id=1 card in card.html
def display_card(request):
    id1card=card.objects.get(id=1)
    return(render(request,'card.html',{'card':id1card}))

