from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Platillo
    path('platillo/ver/', views.ver_platillos, name='ver_platillos'),
    path('platillo/agregar/', views.agregar_platillo, name='agregar_platillo'),
    path('platillo/actualizar/<int:platillo_id>/', views.actualizar_platillo, name='actualizar_platillo'),
    path('platillo/borrar/<int:platillo_id>/', views.borrar_platillo, name='borrar_platillo'),

    # Cliente
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),

    # Mesa
    path('mesa/ver/', views.ver_mesas, name='ver_mesas'),
    path('mesa/agregar/', views.agregar_mesa, name='agregar_mesa'),
    path('mesa/actualizar/<int:mesa_id>/', views.actualizar_mesa, name='actualizar_mesa'),
    path('mesa/borrar/<int:mesa_id>/', views.borrar_mesa, name='borrar_mesa'),

    # Empleado
    path('empleado/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # Pedido
    path('pedido/ver/', views.ver_pedidos, name='ver_pedidos'),
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/actualizar/<int:pedido_id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedido/actualizar/realizar/<int:pedido_id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('pedido/borrar/<int:pedido_id>/', views.borrar_pedido, name='borrar_pedido'),
]
