
def encontrar_par(lista):
    for numero in lista:
     if numero % 2 == 0:
        return numero
    return None
print(encontrar_par ([1, 3, 5, 6, 8]))