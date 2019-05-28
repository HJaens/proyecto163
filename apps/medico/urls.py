from django.conf.urls import url
from apps.medico.views import medico_list,agregar_medico
from django.contrib.auth.decorators import login_required
app_name='medico'
urlpatterns = [
    url(r'^listar$', medico_list, name='listar_medico'),
    url(r'^registrar',login_required(agregar_medico), name="registrarm"),
]