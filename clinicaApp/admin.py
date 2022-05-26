from django.contrib import admin
from .models import Medico, Paciente, Turno,Pedido,Producto,Historial_medico,Vendedor

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','ultima_visita','doctor')
    list_filter=('ultima_visita',)
    date_hierarchy='ultima_visita'

class TurnoAdmin(admin.ModelAdmin):
    list_display=('fecha','paciente','medico','concurrio')

class PedidoAdmin(admin.ModelAdmin):
    list_display=('producto','paciente','precio','estado_del_pedido','vendedor','forma_de_Pago')
    list_filter=('fecha_pedido',)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class Historial_medicoAdmin(admin.ModelAdmin):
    list_display=('paciente','historial_medico')

class MedicoAdmin(admin.ModelAdmin):
    list_display=('nombre',)




admin.site.register(Turno, TurnoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Historial_medico, Historial_medicoAdmin)
admin.site.register(Vendedor)
