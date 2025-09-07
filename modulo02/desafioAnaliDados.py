suc_acess = []
soma = 0
registros_de_acessos=[]


while True :
    acesso_valido = []
    usuario = input("Digite o nome do usuário ou 'parar' para encerrar: ")
    if usuario.lower() == "parar":
            break
    acesso_valido.append(usuario)
    while True:
         status = input("Digite: \n1-Sucesso \n2-Falha \nStatus do usuário: ")

         if  status != "1" and status != "2":
            print("Status inválido. Tente novamente.")
            
         if status == "1":
            status = "Sucesso"
            acesso_valido.append(status)
            suc_acess.append(usuario)
            break
         if status == "2":
            status = "Falha"
            acesso_valido.append(status) 
            break
    while True:
         try:
          duracao_minutos = int(input("Digite o tempo de sessão em minutos: "))
          if duracao_minutos >= 0:
             acesso_valido.append(duracao_minutos)
             break
         except ValueError:
          print("Digite apenas número.")
    if status == "Sucesso" or status== "1":
             soma+=duracao_minutos 
          
    acesso_valido=tuple(acesso_valido)  
    registros_de_acessos.append(acesso_valido)

           
           
print(registros_de_acessos)
print(f"Os login com sucesso:  {suc_acess}")
print(f"Minutagem dos login bem sucedido: {soma}")
        
    


