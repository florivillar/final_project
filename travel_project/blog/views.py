# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse

from django.db.models import Q

from .forms import ArticuloForm, DestinoForm, HospedajeForm, SearchForm
from .models import Articulo, Destino, Hospedaje

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView

import logging

def search_results(request):

    form = SearchForm(request.GET or None)

    results = {}

    query = None

    if form.is_valid():

        query = form.cleaned_data.get('query')


        if query:
            articulo_results = Articulo.objects.filter(

                Q(titulo__icontains=query) | Q(contenido__icontains=query))

            destino_results = Destino.objects.filter(

                Q(nombre__icontains=query))

            hospedaje_results = Hospedaje.objects.filter(

                Q(nombre__icontains=query))


            results = {

                'articulos': articulo_results,

                'destinos': destino_results,

                'hospedajes': hospedaje_results,

            }


    return render(request, 'blog/search_results.html', {'form': form, 'results': results, 'query': query})


#def home(request):

    #return render(request, 'home.html')


def home(request, exception=None):
    if exception is not None:
        # Registro del error 404
        logging.error(f"Error 404 - URL: {request.path}")

    return render(request, 'home.html')



def lista_articulos(request):
    articulos = Articulo.objects.all()

    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})


@login_required

def crear_articulo(request):

    if request.method == "POST":

        form = ArticuloForm(request.POST, request.FILES)

        if form.is_valid():

            articulo = form.save(commit=False)
            articulo.creador = request.user

            articulo.save()
            return redirect('lista_articulos')

    else:

        form = ArticuloForm()

    return render(request, 'blog/crear_articulo.html', {'form': form})


def lista_destinos(request):

    destinos = Destino.objects.all()

    return render(request, 'blog/lista_destinos.html', {'destinos': destinos})


@login_required

def crear_destino(request):

    if request.method == "POST":

        form = DestinoForm(request.POST, request.FILES)

        if form.is_valid():

            destino = form.save(commit=False)
            destino.creador = request.user

            destino.save()
            return redirect('lista_destinos')

    else:

        form = DestinoForm()

    return render(request, 'blog/crear_destino.html', {'form': form})


def lista_hospedajes(request):

    hospedajes = Hospedaje.objects.all()

    return render(request, 'blog/lista_hospedajes.html', {'hospedajes': hospedajes})


@login_required

def crear_hospedaje(request):

    if request.method == "POST":

        form = HospedajeForm(request.POST, request.FILES)

        if form.is_valid():

            hospedaje = form.save(commit=False)

            hospedaje.creador = request.user

            hospedaje.save()

            return redirect('lista_hospedajes')

    else:

        form = HospedajeForm()

    return render(request, 'blog/crear_hospedaje.html', {'form': form})



def editar_articulo(request, pk):
    post = Articulo.objects.get(id=pk)

    if request.method == "POST":

        formulario = ArticuloForm(request.POST, request.FILES, instance=post)


        if formulario.is_valid():

            formulario.save()

            url_exitosa = reverse('lista_articulos')

            return redirect(url_exitosa)

        else:

            formulario = ArticulosForm(instance=post)

    else:

        formulario = ArticuloForm(instance=post)
    return render(
        request=request,

        template_name='blog/editar_articulo.html',

        context={'formulario': formulario},
    )

    

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)

    if request.method == "POST":
        articulo.delete()

        url_exitosa = reverse('lista_articulos')

        return redirect(url_exitosa)
    


def editar_destino(request, pk):

    destino = Destino.objects.get(id=pk)

    if request.method == "POST":

        formulario = DestinoForm(request.POST, request.FILES, instance=destino)


        if formulario.is_valid():

            formulario.save()

            url_exitosa = reverse('lista_destinos')

            return redirect(url_exitosa)

        else:

            formulario = DestinoForm(instance=destino)

    else:

        formulario = DestinoForm(instance=destino)
    return render(
        request=request,

        template_name='blog/editar_destino.html',

        context={'formulario': formulario},
    )


def eliminar_destino(request, id):

    destino = Destino.objects.get(id=id)

    if request.method == "POST":
        destino.delete()

        url_exitosa = reverse('lista_destinos')

        return redirect(url_exitosa)
    
    

def editar_hospedaje(request, pk):

    hospedaje = Hospedaje.objects.get(id=pk)

    if request.method == "POST":

        formulario = HospedajeForm(request.POST, request.FILES, instance=hospedaje)


        if formulario.is_valid():

            formulario.save()

            url_exitosa = reverse('lista_hospedajes')

            return redirect(url_exitosa)

        else:

            formulario = HospedajeForm(instance=hospedaje)

    else:

        formulario = HospedajeForm(instance=hospedaje)
    return render(
        request=request,

        template_name='blog/editar_hospedaje.html',

        context={'formulario': formulario},
    )
    

def eliminar_hospedaje(request, id):

    hospedaje = Hospedaje.objects.get(id=id)

    if request.method == "POST":

        hospedaje.delete()

        url_exitosa = reverse('lista_hospedajes')

        return redirect(url_exitosa)
    


def articulo_detail(request, pk):

    articulo = get_object_or_404(Articulo, pk=pk)

    return render(request, 'blog/articulo_detail.html', {'articulo': articulo})


def destino_detail(request, pk):

    destino = get_object_or_404(Destino, pk=pk)

    return render(request, 'blog/destino_detail.html', {'destino': destino})


def hospedaje_detail(request, pk):

    hospedaje = get_object_or_404(Hospedaje, pk=pk)

    return render(request, 'blog/hospedaje_detail.html', {'hospedaje': hospedaje})


def about(request):

    return render(request, 'about.html')


def pages(request):
    articulos = Articulo.objects.all()
    destinos = Destino.objects.all()
    hospedajes = Hospedaje.objects.all()

    return render(request, 'blog/pages.html', {'articulos': articulos, 'destinos': destinos, 'hospedajes': hospedajes})

def contacto(request):

    return render(request, 'contacto.html')