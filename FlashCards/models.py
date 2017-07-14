from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length='255')
    img_src = models.ImageField(upload_to='Deck_images',default='media/default.png')
    img_alt = models.CharField(max_length='255')
    desc = models.CharField(max_length='255')

class DecksCards(models.Model):
    id_Deck = models.IntegerField()
    id_Card = models.IntegerField()