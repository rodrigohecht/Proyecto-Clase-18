from django.db import models

class Curso(models.Model):	# el Curso es un modelo de django (hereda)
	nombre = models.CharField(max_length=50)	# los datos tienen hasta 50 caracteres
	comision = models.IntegerField()	# la comisiones es un tipo de entero de base de datos

class Estudiante(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.EmailField()

class Profesor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.EmailField()
	profesion = models.CharField(max_length=50)

class Entregable(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_entrega = models.DateField()
	entregado = models.BooleanField()
	