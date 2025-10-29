import random


def encontrar_intersecao(lista1, lista2):
    """Encontra e retorna os elementos comuns entre duas listas.

    Argumentos:
      lista1 (list): A primeira lista de números inteiros.
      lista2 (list): A segunda lista de números inteiros.

    Retorna:
      list: Uma nova lista contendo os elementos que estão presentes em ambas
            as listas, sem repetição.
    """
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    intersecao_conjunto = conjunto1 & conjunto2

    return list(intersecao_conjunto)


# Alias com o nome usado em alguns testes
intersecao = encontrar_intersecao


if __name__ == "__main__":
    # Exemplo de uso (só executa quando rodado diretamente)
    lista1 = []
    lista2 = []
    for _ in range(3):
        lista1.append(random.randint(1, 5))
        lista2.append(random.randint(1, 5))

    print(encontrar_intersecao(lista1, lista2))
