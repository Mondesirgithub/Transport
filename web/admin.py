from django.contrib import admin
from .models import Chauffeur, Client, Livreur, Vehicule, TransactionChauffeurClient, TransactionLivreurClient
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
admin.site.register(Vehicule)
admin.site.register(TransactionChauffeurClient)
admin.site.register(TransactionLivreurClient)
