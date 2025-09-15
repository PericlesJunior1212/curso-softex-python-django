def maior_Num(numeros:list)->int:
    if len(numeros) == 0:
        return None
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num
    return maior
numeros=[]
while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")
print("O maior número é:", maior_Num(numeros))


