from django.db import models

# Create your models here.

class Notifications(models.Model):
    user_id = models.PositiveIntegerField()
    message = models.CharField(max_length=300)
    time_stamp = models.DateTimeField()