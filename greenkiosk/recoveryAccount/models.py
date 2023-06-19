from django.db import models

# Create your models here.

class RecoveryAccount(models.Model):
    user_id = models.PositiveIntegerField()
    email = models.EmailField()
