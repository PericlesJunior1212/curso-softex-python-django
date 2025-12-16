from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm
from django.contrib import messages 
from django.http import JsonResponse, HttpResponseNotAllowed



@login_required
def home(request):

    if request.method== 'POST':
        
        form = TarefaForm(request.POST, user=request.user)
        
        if form.is_valid():

            tarefa = form.save(commit=False) 
            tarefa.user = request.user 
            tarefa.full_clean()
            tarefa.save()
            
            return redirect('home')
    
    else:
        
        form = TarefaForm(user=request.user)



    
    todas_as_tarefas=Tarefa.objects.filter(user=request.user).order_by('-criada_em')

    context={
        'nome_usuario':request.user.username,
        'tecnologias': ['Autenticação','ForeignKey','Login','HTML','CSS','Django','SQL','Banco de Dados'],
        'tarefas': todas_as_tarefas,
        'form': form,
    }
    
    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):

    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)

    if request.method == 'POST':

        if not tarefa.concluida:
            tarefa.concluida = True
            tarefa.save()
            messages.success(request, "Parabéns! Tarefa concluida com sucesso!")
        else:
    
            tarefa.concluida = False
            tarefa.save()
            messages.warning(request,"Tarefa marcada como pendente")
        

        return redirect('home')

@login_required    
def deletar_tarefa(request, pk):

    tarefa = get_object_or_404(Tarefa, pk=pk,user=request.user)

    if request.method == 'POST':

        tarefa.delete()
        return redirect('home')

def register(request): 

    if request.method == 'POST': 

        form = UserCreationForm(request.POST) 

        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('home') 

    else: 
        form = UserCreationForm() 

    context = {'form': form}
    return render(request, 'register.html', context)

def contagem_tarefas(request):
    total = Tarefa.objects.count()
    concluidas = Tarefa.objects.filter(concluida=True).count()
    pendentes = Tarefa.objects.filter(concluida=False).count()

    return JsonResponse({
        "total": total,
        "concluidas": concluidas,
        "pendentes": pendentes
    })
    
def duplicar_tarefa(request, tarefa_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
    except Tarefa.DoesNotExist:
        return JsonResponse(
            {"erro": "Tarefa não encontrada"},
            status=404
        )

    nova_tarefa = Tarefa.objects.create(
        titulo=f"{tarefa.titulo} (Cópia)",
        descricao=tarefa.descricao,
        prioridade=tarefa.prioridade,
        prazo=tarefa.prazo,
        concluida=False
    )

    return JsonResponse({
        "mensagem": "Tarefa duplicada com sucesso",
        "nova_tarefa_id": nova_tarefa.id
    }, status=201)
    
    
def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})        