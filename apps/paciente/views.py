from django.shortcuts import render, redirect
from apps.paciente.models import Perfilpaciente
from apps.paciente.forms import PerfilForm


# Create your views here.
#import crispy_forms
def inicio(request):
    titulo = "Bienvenidos"
    if request.user.is_authenticated:
        titulo = "bienvenido %s" %(request.user)
        paciente= Perfilpaciente.objects.filter(username=request.user)
        context={
            'titulo':titulo,
            'paciente':paciente
        }
    else:
        context={
            'titulo':titulo
        }
    return render(request, "login.html",context)

#funcion q adiciona un nuevo Usuario Paciente
def agregar_paciente(request):
   form = PerfilForm(request.POST or None, request.FILES or None)
   context = {
       "form":form
   }
   if form.is_valid():
       form.save()
       return redirect('paciente:listar_paciente')
   return render(request,"registrar.html",context)

#funcion q lista a los pacientes
def paciente_list(request):
    paciente = Perfilpaciente.objects.all()
    contexto = {'pacientes': paciente}
    return render(request, 'listar_paciente.html', contexto)
#funcion q edita a un paciente con ci
def paciente_edit(request, ci):
    paciente = Perfilpaciente.objects.get(ci=ci)
    if request.method == 'GET':
        form = PerfilForm(instance=paciente)
    else:
        form = PerfilForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('/paciente/listar')
    return render(request, 'agregar_historial.html', {'form': form})
#funcion q elimina a un paciente con ci
def paciente_elim(request, ci):
        paciente = Perfilpaciente.objects.get(ci=ci)
        if request.method == 'POST':
            paciente.delete()
            return redirect('/paciente/listar')
        return render(request, 'eliminar_paciente.html', {'paciente': paciente})



