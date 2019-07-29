from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy


from apps.usuario.forms import RegistroUsuario, RegistroEntidad
from apps.usuario.models import Entity,Info_Entity


def index(request):
	return render(request, 'home/index.html')

def homeEntidad(request):
	return render(request,'usuario/homeEntidad.html');


def registroEntidad(request):
	if request.method == 'POST':
		form = RegistroUsuario(request.POST, prefix='form')
		formEntidad = RegistroEntidad(request.POST, prefix = 'formEntidad')
		if form.is_valid() and formEntidad.is_valid():
			usuario = form.save(commit = False)
			usuario.save()
			entity = Entity.objects.create(iduser = usuario.id)
			info_entity = formEntidad.save(commit = False)
			info_entity.idEntity = entity
			info_entity.save()
			return redirect('home')
	else:
		form =RegistroUsuario( prefix='form')
		formEntidad = RegistroEntidad(prefix = 'formEntidad')

	return  render(request,'usuario/formularioEntidad.html', {
		'form': form,
		'formEntidad': formEntidad,
	})	




# Ejemplo de como crearlo con una clase vista
#class RegistroEntidad(CreateView):
#	model = User
#	form_class = RegistroUsuario
#	template_name = 'usuario/formularioEntidad.html'
#	succes_url = redirect('home')
