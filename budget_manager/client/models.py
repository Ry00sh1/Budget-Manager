from django.db import models

class Address(models.Model):
    street = models.CharField(verbose_name='Rua',max_length=50)
    number = models.IntegerField(verbose_name='Número')
    neighborhood = models.CharField(verbose_name='Bairro',max_length=50)
    city = models.CharField(verbose_name='Cidade',max_length=50)
    state = models.CharField(verbose_name='UF',max_length=2)

class Client(models.Model):
    name = models.CharField(verbose_name="Nome",max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(verbose_name="Número de Telefone",max_length=10)
    address = models.OneToOneField(
        Address, 
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name

class IndividualClient(Client):
    cpf = models.CharField(verbose_name='CPF',max_length=14, unique=True)

    class Meta:
        verbose_name = 'Cliente Físico'
        verbose_name_plural = 'Clientes Físicos'

class CorporateClient(Client):
    cnpj = models.CharField(verbose_name='CNPJ',max_length=18, unique=True)

    class Meta:
        verbose_name = 'Cliente Jurídico'
        verbose_name_plural = 'Clientes Jurídicos'