from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.IntegerField(max_length=6)
    quantity = models.IntegerField(max_length=10)

    def __str__(self):
        return self.description