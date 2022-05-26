from django import forms
from django.forms import fields
from django.forms import widgets
from .models import Pedido, Turno, Producto, Paciente, Historial_medico


class Pedido_form(forms.ModelForm):
    class Meta:
        model=Pedido
        fields=[
            'paciente',
            'producto',
            'Cerca_o_Lejos',
            'Derecha_o_Izquierda',
            'Marco',
            'precio',
            'forma_de_Pago',
            'vendedor',
        ]
class DateImput(forms.DateInput):
    imput_type = 'date'
class FiltrarForm(forms.Form):
    my_date_field = forms.DateField(widget=DateImput)

class DateImput2(forms.DateInput):
    imput_type = 'month'
class FiltrarForm2(forms.Form):
    my_date_field = forms.DateField(widget=DateImput2)


class Turno_form(forms.ModelForm):
    class Meta:
        model=Turno
        fields=[
            'paciente',
            'fecha',
            'medico',
            'concurrio',
        ]
        #widgets video 9
        widgets={
            'fecha':forms.DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%dT%H:%M')
            
        }

class Producto_form(forms.ModelForm):
    class Meta:
        model=Producto
        fields= '__all__'

class Paciente_form(forms.ModelForm):
    class Meta:
        model=Paciente
        fields={
            'apellido',
            'nombre',
        }

class Historial_medico_form(forms.ModelForm):
    class Meta:
        model=Historial_medico
        fields='__all__'

