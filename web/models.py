from django.db import models
from django.contrib.auth.models import User
from .resources import cars,partenaires
# Create your models here.


class Vehicule(models.Model):
    type = models.IntegerField(choices=cars.CARS)
    capacite = models.IntegerField(null=True,blank=True)
    nombre_places = models.IntegerField(null=True,blank=True)
    photo = models.ImageField(upload_to='photos_vehicules/', null=True, blank=True)
   
    def __str__(self):
      return f"{self.type}"


class Chauffeur(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s) du chauffeur")
   prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s) du chauffeur")
   date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
   telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
   adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")
   vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True, blank=True)
   piece_jointe = models.FileField(upload_to='pieces_jointes/chauffeurs/')

   def __str__(self):
      return f"{self.nom} {self.prenom}"




class Client(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s) du Client")
   prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s) du Client")
   date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
   telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
   adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse") 
   chauffeur = models.ManyToManyField(Chauffeur, through='TransactionChauffeurClient')

   def __str__(self):
      return f"{self.nom} {self.prenom}"

class TransactionChauffeurClient(models.Model):
   chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
   client = models.ForeignKey(Client, on_delete=models.CASCADE)
   montant = models.IntegerField(null=True, blank=True)
   date_transaction = models.DateTimeField(auto_now=True)
   lieu = models.CharField(max_length=50, null=True, blank=True)


class Livreur(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)    
   nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s) du Livreur")
   prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s) du Livreur")
   date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
   telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
   adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")
   clients = models.ManyToManyField(Client, through='TransactionLivreurClient')
   piece_jointe = models.FileField(upload_to='pieces_jointes/livreurs/')

   def __str__(self):
      return f"{self.nom} {self.prenom}"

class TransactionLivreurClient(models.Model):
   livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE)
   client = models.ForeignKey(Client, on_delete=models.CASCADE)
   montant = models.IntegerField(null=True, blank=True)
   date_transaction = models.DateTimeField(auto_now=True)
   lieu = models.CharField(max_length=50, null=True, blank=True)



class Commentaire(models.Model):
   nom_personne = models.CharField(max_length=50, blank=True, null=True)
   contenu = models.TextField(blank=True, null=True)
   date_publication = models.DateTimeField(auto_now=True, null=True)


class Partenaire(models.Model):
   nom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom(s)")
   type = models.IntegerField(choices=partenaires.PERSONNES)
   prenom = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prénom(s)")
   date_naissance = models.DateField(max_length=100, null=True, blank=True, verbose_name="Date de naissance")
   telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Numero de telephone")
   adresse = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse")    
   email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")

   def __str__(self):
      return f"{self.nom} {self.prenom}"