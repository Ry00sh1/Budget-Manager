from django.db import models
from company.models import Company

class Vehicle(models.Model):
    brand: str = models.CharField(max_length=20)
    plate_number: str = models.CharField(max_length=20)
    km: float = models.DecimalField()

class Service(models.Model):
    service_name: str = models.CharField(max_length=20)
    value: float = models.DecimalField()

class Sale(models.Model):
    UNITS_OF_MEASUREMENT = {
        "UN": "Unidade",
        "LT": "Litros",
        "KG": "Kilogramas"
    }

    item_name: str = models.CharField(max_length=20)
    unit_of_measurement = models.CharField(max_length=2, choices=UNITS_OF_MEASUREMENT)
    quantity = 0
    
    def define_quantity(self):
        if self().unit_of_measurement == "UN":
            quantity: int = models.IntegerField()
        else:
            quantity: float = models.DecimalField()
            

class Budget(models.Model):
    employer = models.ManyToOneField(Company, required=True)
    employee = models.ManyToOneField(Company, required=True)
    os_number: int = models.IntegerField()
    total: float = models.DecimalField()