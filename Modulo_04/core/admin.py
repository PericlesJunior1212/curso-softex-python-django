from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user','get_user_email', 'concluida', 'criada_em','project', 'prioridade',
        'prazo','data_conclusao',)
    list_filter = ('concluida', 'user', 'criada_em','project','prioridade', 'concluida')
    search_fields = ('titulo', 'user__username','project','descricao')
    fieldsets = (
        ('Informações Principais', {
            'fields': ('user','project', 'titulo')
        }),
        ('Status da Tarefa', {
            'fields': ('concluida', 'criada_em')
        }),
    )
    readonly_fields = ('criada_em',)

    @admin.display(description='Email do Usuário')
    def get_user_email(self, obj):
        return obj.user.email


admin.site.register(Tarefa, TarefaAdmin)