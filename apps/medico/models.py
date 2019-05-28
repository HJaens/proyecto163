from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfilmedico(User):
    tipo=models.CharField(max_length=20,default='Medico')
    id_medico = models.IntegerField()
    area = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    foto= models.ImageField(upload_to='photosmedico',blank=True,null=True)

    def __str__(self):
        return '{}{}'.format(self.tipo, self.id_medico)
