from rest_framework import serializers
from .models import Producto

# Serializador para el modelo Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'categoria']  # Campos a incluir en la API

    def validate_precio(self, value):
        """Valida que el precio sea un número positivo."""
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser un número positivo.")
        return value
