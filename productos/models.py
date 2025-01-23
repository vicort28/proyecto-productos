from django.db import models

# Modelo para la tabla Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    categoria = models.CharField(max_length=50)  

    def __str__(self):
        return self.nombre 
