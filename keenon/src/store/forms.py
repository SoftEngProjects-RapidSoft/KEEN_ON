from django import forms
from .models import Customer,Address,Product



class CustomerUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Customer
        fields = ['userName','email','firstName','lastName', 'phone']
class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country','city','town','aveSt','apartmentNo','zipCode']
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','quantity','description']