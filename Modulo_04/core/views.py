from django.shortcuts import render
from .models import Tarefa
# Create your views here.

def home(request):
    todas_as_tarefas = Tarefa.objects.all()
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Admin'],
        'tarefas': todas_as_tarefas
    }
    return render(request, 'home.html', context)

def segundo(request):
    context = {
        'mensagem': 'Esta é a página segunda',
    }
    return render(request, 'base.html', context)