from clinicaApp.views import Index_view
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
                #--------------INDEX----------

        path('', Index_view.as_view(), name='index'),
        #path('pedido_paciente/', views.pedido_paciente, name='pedido_paciente'),
        #path('listar_pedidos/<int:paciente_id>/', views.pedido_paciente, name='pedido_paciente'),


                #--------------TURNOS----------

        path('turnos/', views.turno, name='turnos'),
        path('listar_turnos/', views.listar_turnos, name='listar_turnos'),
        path('listar_turnos2/', views.listar_turnos2, name='listar_turnos2'),
        path('modificar_turno/<id>/', views.modificar_turno, name='modificar_turno'),
        path('eliminar_turno/<id>/', views.eliminar_turno, name='eliminar_turno'),
        path('estado_pedido/<id>/', views.estado_pedido, name='estado_pedido'),


                #--------------PRODUCTO----------

        path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
        path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),

                #--------------PACIENTE----------

        path('listar_paciente/', views.listar_paciente, name='listar_paciente'),
        path('listar_paciente/pacienteXhistoria/<int:paciente_id>/', views.pacienteXhistoria, name='pacienteXhistoria'),
        path('modificar_paciente/<id>/', views.modificar_paciente, name='modificar_paciente'),
        path('eliminar_paciente/<id>/', views.eliminar_paciente, name='eliminar_paciente'),

                #--------------historia clinic----------

        path('modificar_historia/<int:paciente_id>/', views.modificar_historia, name='modificar_historia'),
        path('agregar_historia/', views.agregar_historia, name='agregar_historia'),

                #--------------pedidos----------

        path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
        path('agregar_pedido/', views.agregar_pedido, name='agregar_pedido'),
        path('listar_pedidos/pedidosXpaciente/<int:paciente_id>/', views.pedidosXpaciente, name='pedidosXpaciente'),        
        path('modificar_pedido/<id>/', views.modificar_pedido, name='modificar_pedido'),
        path('eliminar_pedido/<id>/', views.eliminar_pedido, name='eliminar_pedido'),
                #--------------gerencia----------

        path('gerencia/', views.gerencia, name='gerencia'),
        path('listar_pedido_fecha/', views.listar_pedido_fecha, name='listar_pedido_fecha'),
        path('listar_pedido_fecha30/', views.listar_pedido_fecha30, name='listar_pedido_fecha30'),
        path('listar_turno_fecha/', views.listar_turno_fecha, name='listar_turno_fecha'),
        path('listar_turno_fecha30/', views.listar_turno_fecha30, name='listar_turno_fecha30'),
        path('listar_turno_concurrio_semana/', views.listar_turno_concurrio_semana, name='listar_turno_concurrio_semana'),
        path('listar_turno_concurrio_mes/', views.listar_turno_concurrio_mes, name='listar_turno_concurrio_mes'),
        path('listar_productos_vendidos/', views.listar_productos_vendidos, name='listar_productos_vendidos'),
        path('listar_productos_vendidos_vendedor/', views.listar_productos_vendidos_vendedor, name='listar_productos_vendidos_vendedor'),
        

]
