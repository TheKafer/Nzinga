from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Modelos de los usuarios.

#Modelo de la entidad
class Entity(models.Model):
	iduser = models.IntegerField(primary_key=True)


#Modelo que contiene la información de la entidad

class Info_Entity(models.Model):
	name = models.CharField(max_length=100)
	numberDirectors = models.IntegerField(default=0)
	state = models.BooleanField(default=True)
	entity = models.OneToOneField(Entity,null=True, blank=True, on_delete=models.CASCADE) 

#Modelo del director
class Director(models.Model):
	iduser = models.IntegerField(primary_key=True)

#Modelo que contiene la información del director.
class Info_Director(models.Model):
	names = models.CharField(max_length=200)
	LastNames = models.CharField(max_length=200)
	state = models.BooleanField(default=True)
	director = models.OneToOneField(Director,null=True, blank=True, on_delete=models.CASCADE) 



