from django import forms
from .models import Customer,Address,Product
from django.contrib.auth.models import User



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