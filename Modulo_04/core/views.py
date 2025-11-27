from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from .models import Tarefa
from .forms import TarefaForm
from django.contrib import messages

@login_required
def home(request):
    # 3. Lógica de POST: Se o formulário foi enviado
    if request.method == 'POST':
    # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST, user=request.user)
        # 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
            # 5. Salva o objeto no banco de dados!
            tarefa = form.save(commit=False)
            
            tarefa.user = request.user
            
            tarefa.save()

            return redirect('home')
    # Se o form NÃO for válido, o código continua e
    # o 'form' (com os erros) será enviado para o template
    # 7. Lógica de GET: Se o usuário apenas visitou a página
    else:
        form = TarefaForm(user=request.user) # Cria um formulário vazio
    
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')

    context = {
        'nome_usuario': request.user.username, 
        'tecnologias': ['Autenticação', 'ForeignKey', 'Login'],
        'tarefas': todas_as_tarefas,
        'form': form,
}
    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):
    # 2. Modifique o 'get_object_or_404'
    # Busque a Tarefa pela 'pk' E ONDE o 'user' é o 'request.user'
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save() 
        # Não se esqueça de salvar!
        messages.success(request, 'Parabéns! Tarefa concluída com sucesso!')
        
    return redirect('home')



def deletar_tarefa(request, pk):
    # 1. Busca a tarefa
    tarefa = get_object_or_404(Tarefa, pk=pk,user=request.user)
    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        # 3. A Lógica de "Delete"
        tarefa.delete()
        # 4. Redireciona de volta para a 'home'
        return redirect('home')

def register(request):
    # Se a requisição for POST, o usuário enviou o formulário
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = UserCreationForm(request.POST)
        # Verifica se o formulário é válido (ex: senhas batem, username não existe)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco
            login(request, user) # Faz o login automático do usuário
            return redirect('home') # Redireciona para a home
    # Se a requisição for GET, o usuário apenas visitou a página
    else:
        form = UserCreationForm() # Cria um formulário de cadastro vazio

    # Prepara o contexto e renderiza o template
    context = {'form': form}
    return render(request, 'register.html', context)