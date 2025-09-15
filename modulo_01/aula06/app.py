"""
Programa de banco

1- rodar em loop
2- ter conta e senha(validar)
3- encerrar atendimendo
4- cheque especial (limite de saldo negativo)
5- tentar 3 vezes a senha
6- opções(saque, deposito, saldo)
7- mostrar saldo apos saque
8- alterar a senha
9- dizer o nome usuario ao abrir o aplicativo
10- pagar boleto

"""

conta_corrente = "12345"
senha_usuario = "0000"
saldo_inicial = 0
limite_saldo_negativo = "-500.00"
nome_usuario = "José"

while True:
      for i in range(3):
        conta = input("Entre com a sua conta corrente: ")
        senha = input("Entre com a sua senha: ")
     
        if conta == conta_corrente and senha == senha_usuario:
          print(f"Bem vindo {nome_usuario}")
          acessso_permitido = True
          break
        
        else:
          print("Conta ou Senha invalida! ")
          acessso_permitido=False
        
      if not acessso_permitido:
        break
      while True:
         opcao = input("Escolha uma opção:\n"\
                "1- Ver Saldo\n."\
                "2- Sacar Valor.\n"\
                "3- Depositar.\n" \
                "4- Pagar Boleto.\n"\
                "5- Alterar Senha.\n"\
                "6- Sair.\n")
           
         if opcao ==  "1":
              print(f"Seu saldo atual é de {saldo_inicial}.")
           
         elif opcao == "2":
              valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
              if valor_a_sacar <= (saldo_inicial + limite_saldo_negativo):
                 saldo_inicial -= valor_a_sacar
                 print("saldo liberado, retire seu valor! ")
              else:
                 print("Saldo insuficinte!")
           
         elif opcao == "3":
              depositar = float(input("Insira o valor a ser depositado: "))
              if depositar > 0:
                 saldo_inicial += depositar
              else :
                 print("Valor inválido")    
           

         elif opcao == "4":
            boleto = float(input("Insira o valor do boleto: "))
            
            if boleto <= saldo_inicial:
               saldo_inicial -= boleto
               print("Boleto pago com sucesso!")
            else:
               print("Saldo insuficiente para pagar o boleto")
               
         elif opcao == "5":
              senha_antiga = input("Insira sua senha antiga: ")
              senha_nova = input("Insira sua nova senha: ")
              senha_nova_confirma = input("Confirme sua nova senha: ")
              if senha_antiga == senha_usuario and senha_nova == senha_nova_confirma:
                 senha_usuario = senha_nova
                 print("Senha atualizada com sucesso! ")
              else:
                 print("Senha inválida! ")
                 
         elif opcao =="6":
              print("Atendimento Finalizado")
              break
         else:
              print("Opção Inválida")         
              

