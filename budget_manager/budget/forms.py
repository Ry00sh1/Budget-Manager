from django import forms
from .models import Budget, ItemSale, Service

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['company', 'os_number']

class ItemSaleForm(forms.ModelForm):
    class Meta:
        model = ItemSale
        fields = ['item_name','unit_of_measurement', 'quantity','value']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_description','service_type','value']