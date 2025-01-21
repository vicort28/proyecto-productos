# Proyecto de Gestión de Productos

Este proyecto es una API REST desarrollada con Django y Django REST Framework. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar productos con los siguientes campos: nombre, descripción, precio y categoría.

---

## Características
- Crear un producto.
- Listar todos los productos.
- Obtener detalles de un producto por su ID.
- Actualizar un producto.
- Eliminar un producto.

---

## Tecnologías utilizadas
- **Lenguaje:** Python 3.9+
- **Framework:** Django 4.2, Django REST Framework 3.14
- **Base de datos:** SQLite (por defecto)


---

## Requisitos previos
Asegúrate de tener instalado:
- Python 3.9 o superior
- Git

---

## Configuración del proyecto

### 1.1 Clonar el repositorio
Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/proyecto-productos.git
cd proyecto-productos
```
---

## 2. Configuración Del entorno virtual
Un entorno virtual ayuda a aislar las dependencias del proyecto. Sigue los pasos a continuación:
### 2.1 Crear y activar el entorno virtual:

En Windows
```bash
python -m venv venv
venv\Scripts\activate
```
En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.2 Instalar las dependencias
```bash
pip install -r requirements.txt
```
En caso de agregar nuevas dependencias
```bash
pip freeze > requirements.txt
```

---

## 3. Configuración De Base de Datos y ejecucion del servidor local

### 3.1 Ejecutar migraciones
Aplica las migraciones de base de datos para configurar la base de datos:
```bash
python manage.py migrate
```

### 3.2 Iniciar el servidor
```bash
py manage.py runserver
```
El servidor estará disponible en http://127.0.0.1:8000/.

