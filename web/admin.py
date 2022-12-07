from django.contrib import admin
from .models import Etudiant, Professeur
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


admin.site.unregister(User)

class EtudiantInline(admin.StackedInline):
    model = Etudiant
    fk_name = 'user'

class ProfesseurInline(admin.StackedInline):
    model = Professeur
    fk_name = 'user'


class UserAdmin(UserAdmin):
    inlines = [ EtudiantInline, ProfesseurInline]


admin.site.register(User, UserAdmin)
