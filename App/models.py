from django.db import models

# Create your models here.

from django.db import models

class register(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)