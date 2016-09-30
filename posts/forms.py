from django import forms
from .models import Post, Comentario
#formulario  
class PostForm (forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo', 'contenido']


class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['cuerpo',] #Los campos en una lista 
		label = {
			'cuerpo':'Escribe un comentario' #escribe una descripcion
		}