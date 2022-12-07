from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vehicule(models.Model):
    type = models.CharField(max_length=50, choices=['v8','4x4'])
    capacite = models.IntegerField(null=True,blank=True)
    nombre_places = models.IntegerField(null=True,blank=True)


class Chauffeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s) du chauffeur")
    prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s) du chauffeur")
    date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
    telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
    adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True, blank=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s) du Client")
    prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s) du Client")
    date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
    telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
    adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")    
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")
    chauffeur = models.ManyToManyField(Chauffeur)


class Commentaire(models.Model):
    nom_personne = models.CharField(max_length=50, blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    date_publication = models.DateTimeField(auto_now=True, null=True)

class Livreur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s) du Livreur")
    prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s) du Livreur")
    date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
    telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
    adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")    
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")
    client = models.ManyToManyField(Client)

class Partenaire(models.Model):
    nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s)")
    type = models.CharField(max_length=50, choices=['Personne Physique','Personne Morale'])
    prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s)")
    date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
    telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
    adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")    
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")