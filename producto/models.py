from django.db import models

# Create your models here.

class ProductoCategoria(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.nombre