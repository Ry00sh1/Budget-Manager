from django import forms
from .models import IndividualClient,CorporateClient, Address
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street','number','neighborhood','city','state')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'row g-3'
        


class IndividualClientForm(forms.ModelForm):
    class Meta:
        model = IndividualClient
        fields = ('name', 'phone_number', 'email', 'cpf')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de Telefone'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'row g-3'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('phone_number', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='col-md-6'),
                Column('cpf', css_class='col-md-6'),
                css_class='row'
            )
        )

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'row g-3'
        self.helper.label_class = 'col-2 col-form-label'
        self.helper.field_class = 'col-10'