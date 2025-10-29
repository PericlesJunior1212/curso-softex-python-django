def somar_listas(lista1, lista2):
  
 
  if len(lista1) > len(lista2):
    lista_maior = lista1
    lista_menor = lista2
  else:
    lista_maior = lista2
    lista_menor = lista1
    
  resultado = []
  
  for i in range(len(lista_maior)):
    try:
      
      soma = lista_maior[i] + lista_menor[i]
      resultado.append(soma)
    except IndexError:

      resultado.append(lista_maior[i])
      
  return resultado

print(somar_listas(lista1, lista2))
