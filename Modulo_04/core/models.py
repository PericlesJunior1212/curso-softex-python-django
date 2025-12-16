from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from django.core.exceptions import ValidationError
from django.utils import timezone


class Tarefa(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tarefas')
    
    titulo = models.CharField(max_length=200)
    
    descricao=models.TextField(blank=True)
   
    concluida = models.BooleanField(default=False)
    
    criada_em = models.DateTimeField(auto_now_add=True)
    
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    
    prioridade = models.CharField(
        max_length=5,
        choices=PRIORIDADE_CHOICES,
        default='media'
    )

    prazo = models.DateField(null=False, blank=False)
    
    data_conclusao = models.DateTimeField(
        null=True,
        blank=True
    )
    
    def clean(self):
        if self.prazo and self.prazo < timezone.now().date():
            raise ValidationError({
                'prazo': 'O prazo não pode ser uma data no passado.'
            })
            
            
    def save(self, *args, **kwargs):
        if self.concluida and self.data_conclusao is None:
            self.data_conclusao = timezone.now()
        if not self.concluida:
            self.data_conclusao = None

        super().save(*args, **kwargs)
        

  
    def __str__(self):
        return self.titulo