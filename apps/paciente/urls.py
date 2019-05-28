
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.paciente.views import paciente_list, paciente_edit, paciente_elim,agregar_paciente
app_name = "paciente"
urlpatterns = [
    url(r'^listar$', login_required(paciente_list), name='listar_paciente'),
    url(r'^editar/(?P<ci>\d+)/$',login_required(paciente_edit), name='editar_paciente'),
    url(r'^eliminar/(?P<ci>\d+)/$',login_required(paciente_elim), name='eliminar_paciente'),
    url(r'^registrar',login_required(agregar_paciente), name="registrar")
]