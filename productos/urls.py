from django.urls import path
from .views import ProductoListCreate, ProductoDetail

# Rutas para el CRUD de productos
urlpatterns = [
    path('productos/', ProductoListCreate.as_view(), name='productos-list-create'),  # Listar y crear productos
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='productos-detail'),  # Obtener, actualizar y eliminar un producto
]
