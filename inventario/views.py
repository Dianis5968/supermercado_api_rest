from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from.forms import ProductoForm

# 1️ GET - Mostrar todos los productos
def lista_productos(request):
    # request.method == "GET"  →  Solo lee información
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

# 2️ GET - Ver un solo producto
def detalle_producto(request, producto_id):
    # Busca UN producto específico por su número (ID)
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})

# 3️ POST - Crear un producto nuevo
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'inventario/formulario_producto.html', {'form': form})
    
  

# 4️ POST - Editar un producto existente
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == "POST":
        # Actualizamos TODOS los datos del producto
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.cantidad = request.POST.get('cantidad')
        producto.categoria_id = request.POST.get('categoria')
        producto.save()
        return redirect('inventario:lista_productos')
    
    # Mostramos el formulario con los datos actuales
    return render(request, 'inventario/formulario_editar.html', {'producto': producto})

# 5️ POST - Eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()  # 🗑️ Borra el producto de la base de datos
    return redirect('lista_productos')