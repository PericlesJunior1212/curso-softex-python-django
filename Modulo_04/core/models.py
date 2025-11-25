from django.db import models
from django.contrib.auth.models import User
class Tarefa(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    # 2. ADICIONE A NOVA RELAÇÃO
    # Cada Tarefa agora DEVE estar ligada a um Projeto.
    # Usamos uma referência por string para evitar import circular entre apps
    # formato: 'app_label.ModelName'
    projects = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tarefas')

    titulo = models.CharField(max_length=200)

    concluida = models.BooleanField(default=False)

    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
