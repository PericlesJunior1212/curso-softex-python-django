jogadores = {"Cristiano": 200,"Messi": 198, "Neymar": 450}
soma = 0

print("--------Opções:---------\n")
print("1.Atualizar Pontuação do jogador: \n")
print("2.Adicionar/Pontuar: \n")


escolha = input("Digite sua escolha: ")


if escolha == "1":
    jogador = input("Digite o nome do jogador: ").capitalize()
    pontos = int(input("Digite quantos pontos irá atualizar: "))
    
    for jog, pont in jogadores.items():
      if jogador == jog:
         jogadores[jogador] = pont + pontos
    print(f"O jogador {jogador} atualizou: {jogadores[jogador]} pontos")

if escolha == "2":
  
   nov_jog = input("Digite o nome do novo jogador: ")
   nov_pont = input("Digite a nova pontuação do jogador: ")
   
   jogadores[nov_jog] = nov_pont
   print(f"Novo jogador {nov_jog} e pontuação: {jogadores[nov_jog]}")
   print(f"Nova lista de jogadores: {jogadores}")
  

else:
  print("Erro Inválido, digite 1 ou 2")

