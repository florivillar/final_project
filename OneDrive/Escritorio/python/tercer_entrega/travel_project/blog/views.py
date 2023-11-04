# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .forms import PostForm, DestinoForm, ComunidadForm
from .models import Post, Destino, Comunidad

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'lista_posts.html', {'posts': posts})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def lista_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'lista_destinos.html', {'destinos': destinos})

def crear_destino(request):
    if request.method == "POST":
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm()
    return render(request, 'crear_destino.html', {'form': form})

def lista_comunidades(request):
    comunidades = Comunidad.objects.all()
    return render(request, 'lista_comunidades.html', {'comunidades': comunidades})

def crear_comunidad(request):
    if request.method == "POST":
        form = ComunidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comunidades')
    else:
        form = ComunidadForm()
    return render(request, 'crear_comunidad.html', {'form': form})
