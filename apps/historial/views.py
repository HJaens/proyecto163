from django.shortcuts import render, redirect
from apps.historial.forms import HistorialForm
from apps.historial.models import Historial
from apps.paciente.models import Perfilpaciente
def historial_view(request):
        form = HistorialForm(request.POST or None)
        context = {
            "form": form
        }
        if form.is_valid():
            instance= form.save(commit=False)
            instance.save()
            context = {
                "titulo":"Historial Guardado"
            }
            return redirect('historial:listar_historial')
        return render(request,'agregar_historial.html',context)

def historial_list(request):
    #creamos nuestro query set
    historial = Historial.objects.all()
    contexto = {'historiales': historial}
    return render(request, 'listar_historial.html', contexto)

def historial_pac(request, ci):
    historial = Historial.objects.filter(paciente__ci=ci)
    contexto ={'historialp':historial}
    return render(request, 'listar_historialpac.html',contexto)

#funcion q lista historial d paciente x con su informacion
def informe_historial_pac(request, ci):
    historial = Historial.objects.filter(paciente__ci=ci)
    paciente = Perfilpaciente.objects.filter(ci=ci)
    contexto ={'historiales':historial, 'paciente':paciente}
    return render(request, 'informe_historial_paciente.html',contexto)