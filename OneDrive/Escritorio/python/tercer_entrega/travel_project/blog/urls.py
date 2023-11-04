from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.lista_posts, name='lista_posts'),
    path('post/', views.crear_post, name='crear_post'),
    path('destinos/', views.lista_destinos, name='lista_destinos'),
    path('destino/', views.crear_destino, name='crear_destino'),
    path('comunidades/', views.lista_comunidades, name='lista_comunidades'),
    path('comunidad/', views.crear_comunidad, name='crear_comunidad'),
]
