from django.db import models
import json

class Address(models.Model):

    street = models.CharField(max_length=50)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class Client(models.Model):
    client_name = models.CharField(verbose_name="Razão social",max_length=50)
    cnpj = models.CharField(max_length=18, primary_key=True)
    email = models.EmailField(max_length=50, unique=True, default="example@example.com")
    phone_number = models.CharField(max_length=10)
    address = models.OneToOneField(
        Address, 
        on_delete=models.CASCADE
    )
    
    
    def __str__(self):
        return self.client_name