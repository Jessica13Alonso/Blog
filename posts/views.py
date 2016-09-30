from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User #Importa los usuarios manualmente
from django. utils.text import slugify
from .models import Post
from .forms import PostForm, ComentarioForm
# Create .your views here.

class PostList(View):
	def get(self,request):
		template = "posts/list_view.html"
		user= User.objects.get(username = "jessica")
		posts = user.blog_posts.all() 
		context = {
			'posts':posts
		}
		return render (request, template, context)

class DetailView(View): #el nombre se obtiene del archivo urls.py
	def get(self,request,slug):
		template = "posts/detail.html"
		post = Post.objects.get(slug=slug) #Obtendra el slug del modelo
		comentarios = post.comentarios.all()
		form = ComentarioForm()
		context= { #diccionario con llaves 
			'post': post,
			'comentarios': comentarios,
			'form': form,
		}
		return render (request, template, context) #tuplas con parentesís

	def post(self,request,slug):
		form = ComentarioForm(request.POST)
		post  = Post.objects.get(slug=slug)
		form = form.save (commit=False)
		form.autor = request.user
		form.post = post
		form.save()
		return redirect('post:detail', slug=slug)

class NuevoPost(View):
	def get(self,request):
		form = PostForm()
		template_name="posts/new.html"
		context = {
			'form':form
		}
		return render(request, template_name, context)


	def post(sefl,request):
		form = PostForm(request.POST)
		post = form.save(commit=False) #commit para que no guarde para que se reestrucuture y envie solo los datos que el admin quiere que se guarden 
		post.slug = slugify(post.titulo)
		post.autor = request.user
		post.save()
		return redirect('post:post_list')


