from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def home(request):
	queryset=request.GET.get("buscar")
	if queryset:
		post= Post.objects.filter(
				Q(titulo__icontains=queryset) | 
				Q(descripcion__icontains=queryset),
				estado=True
			).distinct()
	else:
		post= Post.objects.filter(estado=True)

	paginator = Paginator(post, 2)
	page=request.GET.get('page')
	post=paginator.get_page(page)
	return render(request,'index.html', {'posts':post} )

def detallePost(request,slug):
	try:
		post= Post.objects.get(
			slug=slug
			)
		print(request, 'post.html')
		return render(request, 'post.html', {'post':post})
	except Post.DoesNotExist:
		raise Http404

def generales(request):
	queryset= request.GET.get("buscar")
	if queryset:
		post=Post.objects.filter(
			Q(titulo__icontains=queryset) |
			Q(descripcion__icontains=queryset),
			categoria=Categoria.objects.get(nombre__iexact="Generales"),
			estado=True
			).distinct()
	else:
		post= Post.objects.filter(
			estado=True, 
			categoria= Categoria.objects.get(nombre__iexact = 'Generales')
		)
	paginator = Paginator(post, 2)
	page=request.GET.get('page')
	post=paginator.get_page(page)
	return render(request,'generales.html', {'posts':post})

def programacion(request):
	queryset=request.GET.get("buscar")
	if queryset:
		post=Post.objects.filter(
			Q(titulo__icontains=queryset) |
			Q(descripcion__icontains=queryset),
			categoria=Categoria.objects.get(nombre__iexact="programacion"),
			estado=True
			).distinct()
	else:
		post= Post.objects.filter(
			estado=True, 
			categoria= Categoria.objects.get(nombre__iexact = 'programacion')
		)
	paginator = Paginator(post, 2)
	page=request.GET.get('page')
	post=paginator.get_page(page)
	return render(request,'programacion.html', {'posts':post})


def tutoriales(request):
	queryset=request.GET.get("buscar")
	if queryset:
		post=Post.objects.filter(
			Q(titulo__icontains=queryset) |
			Q(descripcion__icontains=queryset),
			categoria=Categoria.objects.get(nombre__iexact="tutoriales"),
			estado=True
			)
	else:
		post= Post.objects.filter(
			estado=True, 
			categoria= Categoria.objects.get(nombre__iexact = 'tutoriales')
		)
	paginator = Paginator(post, 2)
	page=request.GET.get('page')
	post=paginator.get_page(page)
	return render(request,'tutoriales.html', {'posts':post})


def tecnologia(request):
	queryset=request.GET.get("buscar")
	if queryset:
		post=Post.objects.filter(
			Q(titulo__icontains=queryset) |
			Q(descripcion__icontains=queryset),
			categoria=Categoria.objects.get(nombre__iexact="tecnologia"),
			estado=True
			)
	else: 
		post= Post.objects.filter(
			estado=True, 
			categoria= Categoria.objects.get(nombre__iexact = 'Tecnologia')
		)
	paginator = Paginator(post, 2)
	page=request.GET.get('page')
	post=paginator.get_page(page)
	return render(request,'tecnologia.html', {'posts':post})


def videojuegos(request):
	queryset=request.GET.get("buscar")
	if queryset:
		post=Post.objects.filter(
			Q(titulo__icontains=queryset) |
			Q(descripcion__icontains=queryset),
			categoria=Categoria.objects.get(nombre__iexact="Videojuegos"),
			estado=True
			)
	else:
		post= Post.objects.filter(
			estado=True, 
			categoria= Categoria.objects.get(nombre__iexact = 'videojuegos')
		)
	paginator = Paginator(post, 2)
	page=request.GET.get('page')
	post=paginator.get_page(page)
	return render(request,'videojuegos.html', {'posts':post})

