lista_numeros = {15: "impar", 22: "par", 33: "impar", 44: "par"}
for chave, valor in lista_numeros.items():
    if valor == "par":
        print(f"O número {chave} é par.")
    else:
        print(f"O número {chave} é ímpar.")
        