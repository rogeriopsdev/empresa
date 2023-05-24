from django.shortcuts import render, redirect
from usuarios.forms import Usuarioform

# Create your views here.
def cad_usuario(request):
    form = Usuarioform(request.POST)
    if request.method == "POST":
        form = Usuarioform(request.POST, request.FILES)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            return redirect('login')
    return render(request,'usuarios/cad_usuario.html',{'form':form})