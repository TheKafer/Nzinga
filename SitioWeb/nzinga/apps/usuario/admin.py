from django.contrib import admin
from apps.usuario.models import Entity,Info_Entity,Director,Info_Director

# Register your models here.
admin.site.register(Entity)
admin.site.register(Info_Entity)
admin.site.register(Director)
admin.site.register(Info_Director)
