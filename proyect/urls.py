"""proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.paciente import views
from apps.historial.views import historial_list
from apps.paciente import urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


app_name='inicio'
urlpatterns=[
    url(r'^accounts/login/', auth_views.LoginView.as_view(template_name='index.html'), name="login"),
    url(r'^$', auth_views.LoginView.as_view(template_name='index.html'), name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'^sesion/', views.inicio, name='inicio'),
    url(r'^historial/', include('apps.historial.urls', namespace='historial')),
    url(r'^paciente/', include('apps.paciente.urls', namespace='paciente')),
    url(r'^medico/', include('apps.medico.urls', namespace='medico')),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)