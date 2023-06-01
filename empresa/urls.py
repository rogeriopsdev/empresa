"""empresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from empresaapp.views import agenda, avaliacao, status,empresa,servico,cad_servico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', agenda, name='agenda'),
    path('avaliacao/', avaliacao, name='avaliacao'),
    path('status/', status, name='status'),
    path('empresa/', empresa, name='empresa'),
    path('servico/', servico, name='servico'),
    path('cad_servico/', cad_servico, name='cad_servico'),
    path('', include('usuarios.urls')),
]
