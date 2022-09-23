from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'), 
    path('ingresar/', views.ingresar, name='ingresar'), 
    path('crearusuario/', views.crearusuario, name='crearusuario'), 
]