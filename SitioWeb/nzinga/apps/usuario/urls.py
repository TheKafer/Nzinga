from django.urls import path
from apps.usuario import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('registroEntidad/',RegistroEntidad.as_view(),name='RegistroEntidad'), ejemplo de una clase vista
    path('registroEntidad/',views.registroEntidad,name='RegistroEntidad'),
    path('homeEntidad/',views.homeEntidad,name='homeEntidad'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
