from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.shortcuts import get_object_or_404


class ListaTarefasAPIView(APIView):
    """
    View para listar todas as tarefas (GET).
    Endpoints:
    GET /api/tarefas/ - Lista todas as tarefas
    """
    def get(self, request, format=None):
        """
        Retorna lista de todas as tarefas do banco.
        Returns:
        Response: JSON com lista de tarefas e status 200
        """
        # 1. BUSCAR: ORM do Django busca todos os registros
        tarefas = Tarefa.objects.all()
        # 2. SERIALIZAR: Converter objetos Python → JSON
        # many=True: indica que é uma lista de objetos
        serializer = TarefaSerializer(tarefas, many=True)
        # 3. RESPONDER: Retornar JSON com status HTTP
        return Response(serializer.data, status=status.HTTP_200_OK)
# core/views.py

class DetalheTarefaAPIView(APIView):
    """
    View para operações em recurso individual.
    GET, PUT, PATCH, DELETE /api/tarefas/<pk>/
    """
    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)
    # 4. GET (Buscar)
    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. PUT (Atualização Total)
    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 6. PATCH (Atualização Parcial)
    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(
        tarefa,
        data=request.data,
        partial=True # Permite omissão de campos
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 7. DELETE (Remoção)
    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)