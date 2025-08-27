
numero_tele=input("Digite seu número de telefone: ")
if len(numero_tele)!=11:
    print("Número deve conter 11 digitos")
if not numero_tele.isdigit():
    print("Número deve conter apenas números")
else:
    valido=True
    for c in numero_tele:
        contador=0
        for d in numero_tele:
            if c==d:
                contador+=1
        if contador>3:
            print("Número inválido, contém mais de 3 digitos repetidos")
            valido=False
            break
        if not valido:
            print("Não é um número válido")
        else:
         valido=True
         
         print(f"Seu número formatado é: ({numero_tele[0:2]}) {numero_tele[2:7]}-{numero_tele[7:11]}")   
         break         
                
                
      
    

    
    