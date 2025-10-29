from random_1 import encontrar_intersecao
import random


def test_encontrar_intersecao(mocker):
    resultados_random = [5, 3, 3, 4, 1, 5]
    # resultado tem que ser [5]
    mock = mocker.patch("random.randint", side_effect=resultados_random)

