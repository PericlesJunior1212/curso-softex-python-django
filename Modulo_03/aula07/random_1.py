import random

def encontrar_intersecao(lista1, lista2):
  """
  Encontra e retorna os elementos comuns entre duas listas.

  Argumentos:
    lista1 (list): A primeira lista de números inteiros.
    lista2 (list): A segunda lista de números inteiros.

  Retorna:
    list: Uma nova lista contendo os elementos que estão presentes em ambas
          as listas, sem repetição.
  """
  # Converte as listas para conjuntos (sets) para remover duplicatas e 
  # realizar a interseção de forma eficiente.
  conjunto1 = set(lista1)
  conjunto2 = set(lista2)

  # Realiza a operação de interseção usando o operador '&'.
  intersecao_conjunto = conjunto1 & conjunto2

  # Converte o conjunto de volta para uma lista e a retorna.
  return list(intersecao_conjunto)

# --- Exemplo de uso ---

# Gera duas listas de números inteiros aleatórios
tamanho_lista1 = []
tamanho_lista2 = []


lista1 = []
lista2 = []

for _ in range(3):
    lista1.append(random.randint(1, 5))
    lista2.append(random.randint(1, 5))

print(encontrar_intersecao(lista1, lista2))
