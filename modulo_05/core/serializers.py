from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Tarefa"""

    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'criada_em', 'user']
        read_only_fields = ['id', 'criada_em', 'user']
