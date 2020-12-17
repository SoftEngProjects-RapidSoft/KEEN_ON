from django import forms
from .models import Customer,Address



class CustomerUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Customer
        fields = ['userName','email','firstName','lastName', 'phone']
class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country','city','town','aveSt','apartmentNo','zipCode']