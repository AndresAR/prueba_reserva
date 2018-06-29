from django import forms
from django.forms import ModelForm
from .models import Reservacion


class ReservaForm(forms.ModelForm):
         
    class Meta:
        model = Reservacion

        fields = [
            'sala',
            'fecha',
            'hora_inicio',   
            'hora_termino',
            'capacidad',
            'insumos',
            

        ]
        labels = {  
            'fecha' : 'Fecha',
            'hora_inicio' : 'Inicio',
            'hora_termino': 'Termino',
            'capacidad'        : 'Cantidad Personas',
            'insumos'      : 'Cantidad Insumos',
            'sala'      : 'Sala',
        }
        widgets = {
            'sala':             forms.Select(attrs={'class': 'form-control col-lg-12'}),
            'fecha'      :      forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha'}),
            'hora_inicio':      forms.TextInput(attrs={'class': 'form-control'}),
            'hora_termino':     forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad':        forms.Select(attrs={'class': 'form-control'}),
            'insumos':          forms.Select(attrs={'class': 'form-control'}),
        }
    