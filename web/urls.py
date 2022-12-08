from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register-chauffeur/', views.registerChauffeur, name='registerChauffeur'),
    path('register-livreur/', views.registerLivreur, name='registerLivreur'),
    path('register-client/', views.registerClient, name='registerClient'),
    path('contact/', views.contact, name='contact'),
]
