from django import forms
from .models import Company, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street','number','neighborhood','city','state')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name','cnpj', 'phone_number')