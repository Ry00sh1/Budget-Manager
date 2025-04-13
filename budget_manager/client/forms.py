from django import forms
from .models import IndividualClient,CorporateClient, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street','number','neighborhood','city','state')


class IndividualClientForm(forms.ModelForm):
    class Meta:
        model = IndividualClient
        fields = ('name', 'phone_number','email','cpf')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de Telefone'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'})
        }

class CorporateClientForm(forms.ModelForm):
    class Meta:
        model = CorporateClient
        fields = ('name', 'phone_number','email','cnpj')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de Telefone'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'CNPJ'})
        }