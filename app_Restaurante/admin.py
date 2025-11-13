from django.contrib import admin
from .models import Platillo, Cliente, Pedido, Mesa, Empleado

@admin.register(Platillo)
class PlatilloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponibilidad', 'tiempo_preparacion')
    search_fields = ('nombre', 'categoria')
    list_filter = ('disponibilidad', 'categoria')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email')


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'dimensiones', 'numpersonas', 'estado', 'capacidad')
    search_fields = ('estado',)
    list_filter = ('estado',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'puesto', 'salario', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido', 'puesto')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechahora', 'cliente', 'platillo', 'mesa', 'empleado', 'cantidad', 'estado', 'total')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'estado')
    list_filter = ('estado',)
    readonly_fields = ('fechahora',)

