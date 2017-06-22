from .models import deck
from django.shortcuts import render

#make a list of all decks from the database
def decks(request):
    decks=deck.objects.all()
    return(render(request,'decks.html',{'decks':decks}))
