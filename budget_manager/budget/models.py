from django.db import models
from company.models import Company

class Vehicle(models.Model):
    brand: str = models.CharField(max_length=20)
    plate_number: str = models.CharField(max_length=20)
    km: float = models.DecimalField(decimal_places=2,max_digits=100000000)

class Service(models.Model):
    SERVICE_TYPES = {
        "Corretivo": "corretivo",
        "Preventivo": "preventivo",
        "Preditivo": "preditivo"
    }

    service_description: str = models.CharField(max_length=100)
    service_type: str = models.CharField(max_length=10, choices=SERVICE_TYPES)
    value: float = models.DecimalField(decimal_places=2,max_digits=100000000)

class ItemSale(models.Model):
    UNITS_OF_MEASUREMENT = {
        "UN": "Unidade",
        "LT": "Litros",
        "KG": "Kilogramas"
    }

    item_name: str = models.CharField(max_length=20)
    unit_of_measurement = models.CharField(max_length=2, choices=UNITS_OF_MEASUREMENT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    value: float = models.DecimalField(decimal_places=2,max_digits=100000000)

    @property
    def quantity_value(self):
        if self.unit_of_measurement == "UN":
            return int(self.quantity)
        return float(self.quantity)
            

class Budget(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    os_number: int = models.IntegerField()
    total: float = models.DecimalField(decimal_places=2,max_digits=100000000)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    item_sale = models.ForeignKey(ItemSale, on_delete=models.CASCADE)