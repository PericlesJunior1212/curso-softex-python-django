def quantidades_pala(frase:str)->int:
    frase_nova = frase.split()
    return len(frase_nova)
def vogais(frase:str)->int:
    vogais = 'aeiouAEIOU'
    cont = 0
    for letra in frase:
        if letra in vogais:
            cont += 1
    return cont
def consoantes(frase:str)->int:
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    cont = 0
    for letra in frase:
        if letra in consoantes:
            cont += 1
    return cont
def palindromo(frase:str)->bool:
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]
def main():
    frase = input("Digite uma frase: ")
    print(f"A frase tem {quantidades_pala(frase)} palavras.")
    print(f"A frase tem {vogais(frase)} vogais.")
    print(f"A frase tem {consoantes(frase)} consoantes.")
    if palindromo(frase):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")
        