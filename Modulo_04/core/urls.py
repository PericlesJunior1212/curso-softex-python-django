# core/urls.py
from django.urls import path
from . import views
from .views import contagem_tarefas,duplicar_tarefa

urlpatterns = [
    path('home/', views.home, name='home'),
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    path('register/', views.register, name='register'),
    path('tarefas/contagem/', contagem_tarefas, name='contagem-tarefas'),
    path('tarefas/<int:tarefa_id>/duplicar/', duplicar_tarefa, name='duplicar_tarefa'),
]
