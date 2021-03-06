"""ContraCNO URL Configuration

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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from usuario.views import Ingreso, LogoutView
from Enrolamiento import views as enrol
from Informe import views as info
from EntregaDNI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(views.inicio), name='Inicio'),
    path('ingreso', Ingreso.as_view(), name='Ingreso'),
    path('cierre', login_required(LogoutView.as_view()), name='Cierre'),
    path('escaner-caja', login_required(views.EscanerCaja.as_view()), name='EscanerCaja'),
    path('cajas', login_required(views.ListaCajas.as_view()), name='ListaCajas'),
    path('centros', login_required(views.ListaCentros.as_view()), name='ListaCentros'),
    path('editar-centro/<int:pk>', login_required(views.EditarCentro.as_view()), name='EditarCentro'),
    path('crear-centro', login_required(views.CrearCentro.as_view()), name='CrearCentro'),
    path('escaner-sobre', login_required(views.EscanerSobre.as_view()), name='EscanerSobre'),
    path('escaner-sobre-usuario', login_required(views.EscanerSobreUsuario.as_view()), name='EscanerSobreUsuario'),
    path('sobres', login_required(views.ListaSobres.as_view()), name='ListaSobres'),
    path('sobres_hoy', login_required(views.sobres_hoy), name='sobres_hoy'),
    path('sobres/eliminar/<int:pk>', login_required(views.EliminarSobre.as_view()), name="EliminarSobre"),
    path('acta-cierre', login_required(info.ActaCierre.as_view()), name='ActaCierre'),
    path('acta-cierre/imprimir', login_required(info.ActaCierreImprimir.as_view()), name='ActaCierreImprimir'),
    path('acta-apertura/imprimir', login_required(info.ActaAperturaImprimir.as_view()), name='ActaAperturaImprimir'),
    path('informes', login_required(info.Informes.as_view()), name='Informes'),
    path('entregadas', login_required(info.EntregadosUsuario.as_view()), name='EntregadosUsuario'),
    path('escaner-recibo', login_required(enrol.EscanerRecibo.as_view()), name='EscanerRecibo'),
    path('sedes', login_required(enrol.ListaSedes.as_view()), name='ListaSedes'),
    path('sedes/<int:pk>', login_required(enrol.DetalleSede.as_view()), name='DetalleSede'),
    path('sedes/crear', login_required(enrol.CrearSede.as_view()), name='CrearSede'),
    path('sedes/<int:pk>/editar', login_required(enrol.EditarSede.as_view()), name='EditarSede'),
    path('sedes/<int:pk>/eliminar', login_required(enrol.EliminarSede.as_view()), name='EliminarSede'),
    path('domiciliarias', login_required(views.ListaDomiciliarias.as_view()), name='ListaDomiciliarias'),
    path('domiciliarias/crear', login_required(views.CrearDomiciliaria.as_view()), name='CrearDomiciliaria'),
    path('domiciliarias/<int:pk>/editar', login_required(views.EditarDomiciliaria.as_view()), name='EditarDomiciliaria'),
    path('domiciliarias/<int:pk>/eliminar', login_required(views.EliminarDomiciliaria.as_view()), name='EliminarDomiciliaria'),
]
