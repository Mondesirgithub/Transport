from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


      

class ChauffeurRegisterForm(UserCreationForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
   telephone = forms.CharField()
   adresse = forms.CharField()
   piece_jointe = forms.FileField()
   
   class Meta(UserCreationForm.Meta):
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse','email','password1', 'password2','piece_jointe']


class LivreurRegisterForm(UserCreationForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
   telephone = forms.CharField()
   adresse = forms.CharField()
   piece_jointe = forms.FileField()
   
   class Meta(UserCreationForm.Meta):
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse','email','password1', 'password2','piece_jointe']

class ClientRegisterForm(UserCreationForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
   telephone = forms.CharField()
   adresse = forms.CharField()
   
   class Meta(UserCreationForm.Meta):
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse','email','password1', 'password2']


# --------LOGIN-------

class LoginForm(forms.Form):
    username = forms.CharField(label="Email")
    password = forms.CharField(label="Mot de passe")

# -----------Update----------
class ChauffeurUpdateForm(forms.ModelForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput())
   telephone = forms.CharField()
   adresse = forms.CharField()
   piece_jointe = forms.FileField()

   class Meta:
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse','piece_jointe']


class ChauffeurProfilForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['email']


class LivreurUpdateForm(forms.ModelForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput())
   telephone = forms.CharField()
   adresse = forms.CharField()
   piece_jointe = forms.FileField()

   class Meta:
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse','piece_jointe']

class LivreurProfilForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['email']


class ClientUpdateForm(forms.ModelForm):
   nom = forms.CharField()
   prenom = forms.CharField()
   date_naissance = forms.DateField(widget=forms.DateInput())
   telephone = forms.CharField()
   adresse = forms.CharField()

   class Meta:
      model = User
      fields = ['nom','prenom', 'date_naissance', 'telephone', 'adresse']

class ClientProfilForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['email']