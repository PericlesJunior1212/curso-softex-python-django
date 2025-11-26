from django import forms
from .models import Tarefa
from projects.models import Project  # Importe o Project


class TarefaForm(forms.ModelForm):
    """Formulário para criação/edição de Tarefa.

    Recebe um argumento extra `user` no construtor para filtrar os
    projetos disponíveis no campo `project`.
    """

    def __init__(self, *args, **kwargs):
        # Capture o 'user' que será passado pela view (ou None)
        user = kwargs.pop('user', None)
        # Chame o construtor original (pai)
        super().__init__(*args, **kwargs)

        # Se o 'user' foi passado, filtre as opções do campo 'project'
        if user and 'project' in self.fields:
            self.fields['project'].queryset = Project.objects.filter(user=user)

    class Meta:
        model = Tarefa
        # Escolha os campos expostos pelo formulário
        fields = ['titulo', 'project']













        