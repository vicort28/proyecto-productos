from django.contrib import admin
from django.urls import path, include

# Rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para la administración de Django
    path('api/', include('productos.urls')),  # Rutas del app "productos"
]
