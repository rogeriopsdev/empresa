from django.urls import path
from django.contrib.auth import  views as autenticar
from usuarios.views import cad_usuario

urlpatterns ={
    path('login/',autenticar.LoginView.as_view(
        template_name ='usuarios/login.html'), name='login'
),
    path('cad_usuario/',cad_usuario,name="cad_usuario"),
}
