from django.contrib import admin

# Register your models here.

#from .models import Registrado
from apps.paciente.models import Perfilpaciente

#personalizamos el display de la administracion
class AdminRegistrado(admin.ModelAdmin):
    list_display = ["nombre","apellido","email","telefono"]
    form = Perfilpaciente
    list_display_links = ["nombre"]

    list_editable = ["email"]
    search_fields = ["email",'nombre']

   # class Meta:
   #    model = Registrado


admin.site.register(Perfilpaciente)

