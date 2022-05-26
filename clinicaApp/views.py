from django.db.models.aggregates import Count
from django.shortcuts import redirect, render,get_object_or_404
from django.db.models import Sum
from .forms import Paciente_form, Pedido_form,Turno_form,Producto_form, Historial_medico_form, FiltrarForm, FiltrarForm2
from .models import Paciente, Pedido, Turno, Producto, Historial_medico
from django.views.generic import TemplateView
from django.contrib.auth.decorators import permission_required
from datetime import date, datetime, timedelta
from django.template import Library
from operator import itemgetter
# Create your views here.

#---------------------------------------------------- TURNOS ---------------------
class Index_view(TemplateView):
    template_name='clinicaApp/index.html'

'''  mirar video 6  '''
@permission_required('clinicaApp.add_turno')
def turno(request):
    context={
        'form':Turno_form
    }
    if request.method=='POST':
        formulario=Turno_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje']='Turno guardado'
        else:
            context['form']=formulario

    return render(request,'clinicaApp/turnos.html',context)

@permission_required('clinicaApp.change_turno')
def modificar_turno(request,id):
    turno=get_object_or_404(Turno,id=id)
    context={
        'form':Turno_form(instance=turno)
    }
    if request.method=='POST':
        formulario=Turno_form(data=request.POST,instance=turno)
        if formulario.is_valid():
            formulario.save()
            #context['mensaje']='Turno guardado'
            return redirect(to='listar_turnos')
        else:
            context['form']=formulario

    return render(request,'clinicaApp/modificar_turnos.html',context)

@permission_required('clinicaApp.delete_turno')
def eliminar_turno(request,id):
    turno=get_object_or_404(Turno,id=id)
    turno.delete()
    return redirect(to='listar_turnos')

@permission_required('clinicaApp.view_turno')
def listar_turnos(request):
    turnos=Turno.objects.order_by('-fecha')

    context={
        'turnos':turnos
        }
    return render(request,'clinicaApp/listar_turnos.html',context)

@permission_required('clinicaApp.view_gerencia')
def listar_turno_fecha(request):
    semana= date.today()-timedelta(days=7)
    filtroFecha=Turno.objects.filter(fecha__range=(semana, date.today()))
    context={
        'filtroFecha':filtroFecha,
    }
    return render(request, 'clinicaApp/listar_turno_fecha.html',context)

@permission_required('clinicaApp.view_gerencia')
def listar_turno_fecha30(request):
    
    if request.method == 'POST':
        mes = request.POST['mes']
        año, mes = mes.split('-')
        filtroFecha=Turno.objects.filter(fecha__month=mes, fecha__year=año)
        filtroOrd=filtroFecha.order_by('-fecha')
        context={
            'filtroFecha':filtroFecha,
            'filtroOrd':filtroOrd,
            'mes':mes,
            'año':año,

            }
        return render(request,'clinicaApp/listar_turno_fecha30.html',context)
    else:
        context={
            'filtrarForm2':FiltrarForm2
        }
        return render(request,'clinicaApp/listar_turno_fecha30.html', context)


@permission_required('clinicaApp.view_gerencia')
def listar_turno_concurrio_semana(request):
    semana= date.today()-timedelta(days=7)
    filtroFecha=Turno.objects.filter(fecha__range=(semana, date.today()))
    context={
        'filtroFecha':filtroFecha,
    }
    return render(request, 'clinicaApp/listar_turno_concurrio_semana.html',context)
    
@permission_required('clinicaApp.view_gerencia')
def listar_turno_concurrio_mes(request):
    if request.method == 'POST':
        mes = request.POST['mes']
        año, mes = mes.split('-')
        filtroFecha=Turno.objects.filter(fecha__month=mes, fecha__year=año)
        filtroOrd=filtroFecha.order_by('-fecha')
        context={
            'filtroFecha':filtroFecha,
            'filtroOrd':filtroOrd,
            'mes':mes,
            'año':año,
            }
        return render(request,'clinicaApp/listar_turno_concurrio_mes.html',context)
    else:
        context={
            'filtrarForm2':FiltrarForm2
        }
        return render(request, 'clinicaApp/listar_turno_concurrio_mes.html',context)


@permission_required('clinicaApp.view_paciente')
def listar_turnos2(request):
    turnos=Turno.objects.order_by('-fecha')
    
    if request.method == 'POST':

        fecha_desde = request.POST['fecha']
        fecha_hasta = request.POST['fecha_hasta']

        filtroFecha=Turno.objects.filter(fecha__range=[fecha_desde, fecha_hasta])
        filtroOrd=filtroFecha.order_by('-fecha')
        context={
            'turnos':turnos,
            'filtroFecha':filtroFecha,
            'fecha':fecha_desde,
            'fecha_hasta':fecha_hasta,
            'filtroOrd':filtroOrd,

            }
        return render(request,'clinicaApp/listar_turnos2.html',context)
    else:
        context={
            'turnos':turnos,
            'filtrarForm':FiltrarForm
        }
        return render(request,'clinicaApp/listar_turnos2.html', context)

