from django.contrib import admin
from .models import *
#para que aparezca el importar y exportar en el sitio administrador
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
	class Meta:
		#modelo al que vas a mostrar
		model= Categoria
class AutorResource(resources.ModelResource):
	class Meta:
		#modelo al que vas a mostrar
		model= Autor

class PostResource(resources.ModelResource):
	class Meta:
		model=Post


#ModeloAdmin(admin.ModelAdmin) 
#debes agregar el importexportmodeladmin para que puedas importar
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	#parametro por el que va a buscar la barra de busqueda
	search_fields=['nombre']
	#atributos que se quieren mostrar en el sitio de administracion
	list_display=('nombre','estado',)

	#debs agregarlo aquí para que se muestre en el sitio
	resource_class=CategoriaResource

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields=['nombres','apellidos','estado']
	list_display=('nombres','estado','apellidos',)

	resource_class=AutorResource

class CategoriaPost(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields=['titulo']
	list_display=('titulo','estado','slug',)

	resource_class=PostResource

#register(Modelo, barra de busqueda)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, CategoriaPost)

# Register your models here.
#user: joao clave: 15101220
