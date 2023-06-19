from django.db import models

# Create your models here.

class Discount (models.Model):
    code_discount = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=6, decimal_places=2)
    expiry_date = models.DateField()
    minimum_purchase = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.code_discount
