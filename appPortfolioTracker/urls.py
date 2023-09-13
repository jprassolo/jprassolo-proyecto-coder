"""
URL configuration for prjPortfolioTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
#
# importo las views de la app
from appPortfolioTracker import views
from appPortfolioTracker.views import iactivos, ibonos, icryptos
from appPortfolioTracker.views import ilibros
from appPortfolioTracker.views import iportfolios, aportfolios
from appPortfolioTracker.views import index, acerca, contacto, terminos, politica
from appPortfolioTracker.views import pt


urlpatterns = [
    path('', views.index, name="index"),  #_ ambas hacen referencia a la misma vista
    # path('index/', index),            # 
    path('acerca'   , views.acerca  , name="acerca"),
    path('contacto' , views.contacto, name="contacto"),
    path('terminos' , views.terminos, name="terminos"),
    path('politica  ', views.politica, name="politica"),

    path('pt', views.pt, name="pt"),
    
    path('iactivos'     , views.iactivos, name="iactivos"),
    path('icryptos'     , views.icryptos, name="icryptos"),
    path('ibonos'     , views.ibonos, name="ibonos"),
    path('ilibros'      , views.ilibros, name="ilibros"),
    path('iportfolios'  , views.iportfolios, name="iportfolios"),
    path('aportfolios/<nombre>/<descripcion>', views.aportfolios, name="aportfolios"),
]