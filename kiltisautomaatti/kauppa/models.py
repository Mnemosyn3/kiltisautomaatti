from django.db import models

# Create your models here.
class User(models.Model):
    tagNumber = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=5,decimal_places=2,default=0.0)
