from django.db import models
from django.db.models.deletion import PROTECT, CASCADE, SET_NULL
from django.db.models.enums import Choices
from django.contrib.auth.models import User


# Create your models here.
class Medico(models.Model):
    nombre=models.ForeignKey(User, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.nombre.get_username()

    class Meta:
        verbose_name='medico'
        verbose_name_plural='medicos'


class Vendedor(models.Model):
    nombre=models.ForeignKey(User, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.nombre.get_username()

    class Meta:
        verbose_name='vendedor'
        verbose_name_plural='vendedores'


class Paciente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    doctor=models.ForeignKey(Medico, on_delete=CASCADE, related_name='medico',null=True, blank=True)
    creado=models.DateTimeField(auto_now_add=True)
    ultima_visita=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    class Meta:
        verbose_name='paciente'
        verbose_name_plural='pacientes'

class Historial_medico(models.Model):
    paciente=models.ForeignKey(Paciente, on_delete=CASCADE, related_name='paciente', null=True,blank=True)
    historial_medico=models.TextField(null=True,blank=True)
    class Meta:
        verbose_name='historial_medico'
        verbose_name_plural='historiales_medicos'


class Turno(models.Model):
    paciente=models.ForeignKey(Paciente, on_delete=CASCADE)
    fecha=models.DateTimeField()
    medico=models.ForeignKey('Medico',on_delete=CASCADE)
    ultimaVisita=models.DateField(auto_now_add=True,blank=True, null=True)
    asistencia=(
        ('si',('si')),
        ('no',('no')),
        ('pendiente',('pendiente')),
    )

    concurrio = models.CharField(choices=asistencia, default='pendiente',max_length=20, blank=True, null=True)
    #concurrio=models.BooleanField(null=True)

    def __str__(self):
        return self.paciente.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre



class Pedido(models.Model):
    paciente=models.ForeignKey(Paciente, on_delete=CASCADE,blank=True, null=True)
    producto=models.ForeignKey(Producto, on_delete=CASCADE)
    
    vendedor=models.ForeignKey(Vendedor, on_delete=CASCADE,blank=True, null=True)
    fecha_pedido=models.DateField(auto_now_add=True,null=True)
    tipo=(
        ('cerca',('cerca')),
        ('lejos',('lejos')),
    )

    Cerca_o_Lejos = models.CharField(choices=tipo, default='',max_length=20, blank=True, null=True)
    lado=(
        ('izquierda',('izquierda')),
        ('derecha',('derecha')),
    )
    Derecha_o_Izquierda = models.CharField(choices=lado, default='',max_length=20, blank=True, null=True)
    marco=(
        ('si',('si')),
        ('no',('no')),
    )
    Marco = models.CharField(choices=marco, default='',max_length=20, blank=True, null=True)
    estado =(
        ('pendiente',('Pendiente')),
        ('taller',('Taller')),
        ('pedido',('Pedido')),
        ('finalizado',('Finalizado')),
        )
    estado_del_pedido = models.CharField(choices=estado, default='pendiente',max_length=50,blank=True,null=True)
    precio=models.IntegerField(null=True, blank=True)
    formaDePago=(
        ('Credito',('Credito')),
        ('Debito',('Debito')),
        ('Villetera virtual',('Billetera virtual')),
        ('Efectivo',('Efectivo')),
    )
    forma_de_Pago=models.CharField(choices=formaDePago, default='Efectivo', max_length=50,blank=True,null=True)
    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'



class Permisos(models.Model):
    class Meta:
        permissions = (
            ("view_gerencia", "Puede ver el gerencia"),
            ("view_precio", "Puede ver el precio"),
            ("view_paciente_secre", "Puede ver el pacientes "),
        )

