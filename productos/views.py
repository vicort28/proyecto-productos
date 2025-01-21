from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Producto
from .serializers import ProductoSerializer

class ManejoErrores:
    """Clase para manejar errores en las vistas."""
    def manejar_error(self, exc):
        # Si el error es 'NotFound', mostramos un mensaje personalizado
        if isinstance(exc, NotFound):
            return Response(
                {"error": "Producto no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        # Si es otro tipo de error, usamos el manejo estándar
        return super().manejar_error(exc)

class ProductoListCreate(ManejoErrores, generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def crear_producto(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            return Response(
                {"error": "Error al crear producto: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class ProductoDetail(ManejoErrores, generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def actualizar_producto(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            return Response(
                {"error": "Error al actualizar producto: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def eliminar_producto(self, instance):
        try: 
            instance.delete()
        except Exception as e:
            return Response(
                {"error": "Error al eliminar producto: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
