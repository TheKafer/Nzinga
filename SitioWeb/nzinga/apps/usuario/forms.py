from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.usuario.models import Entity,Info_Entity

class RegistroUsuario(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',

			]
		labels = {
				'username':'Nombre de Usuario',
				'first_name':'Nombre',
				'last_name': 'Apellidos',
				'email':'Correo',


		}

class RegistroEntidad(forms.ModelForm):

	class Meta:
		model = Info_Entity

		fields = [
				'name',
			]
		labels = {
				'name':'Nombre de la entidad',
		}
		widgets = {
				'name': forms.TextInput(attrs={'class':'form-control'}),
		}
