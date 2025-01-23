from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Producto
from .serializers import ProductoSerializer

# Clase para manejar errores personalizados en las vistas
class ManejoErrores:
    """Maneja errores de la API, como 404."""
    def manejar_error(self, exc):
        if isinstance(exc, NotFound):  # Error 404 (no encontrado)
            return Response(
                {"error": "Producto no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        return super().manejar_error(exc)

# Vista para listar y crear productos
class ProductoListCreate(ManejoErrores, generics.ListCreateAPIView):
    queryset = Producto.objects.all()  # Consulta los productos
    serializer_class = ProductoSerializer  # Usa el serializador

    def crear_producto(self, serializer):
        """Guarda un nuevo producto en la base de datos."""
        try:
            serializer.save()
        except Exception as e:
            return Response(
                {"error": "Error al crear producto: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# Vista para obtener, actualizar y eliminar un producto
class ProductoDetail(ManejoErrores, generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()  # Consulta los productos
    serializer_class = ProductoSerializer  # Usa el serializador

    def actualizar_producto(self, serializer):
        """Actualiza un producto existente."""
        try:
            serializer.save()
        except Exception as e:
            return Response(
                {"error": "Error al actualizar producto: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def eliminar_producto(self, instance):
        """Elimina un producto existente."""
        try:
            instance.delete()
        except Exception as e:
            return Response(
                {"error": "Error al eliminar producto: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
