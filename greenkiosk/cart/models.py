from django.db import models

class Cart(models.Model):
    id_number = models.PositiveIntegerField()
    products = models.CharField(max_length=90)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.id

# Create your models here.
