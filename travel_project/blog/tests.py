from django.test import TestCase
from blog.models import Articulo
from django.contrib.auth.models import User
from django.utils import timezone

class ArticuloTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        user = User.objects.create(username='test_user')
        Articulo.objects.create(
            titulo='Título de prueba',
            subtitulo='Subtítulo de prueba',
            contenido='Contenido de prueba',
            autor='Autor de prueba',
            creador=user,
            fecha_publicacion=timezone.now()
        )

    def test_str_method(self):
        articulo = Articulo.objects.get(id=1)
        self.assertEqual(str(articulo), 'Título de prueba')
        
    def test_titulo_max_length(self):
        articulo = Articulo.objects.get(id=1)
        max_length = articulo._meta.get_field('titulo').max_length
        self.assertEqual(max_length, 200)
        
    def test_subtitulo_max_length(self):
        articulo = Articulo.objects.get(id=1)
        max_length = articulo._meta.get_field('subtitulo').max_length
        self.assertEqual(max_length, 200)
