from django import forms
from django.contrib.auth.forms import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


# class EtdudiantForm(UserCreationForm):
#     nom_etudiant = forms.CharField(max_length=25)
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['nom_etudiant','username', 'password1', 'password2']
    
class ChauffeurForm(UserCreationForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField()
   telephone = forms.CharField()
   adresse = forms.CharField()
   email = forms.EmailField()
   
   class Meta(UserCreationForm.Meta):
      model = User
      fields = ['nom','username', 'password1', 'password2']
     

