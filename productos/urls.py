from django.urls import path
from .views import ProductoListCreate, ProductoDetail

urlpatterns = [
    path('productos/', ProductoListCreate.as_view(), name='productos-list-create'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='productos-detail'),
]
