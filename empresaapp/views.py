from django.shortcuts import render

# Create your views here.
def agenda(request):
    return render(request, 'empresa/agenda.html')

def avaliacao(request):
    return render(request, 'empresa/avaliacao.html')

def empresa(request):
    return render(request, 'empresa/empresa.html')

def servico(request):
    return render(request, 'empresa/servico.html')

def status(request):
    return render(request, 'empresa/status.html')


