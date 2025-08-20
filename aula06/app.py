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

conta_corrente = "1234546-7"
senha_usuario = "0000"
saldo_inicial = 0
limite_saldo_negativo = "-500.00"
nome_usuario = "José"

while True:
      for i in range(3)
        conta = input("Entre com a sua senha corrente")
        senha = input("Entre com a sua senha")
     
        if conta == conta_corrente and senha == senha_usuario:
          print(f"Bem vindo {nome_usuario}")
          acessso_permitido = True
          break
        
        else:
          print("Conta ou Senha invalida! ")
        
        if not acessso_permitido:
           break
        
        while True:
           opcao = input("Escolha uma opção\n" \
                "1- Ver Saldo.\n"\
                "2- Sacar Valor.\n"\
                "3- Depositar.\n"\                         
                "4- Pagar Boleto.\n"\
                "5- Alterar Senha.\n"\
                "6- Sair.\n")
           if opcao ==  "1":
              pass
           elif opcao == "2":
              pass
           elif opcao == "3":
              pass
           elif opcao == "4":
              pass
           elif opcao == "5":
              pass
           elif opcao =="6":
              print("Atendimento Finalizado")
              break
           else:
              print("Opção Inválida")         
              

