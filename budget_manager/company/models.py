from django.db import models
import json

def load_states_json():
    with open('br_states_cities.json', 'r') as file:
        f = file.read()
        data = json.loads(f)

    estados = []
    content = data['estados']
    for estado in content:
        estados.append(estado['nome'])

    return(estados)

class Address(models.Model):
    ESTADOS = load_states_json()

    street = models.CharField(max_length=50)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class Company(models.Model):
    company_name = models.CharField(verbose_name="Razão social",max_length=50)
    cnpj = models.CharField(max_length=18, primary_key=True)
    phone_number = models.CharField(max_length=10)
    address = models.OneToOneField(
        Address, 
        on_delete=models.CASCADE
    )
    
    
    def __str__(self):
        return self.company_name