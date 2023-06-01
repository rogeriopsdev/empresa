from django.shortcuts import render
from .forms import ServicoForm

# Create your views here.
def agenda(request):
    return render(request, 'empresa/agenda.html')

def avaliacao(request):
    return render(request, 'empresa/avaliacao.html')

def empresa(request):
    return render(request, 'empresa/empresa.html')

def servico(request):
    return render(request, 'empresa/servico.html')


def cad_servico(request):
    form = ServicoForm(request.POST)
    if request.method =='POST':
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = ServicoForm()
    return render(request, 'empresa/cad_servico.html',{'form':form})

def status(request):
    return render(request, 'empresa/status.html')


