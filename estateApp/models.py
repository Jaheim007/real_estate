from ast import mod
from asyncio.windows_events import NULL
from django.db import models

class Sign(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=62)
    confirm_Password = models.CharField(max_length=62 )

def __str__(self):
    return self.nom

# Create your models here.
