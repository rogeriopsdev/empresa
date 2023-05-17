from django.urls import path
from django.contrib.auth import  views as autenticar

urlpatterns ={
    path('login/',autenticar.LoginView.as_view(
        template_name ='usuarios/login.html'), name='login'
),
}
