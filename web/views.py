from django.shortcuts import render
from django.contrib.auth.models import User
from web.forms import EtdudiantForm
from django.contrib.auth import login
from .models import Etudiant
# Create your views here.


def register(request):
    form = EtdudiantForm()

    if request.method == 'POST':
        form = EtdudiantForm(request.POST)
            
        if form.is_valid():
            user = form.save()
            Etudiant.objects.create(nom_etudiant=form.cleaned_data['nom_etudiant'], user=user)
            login(request, user)

    context = {
        'form':form
    }

    return render(request, 'register.html', context)