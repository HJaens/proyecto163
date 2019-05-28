from django import forms
from apps.historial.models import Historial
class HistorialForm(forms.ModelForm):

    class Meta:
        model = Historial
        fields = [
                'nrohistoria',
                'paciente',
                'medico',
                'hora',
                'caracteristica',
                'diagnostico',
                'receta',
        ]
        labels ={
            'nroHistoria': 'nrohistoria',
            'paciente': 'paciente',
            'medico': 'medico',
            'hora': 'fecha',
            'caracteristica': 'caracteristica',
            'diagnostico': 'diagnostico',
            'receta': 'receta'


        }
        widgets ={
            'nroHistoria': forms.IntegerField(),
            'paciente': forms.Select(attrs={'class':'form-control'}),
            'medico':forms.Select(attrs={'class':'form-control'}),
            'hora': forms.TextInput(attrs={'class':'form-control'}),
            'caracteristica': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnostico': forms.TextInput(attrs={'class':'form-control'}),
            'receta': forms.TextInput(attrs={'class': 'form-control'}),
        }