from .models import deck

#make a list of all decks from the database
def decks(request):
    decks=deck.objects.all()
    return(render(request,'deck.html',{'decks':decks}))