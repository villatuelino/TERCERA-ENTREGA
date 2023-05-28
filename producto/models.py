from django.db import models

# Create your models here.
class producto(models.Model):
    producto = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)


    def __str__(self):
        return self.producto
    