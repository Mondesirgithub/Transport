from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('edit-chauffeur/', views.editChauffeur, name='editChauffeur'),
    path('edit-livreur/', views.editLivreur, name='editLivreur'),
    path('edit-client/', views.editClient, name='editClient'),
    path('register-chauffeur/', views.registerChauffeur, name='registerChauffeur'),
    path('register-livreur/', views.registerLivreur, name='registerLivreur'),
    path('register-client/', views.registerClient, name='registerClient'),
    path('login-chauffeur/', views.loginChauffeur, name='loginChauffeur'),
    path('login-livreur/', views.loginLivreur, name='loginLivreur'),
    path('login-client/', views.loginClient, name='loginClient'),
    path('logout/', views.logoutUser, name='logout'),
    path('contact/', views.contact, name='contact'),
]
