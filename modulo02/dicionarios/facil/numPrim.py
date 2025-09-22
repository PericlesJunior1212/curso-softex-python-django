numeros = [1,2,3,4,5,6,7,8,9,10]
primos = []
for numero in numeros:
    eh_primos = True
    if numero < 2:
        eh_primos = False
    else:
        for i in range(2,numero):
            if numero % i ==0:
                eh_primos= False
                break
    if eh_primos:
                primos.append(numero)
print(primos)                
