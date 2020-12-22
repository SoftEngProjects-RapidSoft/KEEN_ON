from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Customer
from store.models import Product, Address

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
class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'image']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model= User
        fields = ['username','first_name', 'last_name', 'email', ]
class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country','city','town','aveSt','apartmentNo','zipCode']
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','quantity','description','image']