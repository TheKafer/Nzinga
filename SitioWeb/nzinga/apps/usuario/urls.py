from django.urls import path
from apps.usuario import views

urlpatterns = [
    #path('registroEntidad/',RegistroEntidad.as_view(),name='RegistroEntidad'), ejemplo de una clase vista
    path('registroEntidad/',views.registroEntidad,name='RegistroEntidad'),
    path('base/',views.base, name="base"),
   
]
