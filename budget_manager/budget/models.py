from django.db import models
from company.models import

class Budget(models.Model):
    os_number = models.IntegerField()
    employer = 