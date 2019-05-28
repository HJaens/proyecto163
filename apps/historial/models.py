from django.db import models
from apps.medico.models import Perfilmedico
from apps.paciente.models import Perfilpaciente
from django.utils import timezone
import datetime
# Create your models here.



class Historial(models.Model):
    #paciente a historias 1 a N
    nrohistoria = models.IntegerField()

    paciente = models.ForeignKey(Perfilpaciente, default=None,null=True, blank=True, on_delete=models.CASCADE)
    medico = models.ForeignKey(Perfilmedico, default=None,null=True, blank=True, on_delete=models.CASCADE)
    hora = models.DateField(default=datetime.date.today )
    caracteristica = models.TextField()
    diagnostico = models.CharField(max_length=30)
    receta = models.CharField(max_length=200)

    def __str__(self):
        return self.diagnostico