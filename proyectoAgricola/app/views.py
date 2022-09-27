from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q	
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hola, mundo")


def ingresar(request):
    return render(request, 'app/ingresar.html')

def crearusuario(request):
    return render(request, 'app/crearusuario.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')

def crearcultivo(request):
    return render(request, 'app/crearcultivo.html')

def datoscultivo(request):
    return render(request, 'app/datoscultivo.html')