frase = input("Digite uma frase: ")

frase_cod = frase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
print(f"A frase codificada: {frase_cod}")
frase_deco = frase_cod.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("u","5")
print(f"A frase decodificada: {frase_deco}")