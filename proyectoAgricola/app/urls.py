from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'), 
    path('ingresar/', views.ingresar, name='ingresar'), 
    path('crearusuario/', views.crearusuario, name='crearusuario'), 
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('crearcultivo/', views.crearcultivo, name='crearcultivo'),  
    path('datoscultivo/', views.datoscultivo, name='datoscultivo'),  
    path('editar/', views.editar, name='editar'),  
    path('perfil/', views.perfil, name='perfil'),  
]