agenda ={"manada": 986532145, "Meire": 986321514, "nalva": 98635624}
while True:
    print('-----Agenda-----')
    print("1.Adicionar contato:")
    print("2.Buscar contador")
    print("3.Sair")
    try:
      escolha = input("Digite sua escolha: ")
      escolha = int(escolha)
    except ValueError:
      print("Entrada inválida, apenas do 1 a 3.")
    try:
    
     if escolha == 1:
       nome = input("Digite o novo nome na agenda: ")
       telefone = input("Digite o novo número: ")
       agenda [nome] = [telefone]
    except ValueError:
       print("Apenas número.")
     
    if escolha == 2:
       buscar =input("Qual contato desejar buscar")
       buscar in agenda
       print(f"O número encontrado {agenda[buscar]}")
    
    