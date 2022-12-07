from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class ChauffeurForm(UserCreationForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
   telephone = forms.CharField()
   adresse = forms.CharField()
   
   class Meta(UserCreationForm.Meta):
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse','email','password1', 'password2']

