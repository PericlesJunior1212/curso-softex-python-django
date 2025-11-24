# core/admin.py

from django.contrib import admin
from .models import Tarefa
class TarefaAdmin(admin.ModelAdmin):

    # 'list_display' é uma tupla com os nomes dos campos
    # que queremos exibir como colunas na lista
    list_display = ('titulo', 'user', 'get_user_email', 'concluida', 'criada_em')
    list_filter = ('concluida', 'user', 'criada_em')
    search_fields = ('titulo', 'user__username')
    
    
    fieldsets = (
         ('Informações Principais', {
        'fields': ('user', 'titulo')
         }),
         ('Status da Tarefa', {
         'fields': ('concluida', 'criada_em')
         }),
)
    
    readonly_fields = ('criada_em',)
    
    @admin.display(description='Email do Usuário') # Define o título da coluna
    def get_user_email(self, obj):
        return obj.user.email

admin.site.register(Tarefa,TarefaAdmin)