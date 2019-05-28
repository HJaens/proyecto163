from django.conf.urls import url
from apps.historial.views import historial_view, historial_list,historial_pac,informe_historial_pac
from django.contrib.auth.decorators import login_required
app_name='historial'
urlpatterns = [
    url(r'^agregar',login_required(historial_view), name='agregar_historial'),
    url(r'^listar',login_required(historial_list), name='listar_historial'),
    url(r'^listar/(?P<ci>\d+)/$',login_required(historial_pac), name='historia_paciente'),
    url(r'^paciente/(?P<ci>\d+)/$',login_required(historial_pac), name='historia_paciente_x'),
    url(r'^informe/(?P<ci>\d+)/$',login_required(informe_historial_pac), name='informe_paciente'),
]