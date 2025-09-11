estoque = {"melão": 5, "banana": 8, "laranja": 12}
usuario = input("Digite a  fruta que deseja adicionar!: ")
qtd = int(input("Quantos unidades desejar adicionar ao estoque: "))
if usuario in estoque:
    estoque[usuario] += qtd
else:
    estoque[usuario] = qtd
 
print(f"O novo estoque atualizado: {estoque} ")