from django.shortcuts import render,redirect
from apps.medico.models import Perfilmedico
from apps.medico.forms import PerfilForm
# Create your views here.
def medico_list(request):
    medico = Perfilmedico.objects.all().order_by('id_medico')
    contexto = {'medicos': medico}
    return render(request, 'listar_medico.html', contexto)

#funcion q adiciona un nuevo Usuario Medico
def agregar_medico(request):

    form = PerfilForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            "titulo": "Usuario Registrado"
        }
        return redirect('medico:listar_medico')
    return render(request, "registrar.html", context)