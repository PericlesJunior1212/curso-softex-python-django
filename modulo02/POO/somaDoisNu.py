def soma_para(altura, peso):
    area = altura * peso
    perimetro = 2* (peso + altura)
    return area, perimetro
# Chamando a função e recebendo a tupla
resultados = soma_para(5, 10)
print(f"Resultado como tupla: {resultados}")
