from django import forms
from .models import Cliente
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = (
			'username',
			'password',
			'first_name',
			'last_name',
			'email',
		)
		
class ClienteLog(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = (
			'username',
			'password',
		)		
