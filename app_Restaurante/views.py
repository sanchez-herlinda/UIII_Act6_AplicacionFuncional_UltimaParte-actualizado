from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Platillo, Cliente, Pedido, Mesa, Empleado


# ==========================
# INICIO
# ==========================
def inicio(request):
    total_platillos = Platillo.objects.count()
    total_clientes = Cliente.objects.count()
    total_pedidos = Pedido.objects.count()
    total_mesas = Mesa.objects.count()
    total_empleados = Empleado.objects.count()

    platillos = Platillo.objects.order_by('-id')[:5]
    clientes = Cliente.objects.order_by('-id')[:5]
    pedidos = Pedido.objects.order_by('-id')[:5]
    mesas = Mesa.objects.order_by('-id')[:3]
    empleados = Empleado.objects.order_by('-id')[:3]

    return render(request, 'inicio.html', {
        'total_platillos': total_platillos,
        'total_clientes': total_clientes,
        'total_pedidos': total_pedidos,
        'total_mesas': total_mesas,
        'total_empleados': total_empleados,
        'platillos': platillos,
        'clientes': clientes,
        'pedidos': pedidos,
        'mesas': mesas,
        'empleados': empleados,
    })

# ==========================
# CRUD PLATILLO
# ==========================
def ver_platillos(request):
    platillos = Platillo.objects.all().order_by('nombre')
    return render(request, 'platillo/ver_platillos.html', {'platillos': platillos})

def agregar_platillo(request):
    if request.method == 'POST':
        Platillo.objects.create(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio=request.POST.get('precio'),
            categoria=request.POST.get('categoria'),
            disponibilidad=True if request.POST.get('disponibilidad') == 'on' else False,
            ingredientes=request.POST.get('ingredientes'),
            tiempo_preparacion=request.POST.get('tiempo_preparacion')
        )
        return redirect('ver_platillos')
    return render(request, 'platillo/agregar_platillo.html')

def actualizar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        platillo.nombre = request.POST.get('nombre')
        platillo.descripcion = request.POST.get('descripcion')
        platillo.precio = request.POST.get('precio')
        platillo.categoria = request.POST.get('categoria')
        platillo.disponibilidad = True if request.POST.get('disponibilidad') == 'on' else False
        platillo.ingredientes = request.POST.get('ingredientes')
        platillo.tiempo_preparacion = request.POST.get('tiempo_preparacion')
        platillo.save()
        return redirect('ver_platillos')
    return render(request, 'platillo/actualizar_platillo.html', {'platillo': platillo})

def borrar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        platillo.delete()
        return redirect('ver_platillos')
    return render(request, 'platillo/borrar_platillo.html', {'platillo': platillo})


# ==========================
# CRUD CLIENTE
# ==========================
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion_casa=request.POST.get('direccion_casa'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento') or None,
            alergias=request.POST.get('alergias')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion_casa = request.POST.get('direccion_casa')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        cliente.alergias = request.POST.get('alergias')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


# ==========================
# CRUD MESA
# ==========================
def ver_mesas(request):
    mesas = Mesa.objects.all().order_by('id')
    return render(request, 'mesa/ver_mesas.html', {'mesas': mesas})

def agregar_mesa(request):
    if request.method == 'POST':
        Mesa.objects.create(
            dimensiones=request.POST.get('dimensiones'),
            numpersonas=request.POST.get('numpersonas'),
            estado=request.POST.get('estado'),
            capacidad=request.POST.get('capacidad'),
            descripcion=request.POST.get('descripcion')
        )
        return redirect('ver_mesas')
    return render(request, 'mesa/agregar_mesa.html')

def actualizar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        mesa.dimensiones = request.POST.get('dimensiones')
        mesa.numpersonas = request.POST.get('numpersonas')
        mesa.estado = request.POST.get('estado')
        mesa.capacidad = request.POST.get('capacidad')
        mesa.descripcion = request.POST.get('descripcion')
        mesa.save()
        return redirect('ver_mesas')
    return render(request, 'mesa/actualizar_mesa.html', {'mesa': mesa})

def borrar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        mesa.delete()
        return redirect('ver_mesas')
    return render(request, 'mesa/borrar_mesa.html', {'mesa': mesa})


# ==========================
# CRUD EMPLEADO
# ==========================
def ver_empleados(request):
    empleados = Empleado.objects.all().order_by('apellido')
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            puesto=request.POST.get('puesto'),
            salario=request.POST.get('salario'),
            telefono=request.POST.get('telefono'),
            correo=request.POST.get('correo')
        )
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.puesto = request.POST.get('puesto')
        empleado.salario = request.POST.get('salario')
        empleado.telefono = request.POST.get('telefono')
        empleado.correo = request.POST.get('correo')
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# ==========================
# CRUD PEDIDO (actualizado con Mesa y Empleado)
# ==========================
def ver_pedidos(request):
    pedidos = Pedido.objects.select_related('cliente', 'platillo', 'mesa', 'empleado').all().order_by('-fechahora')
    return render(request, 'pedido/ver_pedidos.html', {'pedidos': pedidos})

def agregar_pedido(request):
    clientes = Cliente.objects.all().order_by('apellido')
    platillos = Platillo.objects.filter(disponibilidad=True).order_by('nombre')
    mesas = Mesa.objects.all().order_by('id')
    empleados = Empleado.objects.all().order_by('apellido')

    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente'))
        platillo = get_object_or_404(Platillo, id=request.POST.get('platillo'))
        mesa = get_object_or_404(Mesa, id=request.POST.get('mesa'))
        empleado = get_object_or_404(Empleado, id=request.POST.get('empleado'))
        cantidad = int(request.POST.get('cantidad') or 1)
        estado = request.POST.get('estado') or 'Pendiente'
        notas = request.POST.get('notas', '').strip()
        total = platillo.precio * cantidad

        Pedido.objects.create(
            cliente=cliente,
            platillo=platillo,
            mesa=mesa,
            empleado=empleado,
            cantidad=cantidad,
            estado=estado,
            notas=notas,
            total=total
        )
        return redirect('ver_pedidos')

    return render(request, 'pedido/agregar_pedido.html', {
        'clientes': clientes,
        'platillos': platillos,
        'mesas': mesas,
        'empleados': empleados,
    })

def actualizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    clientes = Cliente.objects.all().order_by('apellido')
    platillos = Platillo.objects.all().order_by('nombre')
    mesas = Mesa.objects.all().order_by('id')
    empleados = Empleado.objects.all().order_by('apellido')
    return render(request, 'pedido/actualizar_pedido.html', {
        'pedido': pedido,
        'clientes': clientes,
        'platillos': platillos,
        'mesas': mesas,
        'empleados': empleados,
    })

def realizar_actualizacion_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=request.POST.get('cliente'))
        platillo = get_object_or_404(Platillo, id=request.POST.get('platillo'))
        mesa = get_object_or_404(Mesa, id=request.POST.get('mesa'))
        empleado = get_object_or_404(Empleado, id=request.POST.get('empleado'))
        cantidad = int(request.POST.get('cantidad') or 1)
        estado = request.POST.get('estado') or pedido.estado
        notas = request.POST.get('notas', '').strip()
        total = platillo.precio * cantidad

        pedido.cliente = cliente
        pedido.platillo = platillo
        pedido.mesa = mesa
        pedido.empleado = empleado
        pedido.cantidad = cantidad
        pedido.estado = estado
        pedido.notas = notas
        pedido.total = total
        pedido.save()

        return redirect('ver_pedidos')

    return redirect('ver_pedidos')

def borrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})