#----------------------------------------------------- PACIENTES ----------------------------------

@permission_required('clinicaApp.view_paciente')
def listar_paciente(request):
    tabla=Paciente.objects.all()
    context={
        'tabla':tabla
    }
    return render(request,'clinicaApp/listar_paciente.html',context)

@permission_required('clinicaApp.view_historial_medico')
def pacienteXhistoria(request,paciente_id):
    historiaPaciente=Paciente.objects.get(id=paciente_id)
    tabla=Historial_medico.objects.filter(paciente=historiaPaciente)
    #historiaPaciente=get_object_or_404(Historial_medico,id=id)

    return render(request,'clinicaApp/pacienteXhistoria.html', {
        'tabla':tabla, 'historiaPaciente': historiaPaciente, })

@permission_required('clinicaApp.add_paciente')
def agregar_paciente(request):
    context={
        'form':Paciente_form
    }
    if request.method=='POST':
        formulario=Paciente_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje']='Paciente agregado'
        else:
            context['form']=formulario
    return render(request,'clinicaApp/agregar_paciente.html',context)

@permission_required('clinicaApp.change_paciente')
def modificar_paciente(request,id):
    paciente=get_object_or_404(Paciente,id=id)
    context={
        'form':Paciente_form(instance=paciente)
    }
    if request.method=='POST':
        formulario=Paciente_form(data=request.POST,instance=paciente)
        if formulario.is_valid():
            formulario.save()
            #context['mensaje']='Turno guardado'
            return redirect(to='listar_paciente')
        else:
            context['form']=formulario
    return render(request,'clinicaApp/modificar_paciente.html',context)

@permission_required('clinicaApp.delete_paciente')
def eliminar_paciente(request,id):
    paciente=get_object_or_404(Paciente,id=id)
    paciente.delete()
    return redirect(to='listar_paciente')


#--------------------------------------------------  PRODUCTO  -------------------------------------------

@permission_required('clinicaApp.add_producto')
def agregar_producto(request):
    context={
        'form':Producto_form
    }
    if request.method=='POST':
        formulario=Producto_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje']='Producto guardado'
        else:
            context['form']=formulario

    return render(request,'clinicaApp/agregar_producto.html',context)


@permission_required('clinicaApp.view_gerencia')
def listar_productos_vendidos(request):
    if request.method == 'POST':
        mes = request.POST['mes']
        año, mes = mes.split('-')
        filtroFecha=Pedido.objects.filter(fecha_pedido__month=mes, fecha_pedido__year=año)
        a={}
        for p in filtroFecha:
            a[p.producto]=a.get(p.producto,0)+1
        a_ord= dict(sorted(a.items(), key=itemgetter(1), reverse=True))

        context={
            'a_ord':a_ord,
            'filtroFecha':filtroFecha,
            'mes':mes,
            'año':año,
            }
        return render(request, 'clinicaApp/listar_productos_vendidos.html',context)
    else:
        context={
            'filtrarForm2':FiltrarForm2
        }
        return render(request, 'clinicaApp/listar_productos_vendidos.html',context)

@permission_required('clinicaApp.view_gerencia')
def listar_productos_vendidos_vendedor(request):
    if request.method == 'POST':
        mes = request.POST['mes']
        año, mes = mes.split('-')
        filtroFecha=Pedido.objects.filter(fecha_pedido__month=mes, fecha_pedido__year=año)
        a={}
        for p in filtroFecha:
            a[p.vendedor]=a.get(p.vendedor,0)+1
        a_ord= dict(sorted(a.items(), key=itemgetter(1), reverse=True))
        context={
            'a_ord':a_ord,
            'filtroFecha':filtroFecha,
            'año':año,
            'mes':mes,
        }
        return render(request, 'clinicaApp/listar_productos_vendidos_vendedor.html',context)
    else:
        context={
            'filtrarForm2':FiltrarForm2
        }
        return render(request, 'clinicaApp/listar_productos_vendidos_vendedor.html',context)

# -----------------------------------------------  PEDIDO  ------------------------------------

@permission_required('clinicaApp.add_pedido')
def agregar_pedido(request):
    data={  
        'pedido_form':Pedido_form()
    }
    if request.method == 'POST':
        pedido_form=Pedido_form(request.POST)
        if pedido_form.is_valid():
            pedido_form.save()
            data['mensaje']='pedido enviado'
            #aqui va rel render redirect
    else:
        pedido_form=Pedido_form()
    return render(request,'clinicaApp/pedido.html',data)

'''pedido = get_object_or_404(Pedido, pk=id_pedido)
    if (request.method == GET) and ("Aprobar" in request.GET):
        pedido.estado = 'entregado'
        pedido.save()
        # Send a Success Message to the User
    else:
        return render(request, 'index.html')'''

@permission_required('clinicaApp.change_pedido')
def modificar_pedido(request,id):
    pedido=get_object_or_404(Pedido,id=id)
    context={
        'form':Pedido_form(instance=pedido)
    }
    if request.method=='POST':
        formulario=Pedido_form(data=request.POST,instance=pedido)
        if formulario.is_valid():
            formulario.save()
            context['mensaje']='Modificado'
            return redirect(to='listar_pedidos')
        else:
            context['form']=formulario
    return render(request,'clinicaApp/modificar_pedido.html',context)


