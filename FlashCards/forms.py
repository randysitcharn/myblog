from django import forms

class DeckForm(forms.Form):
    name = forms.CharField(label= 'Name')
    img_src = forms.ImageField(label='Image')
    img_alt = forms.CharField(label='Description de l\'image')
    desc = forms.CharField(label='Description du Deck')