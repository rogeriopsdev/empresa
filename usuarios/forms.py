from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Usuarioform(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
