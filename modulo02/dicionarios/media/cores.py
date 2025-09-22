cores = {"vermelho": "#FC0101", "verde": "#00FF00", "azul": "#0000FF", "amarelo": "#FFFF00"}

while True :
    print("Para sair digite 'sair' ")
    cores_escolhida = input("Qual cor você que saber em hexadecimais: ")   

    if cores_escolhida in cores:
         print(f"A cor {cores_escolhida} em hexadecimal é: {cores[cores_escolhida]}")
    elif cores_escolhida == "sair":
          break
    else:
        print("Cor não está na lista. ")
    

    
      
     
        
        
    