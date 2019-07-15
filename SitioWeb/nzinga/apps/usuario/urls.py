from django.urls import path
from . import views

urlpatterns = [
    path('registroEntidad/',views.registroEntidad,name='registroEntidad'),

]
