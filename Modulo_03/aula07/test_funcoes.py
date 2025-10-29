# test_funcoes.py (Parte 2)
from funcoes import processar_lista, buscar_usuario

def test_processar_lista_ordenacao():# ativar no PowerShell (dot-source)
    lista_desordenada = [3, 1, 2, 4]
    lista_esperada = [1, 2, 3, 4]
    
    # O Pytest compara elemento por elemento para garantir a ordem
    assert processar_lista(lista_desordenada) == lista_esperada

def test_buscar_usuario_encontrado_completo():
    USUARIOS_TESTE = [
        {'id': 100, 'nome': 'Charlie', 'cargo': 'Dev'},
        {'id': 101, 'nome': 'Diana', 'cargo': 'Manager'}
    ]

    ID_EXISTENTE = 101
    usuario_esperado = {'id': 101, 'nome': 'Diana', 'cargo': 'Manager'}
    
    # Assert que o dicionário retornado é idêntico ao esperado
    assert buscar_usuario(USUARIOS_TESTE, ID_EXISTENTE) == usuario_esperado

def test_buscar_usuario_nao_encontrado():
    
    # Cenário de teste: Uma lista com dados, mas o ID não existe.
    USUARIOS_TESTE = [{'id': 50, 'nome': 'Ana', 'email': 'ana@exemplo.com'}]
    ID_INEXISTENTE = 999
        
    # Assert: O retorno DEVE ser o valor None (ausência de valor)
    resultado = buscar_usuario(USUARIOS_TESTE, ID_INEXISTENTE)
    assert resultado is None