from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Deck
from .forms import DeckForm

def index(request):
    Decks=Deck.objects.all()
    return(render(request,'base.html',{'Decks':Decks}))

def formPage(request):
    DeckForm_Object=DeckForm()
    return(render(request,'Deckform.html',{'form':DeckForm_Object}))

def post_deck(request):
    form=DeckForm(request.POST, request.FILES)
    if form.is_valid():
        Deck_Object=Deck(
            name=form.cleaned_data['name'],
            img_src=form.cleaned_data['img_src'],
            img_alt=form.cleaned_data['img_alt'],
            desc=form.cleaned_data['desc']
            )
        Deck_Object.save()
    return(HttpResponseRedirect('/'))
