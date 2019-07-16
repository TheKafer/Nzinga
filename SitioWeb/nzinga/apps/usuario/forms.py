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
				'password1',
				
				

			]
		labels = {
				'username':'Nombre de Usuario',
				'first_name':'Nombre',
				'last_name': 'Apellidos',
				'email':'Correo',
				'password1':'Contraseña',
				
				

		}
		widgets = {
				'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario'}),
				'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
				'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}),
				'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'example@gmail.com'}),
				'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Usuario'}),
				
				
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
				'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ejm Universidad de las lagartijas'}),
		}
