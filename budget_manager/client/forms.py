from django import forms
from .models import Client, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street','number','neighborhood','city','state')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name','cnpj', 'phone_number')