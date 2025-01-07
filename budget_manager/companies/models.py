from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    cep = models.CharField(max_length=8)
    street = models.JSONField()
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.name


