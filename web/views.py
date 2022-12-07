from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Chauffeur
from web.forms import ChauffeurForm
# Create your views here.


def register(request):
    form = ChauffeurForm()

    if request.method == 'POST':
        form = ChauffeurForm(request.POST)
            
        if form.is_valid():
            user = form.save()
            Chauffeur.objects.create(
               nom=form.cleaned_data['nom'],
               prenom = form.cleaned_data['prenom'], 
               date_naissance = form.cleaned_data['date_naissance'], 
               telephone = form.cleaned_data['telephone'], 
               adresse = form.cleaned_data['adresse'],
               user=user)

            login(request, user)

    context = {
        'form':form
    }

    return render(request, 'register.html', context)