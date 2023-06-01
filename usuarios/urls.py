from django.urls import path
from django.contrib.auth import  views as auth_view
from usuarios.views import cad_usuario

urlpatterns =[
    path('login/',auth_view.LoginView.as_view(template_name ='usuarios/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(),name='logout'),
    path('cad_usuario/',cad_usuario,name="cad_usuario"),
]
