from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='destinos/')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    miembros = models.ManyToManyField(User, related_name='miembros_comunidad')

    def __str__(self):
        return self.nombre

