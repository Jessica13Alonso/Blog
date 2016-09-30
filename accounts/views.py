from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator #decorador para loggeo
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistrationForm
from .models import Profile
from .forms import UserEditForm
from .forms import ProfileEditForm


# Create your views here.

class Registration(View):
	def get(self,request):
		template = "registration/registration.html"
		form = UserRegistrationForm()
		context = {
			'form':form, 
		}
		return render (request, template, context)

	def post (self, request):
		template = "registration/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False) #commit para que no guarde para que se reestrucuture y envie solo los datos que el admin quiere que se guarden 
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
			return redirect('home')

class Dashboard(View):
	@method_decorator(login_required)
	def get (self, request):
		template = "registration/profile.html"
		userform = UserEditForm(instance=request.user)
		profileform = ProfileEditForm (instance = request.user.profile)
		context = {
			'userform':userform,
			'profileform':profileform,
		}
		return render (request, template, context)


	def post(self, request):
		template = "registration/profile.html"
		userform = UserEditForm(instance=request.user, data=request.POST)
		profileform = ProfileEditForm(instance = request.user.profile, data=request.POST, files=request.FILES)
		if userform.is_valid() and profileform.is_valid():
			userform.save() #el commit=False ya no es necesario porque los datos ya estan guardados, solo se estan modificando. 
			profileform.save()
			return redirect('home')
		else:
			context = {
				'userform':userform, 
				'profileform':profileform,
			}
			return render (request, template, context)
