from django.db import models

class Profil(models.Model):
    nom = models.CharField(max_length=255, blank=False, default='')
    prenom = models.CharField(max_length=255, blank=False, default='')
    age = models.IntegerField()
    email = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=255, blank=False, default='')

class Cluster(models.Model):
    idUser = models.IntegerField()
    idProduct = models.CharField(max_length=255, blank=False, default='')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    classe = models.CharField(max_length=255, blank=False, default='')