from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Articulo(models.Model):

    titulo = models.CharField(max_length=200)
    
    subtitulo = models.CharField(max_length=200)
    
    contenido = models.TextField()
    
    autor = models.CharField(max_length=200)

    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):

        return self.titulo
    

class Destino(models.Model):

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    imagen = models.ImageField(upload_to='destinos/')

    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):

        return self.nombre


class Hospedaje(models.Model):

    nombre = models.CharField(max_length=100)

    destino = models.CharField(max_length=100)

    descripcion = models.TextField()

    imagen = models.ImageField(upload_to='hospedajes/')

    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):

        return self.nombre
    

    #class Meta:

        #verbose_name_plural = "Comunidades"

