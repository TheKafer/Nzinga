from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Modelos de los usuarios.

#Modelo de la entidad
class Entity(models.Model):
	iduser = models.IntegerField(primary_key=True)
	

#Modelo que contiene la información de la entidad
class Info_Entity(models.Model):
	name = models.CharField(max_length=100,unique=True)
	numberDirectors = models.IntegerField(default=0)
	state = models.BooleanField(default=True)
	idEntity = models.OneToOneField(Entity,null=False, blank=True, on_delete=models.CASCADE)
	#Falta el calendario!

	
#Modelo del director
class Director(models.Model):
	iduser = models.IntegerField(primary_key=True)

#Modelo que contiene la información del director.
class Info_Director(models.Model):
	state = models.BooleanField(default=True)
	email = models.EmailField(max_length=254)
	director = models.OneToOneField(Director,null=False, blank=True, on_delete=models.CASCADE) 


