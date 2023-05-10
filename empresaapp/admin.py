from django.contrib import admin
from empresaapp.models import Avaliacao,Agenda,Status, Servico, Empresa

# Register your models here.
admin.site.register(Avaliacao)
admin.site.register(Agenda)
admin.site.register(Status)
admin.site.register(Servico)
admin.site.register(Empresa)
