from django.db import models

class Budget(models.Model):
    os_number = models.IntegerField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.os_number