from django.contrib import admin
from viajes.models import *
from users.models import *

# Register your models here.

@admin.register(Ciudad)
class AdminCiudad(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia_id')

@admin.register(Provincia)
class AdminProvincia(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Conductor)
class AdminConductor(admin.ModelAdmin):
    list_display = ('user_id', 'licencia')

@admin.register(Viaje)
class AdminViaje(admin.ModelAdmin):
    list_display = ('conductor_id', 'ciudad_origen_id','ciudad_destino_id', 'descripcion', 'capacidad',)

@admin.register(UsuarioPeticion)
class AdminUsuarioPeticion(admin.ModelAdmin):
    list_display = ('viaje', 'user', 'esta_aceptado')