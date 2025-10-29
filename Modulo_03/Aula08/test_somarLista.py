from somarLista import somar_listas


def test_somar_listas_mesmo_tamanho():
    """Testa a soma de duas listas do mesmo tamanho."""
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    resultado_esperado = [5, 7, 9]  # 1+4, 2+5, 3+6
    
    assert somar_listas(lista1, lista2) == resultado_esperado

def test_somar_listas_tamanhos_diferentes_primeira_maior():
    """Testa quando a primeira lista é maior que a segunda."""
    lista1 = [1, 2, 3, 4]
    lista2 = [1, 2]
    resultado_esperado = [2, 4, 3, 4]  # soma até onde tem par, depois mantém valores da maior
    
    assert somar_listas(lista1, lista2) == resultado_esperado

def test_somar_listas_tamanhos_diferentes_segunda_maior():
    """Testa quando a segunda lista é maior que a primeira."""
    lista1 = [1, 2]
    lista2 = [4, 5, 6, 7]
    resultado_esperado = [5, 7, 6, 7]  # soma até onde tem par, depois mantém valores da maior
    
    assert somar_listas(lista1, lista2) == resultado_esperado

def test_somar_listas_vazia():
    """Testa quando uma das listas está vazia."""
    lista1 = []
    lista2 = [1, 2, 3]
    resultado_esperado = [1, 2, 3]  # deve retornar a lista não-vazia
    
    assert somar_listas(lista1, lista2) == resultado_esperado
    assert somar_listas(lista2, lista1) == resultado_esperado  # ordem não deve importar