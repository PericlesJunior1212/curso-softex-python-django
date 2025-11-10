from django.shortcuts import render
from .models import Tarefa
# Create your views here.
def home(request):
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
    }
    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    return render(request, 'home.html', context)

def home(request):

    todas_as_tarefas = Tarefa.objects.all()
# 3. Atualize o contexto
    context = {
    'nome_usuario': 'Júnior',
    'tecnologias': ['Python', 'Django', 'Models', 'Admin'],
    'tarefas': todas_as_tarefas # 4. Adicione as tarefas ao contexto
    }
    return render(request, 'home.html', context)