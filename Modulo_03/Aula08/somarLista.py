def somar_listas(lista1, lista2):
    """Soma duas listas elemento por elemento.
    
    Se as listas tiverem tamanhos diferentes, soma até onde há elementos
    em ambas e depois mantém os elementos restantes da lista maior.
    """
    if len(lista1) > len(lista2):
        lista_maior = lista1
        lista_menor = lista2
    else:
        lista_maior = lista2
        lista_menor = lista1
        
    resultado = []
    
    for i in range(len(lista_maior)):
        try:
            soma = lista_maior[i] + lista_menor[i]
            resultado.append(soma)
        except IndexError:
            resultado.append(lista_maior[i])
            
    return resultado

if __name__ == '__main__':
    # Código de exemplo
    lista1 = [1, 2, 3, 4]
    lista2 = [1, 2]
    print(somar_listas(lista1, lista2))
