from django.contrib import admin
from proyecto.models import *

class UsuarioAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre','apellido', 'direccion', 'telefono')
        }),
        ('Detalle de alquileres', {
            'fields': ('ejemplar',)
        }),
    )

    list_display = ['nombre', 'telefono', 'direccion']

# Register your models here.
admin.site.register(Autor,);
admin.site.register(Libro,);
admin.site.register(Usuario, UsuarioAdmin);
admin.site.register(Ejemplar,);
