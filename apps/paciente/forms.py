from django import forms
from .models import Perfilpaciente

#otro formulario para contactos
class ContactoForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)



class PerfilForm(forms.ModelForm):
    class Meta:
        model=Perfilpaciente
        fields = [
            'username',
            'password',
            'tipo',
            'ci',
            'first_name',
            'last_name',
            'fecha_naci',
            'email',
            'telefono',
            'foto',
            'codigoqr'
        ]
        labels = {
            'username':'Nombre de Usuario',
            'password':'Contraseña',
            'tipo':'Tipo',
            'ci':'CI',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'fecha_naci':'Fecha Nacimiento',
            'email':'Email',
            'telefono':'telefono',
            'foto':'foto',
            'codigoqr':'Codigo QR'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'ci': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_naci': forms.DateInput(format='%d/%m/%Y'),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            #'foto':forms.ImageField()
        }
