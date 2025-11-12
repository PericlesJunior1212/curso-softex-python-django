from django.shortcuts import redirect, render
from .models import Tarefa
from .forms import TarefaForm


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

def home(request):
    # 3. Lógica de POST: Se o formulário foi enviado
    if request.method == 'POST':
    # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
        # 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
            # 5. Salva o objeto no banco de dados!
            form.save()
            # 6. Redireciona de volta para a 'home'
            # Isso é o Padrão "Post-Redirect-Get" (PRG)
            return redirect('home')
    # Se o form NÃO for válido, o código continua e
    # o 'form' (com os erros) será enviado para o template
    # 7. Lógica de GET: Se o usuário apenas visitou a página
    else:
        form = TarefaForm() # Cria um formulário vazio
    # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas
    # 9. Atualize o contexto para incluir o formulário
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': todas_as_tarefas,
        'form': form, # 10. Envie o 'form' (vazio ou com erros) para o template
    }
    return render(request, 'home.html', context)