def estado_pedido(request, id):
    pedido=get_object_or_404(Pedido,id=id)
    
    if (request.method == 'GET') and ("pedido" in request.GET):
        pedido.estado_del_pedido = 'pedido'
        pedido.save()    
    elif (request.method == 'GET') and ("taller" in request.GET):
        pedido.estado_del_pedido = 'taller'
        pedido.save()
    elif (request.method == 'GET') and ("finalizado" in request.GET):
        pedido.estado_del_pedido = 'finalizado'
        pedido.save()
    return redirect(to='listar_pedidos')

@permission_required('clinicaApp.delete_pedido')
def eliminar_pedido(request,id):
    pedido=get_object_or_404(Pedido,id=id)
    pedido.delete()
    return redirect(to='listar_pedidos')

@permission_required('clinicaApp.view_pedido')
def listar_pedidos(request):

    total = Pedido.objects.all().aggregate(Sum('precio'))
    pedidos=Pedido.objects.order_by('-fecha_pedido')
    context= {
        'pedidos':pedidos,
        'total':total,
    }
    return render(request,'clinicaApp/listar_pedido.html',context)

@permission_required('clinicaApp.view_pedido')
def pedidosXpaciente(request,paciente_id):
    pedidoPaciente=Paciente.objects.get(id=paciente_id)
    pedidos=Pedido.objects.filter(paciente=pedidoPaciente)
    total = Pedido.objects.filter(paciente=pedidoPaciente).aggregate(Sum('precio'))
    return render(request,'clinicaApp/pedidosXpaciente.html', {
        'pedidoPaciente': pedidoPaciente,'pedidos':pedidos, 'total':total, })

@permission_required('clinicaApp.view_pedido')
def listar_pedido_fecha(request):
    semana= date.today()-timedelta(days=7)
    filtroFecha=Pedido.objects.filter(fecha_pedido__range=(semana, date.today()))
    a=set()
    for p in filtroFecha:
        a.add(p.paciente)

    context={
        'a':a,
    }
    return render(request, 'clinicaApp/listar_pedido_fecha.html',context)


@permission_required('clinicaApp.view_gerencia')
def listar_pedido_fecha30(request):
    if request.method == 'POST':
        mes = request.POST['mes']
        año, mes = mes.split('-')
        filtroFecha=Pedido.objects.filter(fecha_pedido__month=mes, fecha_pedido__year=año)
        filtroOrd=filtroFecha.order_by('-fecha_pedido')
        a=set()
        for p in filtroOrd:
            a.add(p.paciente)
        context={
            'a':a,
            'filtroFecha':filtroFecha,
            'filtroOrd':filtroOrd,
            'año':año,
            'mes':mes,
        }
        return render(request, 'clinicaApp/listar_pedido_fecha30.html',context)
    else:
        context={
            'filtrarForm2':FiltrarForm2
        }
        return render(request, 'clinicaApp/listar_pedido_fecha30.html',context)

# -------------------------------------------------------  HISTORIAL MEDICO  -----------------------------

@permission_required('clinicaApp.add_historial_medico')
def agregar_historia(request):
    context={
        'form':Historial_medico_form(),    
    }
    if request.method=='POST':
        form=Historial_medico_form(request.POST)
        if form.is_valid():
            form.save()
            context['mensaje']='historial creado'
    else:
        form=Historial_medico_form()
    return render(request,'clinicaApp/agregar_historia.html',context)



@permission_required('clinicaApp.change_historial_medico')
def modificar_historia(request,paciente_id):
    paciente_h=get_object_or_404(Historial_medico,id=paciente_id)
    context={
        'form':Historial_medico_form(instance=paciente_h)
    }
    if request.method=='POST':
        form=Historial_medico_form(data=request.POST,instance=paciente_h)
        if form.is_valid():
            form.save()
            #context['mensaje']='Turno guardado'
            return redirect(to='listar_turnos')
        else:
            context['form']=form
    return render(request,'clinicaApp/modificar_historia.html',context)

#-----------------------------------------------------  GERENCIA  ----------------------------------------

@permission_required('clinicaApp.view_gerencia')
def gerencia(request):

    return render(request,'clinicaApp/gerencia.html')








'''Si queremos ordenar por el valor y no por la clave, basta con usar el argumento key de sorted:

import operator

valores = {5: 20000, 3: 90000, 4: 15000} 
valores_ord = dict(sorted(valores.items(), key=operator.itemgetter(1)))
print(valores_ord)  # {4: 15000, 5: 20000, 3: 90000}
Extra
Si queremos invertir el orden basta con usar el argumento reverse de sorted:

valores = {5: 20000, 3: 10000, 4:1 5000} 
valores_ord = dict(sorted(valores.items(), reverse=True))
print(valores_ord)  # {5: 20000, 4: 15000, 3: 10000}
'''