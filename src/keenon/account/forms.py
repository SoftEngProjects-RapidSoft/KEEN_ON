from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Customer

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		
		def __init__(self, *args, **kwargs):
			self.fields['username'].widget.attrs.update({'placeholder': 'username'})

class CreateCostumerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['phone']
