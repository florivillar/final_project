from django import forms

from .models import Articulo, Destino, Hospedaje


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo

        fields = ['titulo', 'subtitulo', 'contenido', 'autor']


class DestinoForm(forms.ModelForm):

    class Meta:

        model = Destino

        fields = ['nombre', 'descripcion', 'imagen']


class HospedajeForm(forms.ModelForm):

    class Meta:

        model = Hospedaje

        fields = ['nombre', 'destino', 'descripcion', 'imagen']


class SearchForm(forms.Form):

    query = forms.CharField(max_length=100, required=False, label='')

