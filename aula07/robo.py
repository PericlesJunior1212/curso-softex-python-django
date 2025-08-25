posicao = 0

while True:
    opcao=input("Escolha uma Opção:\n"
        "1-Avançar\n" \
        "2-Recuar\n"  \
        "3-Status\n" \
        "4-Desligar\n")
    if opcao =="1":
       posicao+=1
       print(f"A sua nova posição é:{posicao}")
    elif opcao =="2":
       posicao -=1
       print(f"A sua nova posição é:{posicao}")
    elif opcao =="3":
       print(f"A sua nova posição é:{posicao}")
    
    
    elif opcao =="4":
       print(f"Programa Desligdo")
       break
    else:
        print("Opção Inválida")
       
    
       
    