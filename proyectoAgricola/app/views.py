from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import administrador, camaras, cultivo, sensorhumedad, sensortemperatura
from django.db.models import Q	
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hola, mundo")


def ingresar(request):
    return render(request, 'app/ingresar.html')


def autenticar(request):
    response_data={}
    # Obtiene los datos del formulario de autenticación
    username = request.POST['username']
    password = request.POST['password']
    # Obtiene el usuario
    usuario = authenticate(username=username, password=password)

    # Verifica si el usuario existe en la base de datos
    
    if usuario is not None:
        print('guoapoooo')
        # Inicia la sesión del usuario en el sistema
        login(request, usuario)
        return redirect('app:dashboard')

    else:
        # Retorna un mensaje de error de login no válido
        return render(request, 'app/ingresar.html') 

def crearusuario(request):
    return render(request, 'app/crearusuario.html')


def crearusuario2(request):
    try:
        
        nombre = request.POST['nombre1']
        user = request.POST['username1']
        email2 = request.POST['email1']
        pass2 = request.POST['pass1']
        rpass2 = request.POST['rpass1']

        u = User()
        u.first_name = nombre
        u.username = user
        u.email = email2
        u.password = rpass2
        u.save()

        return redirect('app:ingresar')
    except Exception as e:
        print(e)
        return render(request,'app/ingresar.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')


def dashboard2(request):
    lista22 = cultivo.objects.all()
    print(lista22)
    contexto ={
        'listadecultivos':lista22,
    }
    return render(request, 'app/dashboard.html',contexto)

def crearcultivo(request):
    return render(request, 'app/crearcultivo.html')

def crearcultivo2(request):
    try:
        
        nombre = request.POST['nombre1']
        fecha1 = request.POST['fecha']
        localidad1 = request.POST['localidad']
        st = request.POST['sensort']
        sh = request.POST['sensorh']

        c = cultivo()
        c.nombre = nombre
        c.fecha = fecha1
        c.localidad = localidad1
        c.sensortemperatura = st
        c.sensorhumedad = sh
        c.save()

        return redirect('app:dashboard')
    except Exception as e:
        print(e)
        return render(request,'app/dashboard.html')

def datoscultivo(request):
    return render(request, 'app/datoscultivo.html')

def editar(request):
    return render(request, 'app/editar.html')

def perfil(request):
    return render(request, 'app/perfil.html')