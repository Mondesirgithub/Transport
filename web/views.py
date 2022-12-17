from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Chauffeur, Livreur, Client
from web.forms import (ChauffeurRegisterForm,LivreurRegisterForm,
                        ClientRegisterForm, LoginForm,ChauffeurUpdateForm,
                        ChauffeurProfilForm, LivreurUpdateForm, LivreurProfilForm,
                        ClientUpdateForm, ClientProfilForm)
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
   return render(request, "web/index.html")

def loginRequired(request):
   return render(request , "web/loginRequired.html")

@login_required
def map(request):
   if request.method == 'POST':
      try:
         chauffeur = Chauffeur.objects.get(user=request.user)
         chauffeur.latitude = float(request.POST['latitude'])
         chauffeur.longitude = float(request.POST['longitude'])
         chauffeur.save()
      except:
         try:
            livreur = Livreur.objects.get(user=request.user)         
            livreur.latitude = float(request.POST['latitude'])
            livreur.longitude = float(request.POST['longitude'])
            livreur.save()
         except:
            try:
               client = Client.objects.get(user=request.user)            
               client.latitude = float(request.POST['latitude'])
               client.longitude = float(request.POST['longitude'])
               client.save() 
            except:
               pass
   
   return render(request, "web/map.html")

@login_required
def map_suivi_users(request):
   livreurs = Livreur.objects.filter(longitude__gt=0.0).exclude(latitude=0.0, longitude=0.0)
   chauffeurs = Chauffeur.objects.filter(longitude__gt=0.0).exclude(latitude=0.0, longitude=0.0)
   clients = Client.objects.filter(longitude__gt=0.0).exclude(latitude=0.0, longitude=0.0)
   
   print(livreurs)
   
   context = {
      'livreurs':livreurs,
      'chauffeurs':chauffeurs,
      'clients':clients
   }

   return render(request , 'web/map_suivi_users.html', context)


@login_required
def suivi_user_chauffeur(request, pk):
   chauffeur = Chauffeur.objects.get(pk=pk)
   context = {
      'chauffeur':chauffeur
   }
   return render(request , 'web/suivi_user_chauffeur.html', context)


@login_required
def suivi_user_livreur(request, pk):   
   livreur = Livreur.objects.get(pk=pk)
   context = {
      'livreur':livreur
   }
   return render(request , 'web/suivi_user_livreur.html', context)


@login_required
def suivi_user_client(request, pk):   
   client = Client.objects.get(pk=pk)
   context = {
      'client':client
   }
   return render(request , 'web/suivi_user_client.html', context)


def getDataChauffeur(request, pk):
   chauffeur = Chauffeur.objects.filter(pk=pk)
   return JsonResponse({'chauffeur': list(chauffeur.values())})

def getDataLivreur(request, pk):
   livreur = Livreur.objects.filter(pk=pk)
   return JsonResponse({'livreur': list(livreur.values())})

def getDataClient(request, pk):
   client = Client.objects.filter(pk=pk)
   return JsonResponse({'client': list(client.values())})


def contact(request):
   return render(request, "web/contact.html")


def about(request):
   return render(request, "web/about-us.html")

def faq(request):
   return render(request, "web/faq.html")


def donneesFinancieres(request):
   return render(request, "web/donneesFinancieres.html")

def logoutUser(request):
   messages.info(request, 'Déconnexion réussie')
   logout(request)
   return redirect('index')


def registerChauffeur(request):
      form = ChauffeurRegisterForm()

      if request.method == 'POST':
         form = ChauffeurRegisterForm(request.POST, request.FILES)      
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
               piece_jointe = form.cleaned_data['piece_jointe'],
               user=user)

            request.session['nom_chauffeur'] =  chauffeur.nom
            request.session['prenom_chauffeur'] =  chauffeur.prenom
            request.session['statusChauffeur'] =  1
            login(request, user)
            messages.success(request, 'Création du compte réussie 🏆')
            return redirect('index')


      context = {
         'form':form
      }

      return render(request, 'web/registerChauffeur.html', context)


def registerLivreur(request):
      form = LivreurRegisterForm()

      if request.method == 'POST':
         form = LivreurRegisterForm(request.POST, request.FILES)      
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
               piece_jointe = form.cleaned_data['piece_jointe'],
               user=user)

            request.session['nom_livreur'] =  livreur.nom
            request.session['prenom_livreur'] =  livreur.prenom
            request.session['statusLivreur'] =  1
            login(request, user)
            messages.success(request, 'Création du compte réussie 🏆')
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
            messages.success(request, 'Création du compte réussie 🏆')
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
               try:
                  chauffeur = Chauffeur.objects.get(user=user)               
                  login(request, user)
                  request.session['nom_chauffeur'] =  chauffeur.nom
                  request.session['prenom_chauffeur'] =  chauffeur.prenom
                  request.session['statusChauffeur'] =  1
                  messages.success(request, 'Connexion réussie !!!')
                  return redirect('index')
               except:
                  messages.error(request, 'aucun chauffeur trouvé, username et/ou mot de passe incorrect')

            else:
               messages.error(request, 'aucun chauffeur trouvé, username et/ou mot de passe incorrect')

      context = {
         'form':form,
         'message':message
      }

      return render(request, 'web/loginChauffeur.html ', context)



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
               try:
                  livreur = Livreur.objects.get(user=user)
                  login(request, user)
                  request.session['nom_livreur'] =  livreur.nom
                  request.session['prenom_livreur'] =  livreur.prenom
                  request.session['statusLivreur'] =  1
                  messages.success(request, 'Connexion réussie !!!')
                  return redirect('index')
               except:
                  messages.error(request, 'aucun livreur trouvé, username et/ou mot de passe incorrect')

            else:
               messages.error(request, 'aucun livreur trouvé, username et/ou mot de passe incorrect')


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
               try:
                  client = Client.objects.get(user=user)
                  login(request, user)
                  request.session['nom_client'] =  client.nom
                  request.session['prenom_client'] =  client.prenom
                  request.session['statusClient'] =  1
                  messages.success(request, 'Connexion réussie !!!')
                  
                  return redirect('index')

               except:
                  messages.error(request, 'aucun client trouvé, username et/ou mot de passe incorrect')

            else:
               message = 'aucun client trouvé, username et/ou mot de passe incorrect'

      context = {
         'form':form,
         'message':message
      }

      return render(request, 'web/loginClient.html', context)


#----------------Edit-----------------

def editChauffeur(request):
    user = request.user
    chauffeur = Chauffeur.objects.get(user=user)
    form = ChauffeurUpdateForm(instance=chauffeur)
    form2 = ChauffeurProfilForm(instance=user)

    if request.method == "POST":
        form = ChauffeurUpdateForm(request.POST,request.FILES, instance = chauffeur)
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
        form = LivreurUpdateForm(request.POST,request.FILES, instance = livreur)
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