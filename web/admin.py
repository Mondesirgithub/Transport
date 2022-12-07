from django.contrib import admin
from .models import Chauffeur, Client, Livreur
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


# admin.site.unregister(User)

# class ChauffeurInline(admin.StackedInline):
#     model = Chauffeur
#     fk_name = 'user'

# class ClientInline(admin.StackedInline):
#     model = Client
#     fk_name = 'user'

# class LivreurInline(admin.StackedInline):
#     model = Livreur
#     fk_name = 'user'


# class UserAdmin(UserAdmin):
#     inlines = [ ChauffeurInline, ClientInline, LivreurInline,]


admin.site.register(Chauffeur)
admin.site.register(Livreur)
admin.site.register(Client)
