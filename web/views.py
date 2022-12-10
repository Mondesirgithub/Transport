from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Chauffeur, Livreur, Client
from django.contrib import messages
from web.forms import (ChauffeurRegisterForm,LivreurRegisterForm,
                        ClientRegisterForm, LoginForm,ChauffeurUpdateForm,
                        ChauffeurProfilForm, LivreurUpdateForm, LivreurProfilForm,
                        ClientUpdateForm, ClientProfilForm)
# Create your views here.

def index(request):
   return render(request, "web/index.html")

def contact(request):
   return render(request, "web/contact.html")

def logoutUser(request):
   logout(request)
   return redirect('index')


def registerChauffeur(request):
      form = ChauffeurRegisterForm()
      chauffeur = False

      if request.method == 'POST':
         form = ChauffeurRegisterForm(request.POST)      
         if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            chauffeur = Chauffeur.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)

            request.session['nom_chauffeur'] =  chauffeur.nom
            request.session['prenom_chauffeur'] =  chauffeur.prenom
            request.session['statusChauffeur'] =  1
            login(request, user)

            return redirect('index')


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
            livreur = Livreur.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)

            request.session['nom_livreur'] =  livreur.nom
            request.session['prenom_livreur'] =  livreur.prenom
            request.session['statusLivreur'] =  1
            login(request, user)

            return redirect('index')

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
            client = Client.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)  
            
            request.session['nom_client'] =  client.nom
            request.session['prenom_client'] =  client.prenom
            request.session['statusClient'] =  1
            login(request, user)

            return redirect('index')

      context = {
         'form':form
      }

      return render(request, 'web/registerClient.html', context)

# ---------LOGIN------------


def loginChauffeur(request):
      form = LoginForm()
      message = ""
      if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
               chauffeur = Chauffeur.objects.get(user=user)
               login(request, user)
               request.session['nom_chauffeur'] =  chauffeur.nom
               request.session['prenom_chauffeur'] =  chauffeur.prenom
               request.session['statusChauffeur'] =  1
               return redirect('index')

            else:
               message = 'aucun chauffeur trouvé, username et/ou mot de passe incorrect'

      context = {
         'form':form,
         'message':message
      }

      return render(request, 'web/loginChauffeur.html', context)



def loginLivreur(request):
      form = LoginForm()
      message = ""
      if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
               livreur = Livreur.objects.get(user=user)
               login(request, user)
               request.session['nom_livreur'] =  livreur.nom
               request.session['prenom_livreur'] =  livreur.prenom
               request.session['statusLivreur'] =  1
               return redirect('index')

            else:
               message = 'aucun livreur trouvé, username et/ou mot de passe incorrect'

      context = {
         'form':form,
         'message':message
      }
      return render(request, 'web/loginLivreur.html', context)

   
def loginClient(request):
      form = LoginForm()
      message = ""
      if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
               client = Client.objects.get(user=user)
               login(request, user)
               request.session['nom_client'] =  client.nom
               request.session['prenom_client'] =  client.prenom
               request.session['statusClient'] =  1
               return redirect('index')

            else:
               message = 'aucun client trouvé, username et/ou mot de passe incorrect'

      context = {
         'form':form,
         'message':message
      }

      return render(request, 'web/loginClient.html', context)



def editChauffeur(request):
    user = request.user
    chauffeur = Chauffeur.objects.get(user=user)
    form = ChauffeurUpdateForm(instance=chauffeur)
    form2 = ChauffeurProfilForm(instance=user)

    if request.method == "POST":
        form = ChauffeurUpdateForm(request.POST, instance = chauffeur)
        form2 = ChauffeurProfilForm(request.POST, instance = user)
        if form.is_valid() and form2.is_valid():
            user = form2.save(commit=False)
            user.username = user.email
            user.save()
            chauffeur = form.save()
            login(request, user)
            request.session['nom_chauffeur'] =  chauffeur.nom
            request.session['prenom_chauffeur'] =  chauffeur.prenom
            request.session['statusChauffeur'] =  1
            return redirect('index')

    context ={
      'form':form,
      'form2':form2
      }
    return render(request, 'web/profile_chauffeur.html', context)


def editLivreur(request):
    user = request.user
    livreur = Livreur.objects.get(user=user)
    form = LivreurUpdateForm(instance=livreur)
    form2 = LivreurProfilForm(instance=user)

    if request.method == "POST":
        form = LivreurUpdateForm(request.POST, instance = livreur)
        form2 = LivreurProfilForm(request.POST, instance = user)
        if form.is_valid() and form2.is_valid():
            user = form2.save(commit=False)
            user.username = user.email
            user.save()
            livreur = form.save()
            login(request, user)
            request.session['nom_livreur'] =  livreur.nom
            request.session['prenom_livreur'] =  livreur.prenom
            request.session['statusLivreur'] =  1
            return redirect('index')

    context ={
      'form':form,
      'form2':form2
      }
    return render(request, 'web/profile_livreur.html', context)

   
def editClient(request):
    user = request.user
    client = Client.objects.get(user=user)
    form = ClientUpdateForm(instance=client)
    form2 = ClientProfilForm(instance=user)

    if request.method == "POST":
        form = ClientUpdateForm(request.POST, instance = client)
        form2 = ClientProfilForm(request.POST, instance = user)
        if form.is_valid() and form2.is_valid():
            user = form2.save(commit=False)
            user.username = user.email
            user.save()
            client = form.save()
            login(request, user)
            request.session['nom_client'] = client.nom
            request.session['prenom_client'] = client.prenom
            request.session['statusClient'] =  1
            return redirect('index')

    context ={
      'form':form,
      'form2':form2
      }
    return render(request, 'web/profile_client.html', context)