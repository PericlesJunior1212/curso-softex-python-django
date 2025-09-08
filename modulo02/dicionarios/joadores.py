jogadores = {"cristiano": 200,"Messi": 198, "Neymar": 450}
soma = 0

print("--------Opções:---------\n")
print("1.Atualizar Pontuação do jogador: \n")
print("2.Adicionar/Pontuar: \n")
try:
   escolha = input("Digite sua escolha: ")
   escolha = int(escolha)
except ValueError:
    print("Entrada inválida, apenas do 1 ou 2.")
   
if escolha == "1":
 for jogador, pontos in jogadores:
   jogador = print("Digite o nome do jogador")
   pontos = print("Digite quantos pontos irá atualizar")
   jogador= pontos =+ soma
   print(soma)
    

    
   
  
