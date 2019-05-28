from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfilpaciente(User):
    tipo=models.CharField(max_length=20, default='Paciente')
    ci = models.IntegerField()
    fecha_naci = models.DateField(max_length=50)
    telefono = models.IntegerField()
    foto = models.ImageField(upload_to='photospaciente',blank=True,null=True)
    codigoqr = models.ImageField(upload_to='codigos_qr',blank=True,null=True)
    def __str__(self):
        return '{}{}'.format(self.tipo, self.ci)


