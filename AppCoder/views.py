from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse


def curso(request):

	cursito = Curso(nombre = 'Python', comision = 34645)
	cursito.save()	# se guarda en la base de datos
	cadena_texto = f'curso guardado: Nombre: {cursito.nombre}, Comision = {cursito.comision}'
	return HttpResponse(cadena_texto)

def cursos(request):
	return HttpResponse('Esto es una vista de cursos')

def estudiantes(request):
	return HttpResponse('Esto es una vista de estudiantes')	

def profesores(request):
	return HttpResponse('Esto es una vista de profesores')	

def entregables(request):
	return HttpResponse('Esto es una vista de entregables')	

def inicio(request):
	return HttpResponse('Estoy en inicio')	
	