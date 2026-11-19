from django.urls import path
from . import views

app_name = 'inventario'
urlpatterns = [
    # 1️ GET - Ver todos los productos
    path('productos/', views.lista_productos, name='lista_productos'),
    
    # 2️ GET - Ver UN solo producto
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    # 3️ POST - Crear producto nuevo
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    
    # 4️ POST - Editar producto
    path('productos/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    
    # 5️ POST - Eliminar producto
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]