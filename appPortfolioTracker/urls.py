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
from appPortfolioTracker.views import iactivos
from appPortfolioTracker.views import ilibros
from appPortfolioTracker.views import iportfolios, aportfolios
from appPortfolioTracker.views import index, acerca, contacto, terminos, politica
from appPortfolioTracker.views import main


urlpatterns = [
    path('', index),            #_ ambas hacen referencia a la misma vista
    # path('index/', index),      # 
    path('acerca/', acerca),
    path('contacto/', contacto),
    path('terminos/', terminos),
    path('politica/', politica),

    path('main/', main),
    
    path('iactivos/', iactivos),

    path('ilibros/', ilibros),

    path('iportfolios/', iportfolios),
    path('aportfolios/<nombre>/<descripcion>', aportfolios),    
]

# urlpatterns = [
#     path('', index),            #_ ambas hacen referencia a la misma vista
#     path('index/', index, name=index),      # 
#     path('acerca/', acerca, name=acerca),
#     path('contacto/', contacto, name=contacto),
#     path('terminos/', terminos, name=terminos),
#     path('politica/', politica, name=politica),

#     path('admin', admin, name=admin),
    
#     path('iactivos/', iactivos, name=iactivos),

#     path('ilibros/', ilibros, name=ilibros),

#     path('iportfolios/', iportfolios, name=iportfolios),
#     path('aportfolios/<nombre>/<descripcion>', aportfolios, name=aportfolios),    
# ]