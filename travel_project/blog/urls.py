from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('home/', views.home, name='home'),
    path('articulos/', views.lista_articulos, name='lista_articulos'),
    path('articulo/', views.crear_articulo, name='crear_articulo'),
    path('destinos/', views.lista_destinos, name='lista_destinos'),
    path('destino/', views.crear_destino, name='crear_destino'),
    path('hospedajes/', views.lista_hospedajes, name='lista_hospedajes'),
    path('hospedaje/', views.crear_hospedaje, name='crear_hospedaje'),
    path('editar-articulo/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('eliminar-articulo/<int:id>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('editar-destino/<int:pk>/', views.editar_destino, name='editar_destino'),
    path('eliminar-destino/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
    path('editar-hospedaje/<int:pk>/', views.editar_hospedaje, name='editar_hospedaje'),
    path('eliminar-hospedaje/<int:id>/', views.eliminar_hospedaje, name='eliminar_hospedaje'),
    path('articulo/<int:pk>/', views.articulo_detail, name='articulo_detail'),
    path('destino/<int:pk>/', views.destino_detail, name='destino_detail'),
    path('hospedaje/<int:pk>/', views.hospedaje_detail, name='hospedaje_detail'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('contacto/', views.contacto, name='contacto'),
]

