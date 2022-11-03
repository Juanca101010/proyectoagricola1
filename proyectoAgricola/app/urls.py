from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'), 
    path('ingresar/', views.ingresar, name='ingresar'), 
    path('autenticar/', views.autenticar, name='autenticar'),
    path('crearusuario/', views.crearusuario, name='crearusuario'), 
    path('crearusuario2/', views.crearusuario2, name='crearusuario2'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('crearcultivo/', views.crearcultivo, name='crearcultivo'),  
    path('crearcultivo2/', views.crearcultivo2, name='crearcultivo2'),  
    path('datoscultivo/', views.datoscultivo, name='datoscultivo'),  
    path('editar/', views.editar, name='editar'),  
    path('editar2/', views.editar2, name='editar2'),  
    path('vercamaras/', views.vercamaras, name='vercamaras'),  
    path('perfil/', views.perfil, name='perfil'),  
]