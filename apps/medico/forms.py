from django import forms
from apps.medico.models import Perfilmedico

class PerfilForm(forms.ModelForm):
    class Meta:
        model=Perfilmedico
        fields = [
            'username',
            'tipo',
            'id_medico',
            'first_name',
            'last_name',
            'area',
            'especialidad',
            'email',
            'foto'

        ]
        labels = {
            'username':'Nombre de Usuario',
            'tipo':'Tipo',
            'id_medico':'ID_medico',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'area':'Area Trabajo',
            'especialidad':'Especialidad',
            'email':'Correo',
            'foto':'Foto'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'id_medico': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.DateInput(format='%d/%m/%Y'),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
