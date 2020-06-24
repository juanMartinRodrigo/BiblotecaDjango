from django.contrib import admin
from proyecto.models import *

class LibroInline(admin.TabularInline):
    model = Libro

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Grupo de Datos', {'fields': ('nombre', 'apellido')}),
        ('Grupo de Contactos', {'fields': ('direccion', 'telefono',)}),
        ('Detalle de alquileres', {'fields': ('ejemplar',)}),
    )
class AutorAdmin(admin.ModelAdmin):
    inlines = [LibroInline ,]
    search_fields = ['nombre','apellido']

class LibroAdmin(admin.ModelAdmin):
	exclude = ('paginas','autor')
    #Para que funcione hay que deshabilitar el django-jet
    #filter_horizontal = ('Ejemplar',)
    

# Register your models here.
admin.site.register(Autor,AutorAdmin);
admin.site.register(Libro, LibroAdmin);
admin.site.register(Usuario, UsuarioAdmin);
admin.site.register(Ejemplar,);
