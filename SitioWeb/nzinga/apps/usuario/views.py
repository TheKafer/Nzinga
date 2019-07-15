from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm



from django.http import HttpResponse
from apps.usuario.forms import RegistroUsuario
from django.contrib.auth.models import User
from apps.usuario.models import Entity,Info_Entity

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def registroEntidad(request):
	if request.method == 'POST':
		form =RegistroUsuario(request.POST)
		if form.is_valid():
			#usuario = request.user
			#entity = Entity.objects.create(iduser = usuario.id)
			usuario = form.save(commit = False)
			usuario.save()
			entity = Entity.objects.create(iduser = usuario.id)
			#form.save()
			return redirect('home')
	else:
		form =RegistroUsuario()

	return  render(request,'usuario/formularioEntidad.html', {
		'form': form
	})
