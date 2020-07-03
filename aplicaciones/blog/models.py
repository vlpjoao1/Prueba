from django.db import models
from ckeditor.fields import RichTextField
class Categoria(models.Model):
	id=models.AutoField(primary_key=True)
	nombre= models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
	estado=models.BooleanField('Activado/Desactivado', default=True)
	#auto_now: Que se actualize cuando hagas algun cambio al registro
	#auto_now_field: Que se agregue automaticamente cuando crees un registro
	fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural='Categorías'

	def __str__(self):
		#muestra como será renderizada cada registro de la tabla, y en este caso, se mostrará por su nombre
		return self.nombre

class Autor(models.Model):
	id = models.AutoField(primary_key=True)
	nombres= models.CharField('Nombres de Autor', max_length=255, blank=False, null=False)
	apellidos= models.CharField('Apellidos del Autor', max_length=255, blank=False, null=False)
	facebook= models.URLField('Facebook', blank=True, null=True)
	twitter= models.URLField('Twitter', blank=True, null=True)
	instagram= models.URLField('Instagram', blank=True, null=True)
	web= models.URLField('Web', blank=True, null=True)
	email=models.EmailField('Correo electronico', blank=False, null=False)
	estado=models.BooleanField('Estado', default=True)
	fecha_creacion=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

	class Meta:
		verbose_name='Autor'
		verbose_name_plural='Autores'

	def __str__(self):
		return "{0},{1}".format(self.apellidos,self.nombres)

class Post(models.Model):
	id=models.AutoField(primary_key=True)
	titulo=models.CharField('titulo',max_length=90, blank=False, null=False)
	slug=models.CharField('Slug', max_length=100, blank=False, null=False)
	descripcion=models.CharField('Descripcion', max_length=100, blank=False,null=False)
	contenido= RichTextField()
	imagen=models.URLField('Imagen')
	autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
	categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
	estado= models.BooleanField('Activo/Desactivado', default=True)
	fecha_creacion= models.DateField('Fecha de creacion', auto_now_add=True, auto_now=False)

	class Meta:
		verbose_name='Post'
		verbose_name_plural='Posts'

	def __str__(self):
		return self.titulo