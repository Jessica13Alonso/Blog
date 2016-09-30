from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse 
# Create your models here.

class Post(models.Model): #clases con dos puntos al finalizar 
	autor = models.ForeignKey(User, related_name = "blog_posts")
	titulo = models.CharField(max_length = 150)
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now = True)
	creado = models.DateTimeField(auto_now = True)
	slug = models.SlugField(max_length = 200, unique_for_date = 'creado')
	image = models.ImageField(upload_to="user", blank=True)

	class Meta: 
		ordering = ('-creado',) #tupla finaliza con , y para lo contrario se le quitar ael guion


	def __str__(self): #funcion que permite trabajar una clase con metodos de una misma clase 
		return self.titulo #retornara el titulo del post 
	def get_absolute_url(self):
		return reverse('post:detail', args = [self.slug]) #Con self enviara su propio slug

class Comentario(models.Model):
	autor = models.ForeignKey(User, related_name="comentarios", blank=True, null= True)
	post = models.ForeignKey(Post, related_name="comentarios", blank=True, null=True)
	fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
	cuerpo = models.TextField(max_length=140, blank=True, null=True)


	def __str__(self):
		return '{} comento en {}'.format(self.autor, self.post)

	class Meta: 
		ordering = ('-fecha',)


