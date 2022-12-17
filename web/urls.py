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
    path('login/', views.loginRequired, name='loginRequired'),
    path('logout/', views.logoutUser, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('getDataChauffeur/<int:pk>', views.getDataChauffeur, name='getDataChauffeur'),
    path('donneesFinancieres/', views.donneesFinancieres, name='donneesFinancieres'),
   path('map/', views.map, name='map'),
   path('map_suivi_users/', views.map_suivi_users, name='map_suivi_users'),
   path('suivi_user_chauffeur/<int:pk>', views.suivi_user_chauffeur, name='suivi_user_chauffeur'),
   path('suivi_user_livreur/<int:pk>', views.suivi_user_livreur, name='suivi_user_livreur'),
]
