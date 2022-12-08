from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Chauffeur, Livreur, Client
from web.forms import ChauffeurRegisterForm,LivreurRegisterForm, ClientRegisterForm
# Create your views here.

def index(request):
   return render(request, "web/index.html")

def contact(request):
   return render(request, "web/contact.html")


def registerChauffeur(request):
      form = ChauffeurRegisterForm()

      if request.method == 'POST':
         form = ChauffeurRegisterForm(request.POST)      
         if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            Chauffeur.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)

      context = {
         'form':form
      }

      return render(request, 'web/registerChauffeur.html', context)


def registerLivreur(request):
      form = LivreurRegisterForm()

      if request.method == 'POST':
         form = LivreurRegisterForm(request.POST)      
         if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            Livreur.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)

      context = {
         'form':form
      }

      return render(request, 'web/registerLivreur.html', context)


def registerClient(request):
      form = ClientRegisterForm()

      if request.method == 'POST':
         form = ClientRegisterForm(request.POST)      
         if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            Client.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)

      context = {
         'form':form
      }

      return render(request, 'web/registerClient.html', context)
