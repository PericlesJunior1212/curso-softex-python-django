from random_1 import intersecao
import random


def test_intersecao(mocker):
    resultados_random = [5, 3, 3, 4, 1, 5]
    # resultado tem que ser [5]
    mock = mocker.patch("random.randint", side_effect=resultados_random)


    lista_01 = []
    lista_02 = []
    for _ in range(3):
        lista_01.append(random.randint(1, 5))  # [5,3,1]
        lista_02.append(random.randint(1, 5))  # [3,4,5]

    assert intersecao(lista_01, lista_02) == [3, 5]
    assert mock.call_count == 6