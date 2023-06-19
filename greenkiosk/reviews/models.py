from django.db import models

# Create your models here.

class Reviews (models.Model):
    user_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    ratings = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
