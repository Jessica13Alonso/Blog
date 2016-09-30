from django import forms
from .models import Profile
from django.contrib.auth.models import User

class  UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repite Tu Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email') # son los campos necesarios que llenaria el Usuario

	def clean_password2(self):
		cl = self.cleaned_data
		if cl['password'] != cl['password2']:
			raise forms.ValidationError('Las Contraseñas No Coinciden')
		return cl ['password2']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('age', 'sex', 'photo')